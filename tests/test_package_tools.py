"""Structural and admission checks, not a vulnerability or effectiveness suite."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_tools", ROOT / "scripts/package_tools.py")
tools = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tools
SPEC.loader.exec_module(tools)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "plugin"
        shutil.copytree(ROOT / "plugin", self.source)
        self.dist = self.base / "dist"

    def build(self):
        return tools.build_archive(self.source, self.dist)

    def replace_manifest(self, relative, **changes):
        path = self.source / relative
        data = json.loads(path.read_text())
        data.update(changes)
        path.write_text(json.dumps(data))

    def zip_entries(self, entries):
        path = self.base / "invalid.zip"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in entries:
                archive.writestr(name, content)
        return path

    def test_source_and_archive_roundtrip(self):
        summary = tools.validate_source(self.source).summary()
        self.assertEqual(len(summary["skills"]), 6)
        path = self.build()
        self.assertEqual(tools.validate_archive(path, self.source)["files"], summary["files"])
        self.assertEqual(tools.verify_package(self.source, self.dist)["sha256"],
                         hashlib.sha256(path.read_bytes()).hexdigest())

    def test_deterministic_build(self):
        first = self.build().read_bytes()
        other = self.base / "other"
        second = tools.build_archive(self.source, other).read_bytes()
        self.assertEqual(first, second)

    def test_divergent_manifest_version(self):
        self.replace_manifest(".codex-plugin/plugin.json", version="9.0.0")
        with self.assertRaisesRegex(tools.ValidationError, "differs"):
            tools.validate_source(self.source)

    def test_missing_skill(self):
        (self.source / "skills/release-compare/SKILL.md").unlink()
        with self.assertRaisesRegex(tools.ValidationError, "six project skills"):
            tools.validate_source(self.source)

    def test_source_entry_limit_before_collecting_directory(self):
        oversized = self.base / "oversized-source"
        oversized.mkdir()
        for number in range(257):
            (oversized / f"{number:03}.txt").touch()
        with self.assertRaisesRegex(tools.ValidationError, "Source-entry limit"):
            tools.read_source_files(oversized)

    def test_invalid_frontmatter_description(self):
        path = self.source / "skills/release-compare/SKILL.md"
        path.write_text(path.read_text().replace('description: "', 'description: unquoted "', 1))
        with self.assertRaisesRegex(tools.ValidationError, "frontmatter"):
            tools.validate_source(self.source)

    def test_local_link_escape_and_missing_target(self):
        path = self.source / "extra.md"
        for link in ("../outside.md", "missing.md", "%2e%2e/outside.md"):
            with self.subTest(link=link):
                path.write_text("[link](" + link + ")")
                with self.assertRaises(tools.ValidationError):
                    tools.validate_source(self.source)

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks not available")
    def test_source_symlink(self):
        os.symlink(self.source / "LICENSE", self.source / "link.md")
        with self.assertRaisesRegex(tools.ValidationError, "Symlinks"):
            tools.validate_source(self.source)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO not available")
    def test_source_fifo_rejected_before_read(self):
        os.mkfifo(self.source / "pipe.md")
        with self.assertRaisesRegex(tools.ValidationError, "Special files"):
            tools.validate_source(self.source)

    def test_archive_traversal_and_absolute_entry(self):
        for name in ("../outside", "/outside", "radar-release-shield/../outside",
                     "radar-release-shield/./file", "radar-release-shield\\file",
                     "radar-release-shield/file:stream"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(tools.ValidationError, "entry"):
                    tools.validate_archive(self.zip_entries([(name, b"x")]))

    def test_archive_symlink_and_fifo(self):
        for kind in (stat.S_IFLNK, stat.S_IFIFO):
            with self.subTest(kind=kind):
                entry = zipfile.ZipInfo("radar-release-shield/link")
                entry.external_attr = (kind | 0o644) << 16
                path = self.zip_entries([(entry, b"LICENSE")])
                with self.assertRaisesRegex(tools.ValidationError, "Nonregular"):
                    tools.validate_archive(path)

    def test_archive_entry_file_and_total_limits(self):
        cases = [
            ([(f"radar-release-shield/{i}", b"") for i in range(257)], "entry"),
            ([("radar-release-shield/large", b"x" * (tools.MAX_FILE_BYTES + 1))], "file-size"),
            ([(f"radar-release-shield/{i}", b"x" * tools.MAX_FILE_BYTES)
              for i in range(5)], "byte"),
        ]
        for entries, message in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(tools.ValidationError, message):
                    tools.validate_archive(self.zip_entries(entries))

    def test_archive_source_bytes_mismatch(self):
        path = self.build()
        original = path.read_bytes()
        with zipfile.ZipFile(path) as archive:
            records = [(i, archive.read(i)) for i in archive.infolist()]
        with zipfile.ZipFile(path, "w") as archive:
            for entry, content in records:
                if entry.filename.endswith("/README.md"):
                    content += b"\nChanged byte\n"
                archive.writestr(entry, content)
        self.assertNotEqual(original, path.read_bytes())
        with self.assertRaisesRegex(tools.ValidationError, "differ from source"):
            tools.validate_archive(path, self.source)

    def test_checksum_mismatch(self):
        path = self.build()
        path.with_suffix(".zip.sha256").write_text("0" * 64 + "  " + path.name + "\n")
        with self.assertRaisesRegex(tools.ValidationError, "Checksum"):
            tools.verify_package(self.source, self.dist)

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks not available")
    def test_build_rejects_dangling_output_link(self):
        self.dist.mkdir()
        path = tools.archive_path(self.source, self.dist)
        outside = self.base / "outside.zip"
        os.symlink(outside, path)
        with self.assertRaisesRegex(tools.ValidationError, "symlink"):
            self.build()
        self.assertFalse(outside.exists())

    def test_malformed_and_duplicate_archive(self):
        path = self.base / "bad.zip"
        path.write_bytes(b"not a ZIP")
        with self.assertRaisesRegex(tools.ValidationError, "Invalid"):
            tools.validate_archive(path)
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            path = self.zip_entries([("radar-release-shield/LICENSE", b"a"),
                                     ("radar-release-shield/LICENSE", b"b")])
        with self.assertRaisesRegex(tools.ValidationError, "Duplicate"):
            tools.validate_archive(path)


if __name__ == "__main__":
    unittest.main()
