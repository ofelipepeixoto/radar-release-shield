"""Build and check this instructions-only plugin with the Python standard library.

These checks verify packaging and source consistency. They do not scan a target
for vulnerabilities, certify instruction behavior, or provide a process sandbox.
Use stable local source copies. Path admission is not a guarantee against
concurrent replacement of ancestor directories or other filesystem races.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import unquote, urlsplit
import zipfile


MAX_ENTRIES = 256
MAX_FILE_BYTES = 1024 * 1024
MAX_TOTAL_BYTES = 4 * 1024 * 1024
WRAPPER = "radar-release-shield"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
EXPECTED_SKILLS = {
    "release-compare", "release-diagnose", "release-fix",
    "release-homologate", "release-refresh", "release-surfaces",
}
FIXED_TIMESTAMP = (2026, 11, 1, 0, 0, 0)


class ValidationError(ValueError):
    """The package does not match the documented, deliberately narrow format."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


@dataclass
class SourceInfo:
    files: dict[str, bytes]
    manifest: dict
    skills: list[str]
    local_links: int

    def summary(self) -> dict:
        return {
            "kind": "structural-package-check",
            "version": self.manifest["version"],
            "files": len(self.files),
            "bytes": sum(map(len, self.files.values())),
            "skills": self.skills,
            "local_links_checked": self.local_links,
            "limits": {"entries": MAX_ENTRIES, "file_bytes": MAX_FILE_BYTES,
                       "total_bytes": MAX_TOTAL_BYTES},
        }


def regular_bytes(path: Path) -> bytes:
    """Reject links and special files before opening them, including FIFO."""
    metadata = path.lstat()
    require(stat.S_ISREG(metadata.st_mode), "Expected a regular file")
    require(metadata.st_size <= MAX_FILE_BYTES, "File-size limit exceeded")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        require(stat.S_ISREG(opened.st_mode), "Opened object is not a regular file")
        require((opened.st_dev, opened.st_ino) == (metadata.st_dev, metadata.st_ino),
                "File changed before reading")
        require(opened.st_size <= MAX_FILE_BYTES, "File-size limit exceeded")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            content = stream.read(MAX_FILE_BYTES + 1)
        after = os.fstat(descriptor)
        require(len(content) <= MAX_FILE_BYTES, "File-size limit exceeded")
        require((opened.st_size, opened.st_mtime_ns, opened.st_ctime_ns) ==
                (after.st_size, after.st_mtime_ns, after.st_ctime_ns),
                "File changed during reading")
        return content
    finally:
        os.close(descriptor)


def read_source_files(source: Path) -> dict[str, bytes]:
    source = Path(source)
    require(stat.S_ISDIR(source.lstat().st_mode), "Source must be a real directory")
    files: dict[str, bytes] = {}
    visited = 0

    def walk(directory: Path) -> None:
        nonlocal visited
        entries = []
        with os.scandir(directory) as iterator:
            for entry in iterator:
                visited += 1
                require(visited <= MAX_ENTRIES, "Source-entry limit exceeded")
                entries.append(entry)
        for entry in sorted(entries, key=lambda item: item.name):
            mode = entry.stat(follow_symlinks=False).st_mode
            require(not stat.S_ISLNK(mode), "Symlinks are not admitted")
            path = Path(entry.path)
            if stat.S_ISDIR(mode):
                walk(path)
            else:
                require(stat.S_ISREG(mode), "Special files are not admitted")
                name = path.relative_to(source).as_posix()
                files[name] = regular_bytes(path)
                require(sum(map(len, files.values())) <= MAX_TOTAL_BYTES,
                        "Source-byte limit exceeded")

    walk(source)
    return files


def json_object(content: bytes, name: str) -> dict:
    try:
        value = json.loads(content.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise ValidationError("Invalid UTF-8 JSON: " + name) from exc
    require(isinstance(value, dict), "JSON root must be an object: " + name)
    return value


def inspect_files(files: dict[str, bytes]) -> SourceInfo:
    require("plugin.json" in files, "Missing root manifest")
    manifest = json_object(files["plugin.json"], "plugin.json")
    require(manifest.get("$schema") == SCHEMA, "Unexpected manifest schema")
    require(manifest.get("name") == WRAPPER, "Unexpected plugin identity")
    require(isinstance(manifest.get("version"), str) and
            re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)",
                         manifest["version"]) is not None, "Invalid release version")
    require(not {"skills", "apps", "interface", "mcpServers"} & manifest.keys(),
            "Nonportable fields at root")
    try:
        openai = manifest["extensions"]["com.openai"]
        interface = openai["interface"]
    except (KeyError, TypeError) as exc:
        raise ValidationError("Missing OpenAI interface") from exc
    require(isinstance(interface, dict), "Interface must be an object")
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(isinstance(interface.get(key), str) and bool(interface[key].strip()),
                "Invalid interface text: " + key)
    require(len(interface["shortDescription"]) <= 30, "Subtitle exceeds 30 characters")
    require(interface["category"] == "Security", "Unexpected category")
    require(isinstance(interface.get("capabilities"), list) and
            all(isinstance(x, str) and x.strip() for x in interface["capabilities"]),
            "Invalid capabilities")
    prompts = interface.get("defaultPrompt")
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3 and
            all(isinstance(x, str) and 0 < len(x) <= 128 and "\n" not in x for x in prompts),
            "Invalid conversation starters")
    require(openai.get("apps") == "./.app.json", "Unexpected app binding location")
    require(".app.json" in files, "Missing app binding")
    binding = json_object(files[".app.json"], ".app.json")
    require(binding == {"apps": {"github": {
        "id": "connector_76869538009648d5b282a4bb21c3d157"}}},
        "Unexpected app binding")
    require(".codex-plugin/plugin.json" in files, "Missing compatibility manifest")
    compatibility = json_object(files[".codex-plugin/plugin.json"], "compatibility manifest")
    for key in ("name", "version", "description", "author", "license", "keywords"):
        require(compatibility.get(key) == manifest.get(key),
                "Compatibility manifest differs: " + key)
    require(compatibility.get("interface") == interface and
            compatibility.get("apps") == "./.app.json" and
            compatibility.get("skills") == "./skills", "Compatibility settings differ")
    require("LICENSE" in files and "third_party/BLA-LICENSE.txt" in files,
            "Required attribution files missing")
    skill_paths = [name for name in files if re.fullmatch(r"skills/[^/]+/SKILL\.md", name)]
    names: list[str] = []
    for name in skill_paths:
        try:
            text = files[name].decode("utf-8")
        except UnicodeError as exc:
            raise ValidationError("Invalid UTF-8 skill") from exc
        # A narrow parser for this repository's frontmatter subset, not a YAML parser.
        match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]*")\n---\n', text)
        require(match is not None, "Unsupported or invalid skill frontmatter")
        skill_name, quoted_description = match.groups()
        try:
            description = json.loads(quoted_description)
        except ValueError as exc:
            raise ValidationError("Invalid quoted description") from exc
        require(isinstance(description, str) and bool(description.strip()),
                "Empty skill description")
        require(skill_name == PurePosixPath(name).parent.name, "Skill folder/name mismatch")
        names.append(skill_name)
    require(set(names) == EXPECTED_SKILLS and len(names) == 6,
            "Expected exactly the six project skills")
    local_links = 0
    for name, content in files.items():
        if name.endswith(".json"):
            json_object(content, name)
        if not name.endswith(".md"):
            continue
        try:
            text = content.decode("utf-8")
        except UnicodeError as exc:
            raise ValidationError("Invalid UTF-8 Markdown") from exc
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                continue
            target = unquote(url.path)
            require("\\" not in target and not target.startswith("/"),
                    "Absolute or nonportable local link")
            parts: list[str] = list(PurePosixPath(name).parent.parts)
            for part in PurePosixPath(target).parts:
                if part == "..":
                    require(bool(parts), "Local link escapes plugin")
                    parts.pop()
                elif part not in ("", "."):
                    parts.append(part)
            require("/".join(parts) in files, "Missing local link target")
            local_links += 1
    return SourceInfo(files, manifest, sorted(names), local_links)


def validate_source(source: Path) -> SourceInfo:
    return inspect_files(read_source_files(Path(source)))


def validate_archive(path: Path, source: Path | None = None) -> dict:
    path = Path(path)
    require(stat.S_ISREG(path.lstat().st_mode), "Archive must be a regular file")
    # The compressed container also needs a bound before ZipFile parses its index.
    require(path.stat().st_size <= MAX_TOTAL_BYTES + MAX_ENTRIES * 1024,
            "Archive-container limit exceeded")
    files: dict[str, bytes] = {}
    total = 0
    try:
        with zipfile.ZipFile(path) as archive:
            entries = archive.infolist()
            require(0 < len(entries) <= MAX_ENTRIES, "Archive-entry limit exceeded")
            for entry in entries:
                name = entry.filename
                parts = PurePosixPath(name).parts
                require("\\" not in name and not name.startswith("/") and
                        len(parts) >= 2 and parts[0] == WRAPPER and
                        all(part not in ("", ".", "..") and ":" not in part for part in parts) and
                        "/".join(parts) == name,
                        "Noncanonical or escaping archive entry")
                mode = entry.external_attr >> 16
                require(stat.S_IFMT(mode) in (0, stat.S_IFREG) and not entry.is_dir() and
                        not entry.external_attr & 0x10, "Nonregular archive entry")
                require(not entry.flag_bits & 1, "Encrypted archive not admitted")
                require(entry.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED),
                        "Unsupported compression")
                require(entry.file_size <= MAX_FILE_BYTES, "Archive file-size limit exceeded")
                total += entry.file_size
                require(total <= MAX_TOTAL_BYTES, "Archive-byte limit exceeded")
                relative = "/".join(parts[1:])
                require(relative not in files, "Duplicate archive entry")
                with archive.open(entry) as stream:
                    content = stream.read(MAX_FILE_BYTES + 1)
                require(len(content) == entry.file_size and len(content) <= MAX_FILE_BYTES,
                        "Archive expanded beyond declared limit")
                files[relative] = content
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError, EOFError) as exc:
        raise ValidationError("Invalid or unsupported ZIP") from exc
    info = inspect_files(files)
    if source is not None:
        require(files == validate_source(Path(source)).files,
                "Archive contents differ from source")
    return info.summary()


def archive_path(source: Path, destination: Path) -> Path:
    info = validate_source(source)
    return Path(destination) / f'{WRAPPER}-v{info.manifest["version"]}.zip'


def build_archive(source: Path, destination: Path) -> Path:
    info = validate_source(source)
    output = Path(destination) / f'{WRAPPER}-v{info.manifest["version"]}.zip'
    output.parent.mkdir(parents=True, exist_ok=True)
    require(not output.is_symlink() and
            (not output.exists() or stat.S_ISREG(output.lstat().st_mode)),
            "Output must not be a symlink or special file")
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, content in sorted(info.files.items()):
            entry = zipfile.ZipInfo(WRAPPER + "/" + relative, date_time=FIXED_TIMESTAMP)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(entry, content)
    validate_archive(output, source)
    checksum = output.with_suffix(output.suffix + ".sha256")
    require(not checksum.is_symlink() and
            (not checksum.exists() or stat.S_ISREG(checksum.lstat().st_mode)),
            "Checksum must not be a symlink or special file")
    checksum.write_text(hashlib.sha256(output.read_bytes()).hexdigest() + "  " + output.name + "\n")
    return output


def verify_package(source: Path, destination: Path) -> dict:
    path = archive_path(source, destination)
    result = validate_archive(path, source)
    checksum = regular_bytes(path.with_suffix(path.suffix + ".sha256")).decode("ascii").strip()
    expected = hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name
    require(checksum == expected, "Checksum does not match archive")
    return {**result, "archive": path.name, "sha256": expected.split()[0]}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "build", "verify"))
    parser.add_argument("--source", type=Path)
    parser.add_argument("--dist", type=Path)
    args = parser.parse_args(argv)
    repository = Path(__file__).resolve().parents[1]
    source = args.source or repository / "plugin"
    destination = args.dist or repository / "dist"
    try:
        if args.command == "check":
            result = validate_source(source).summary()
        elif args.command == "build":
            build_archive(source, destination)
            result = verify_package(source, destination)
        else:
            result = verify_package(source, destination)
    except (ValidationError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "failed", "reason": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "passed", **result}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
