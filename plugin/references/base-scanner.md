# Scanner-base externo

Snapshot histórico conferido em 01/11/2026 de um scanner externo do mesmo autor, em fonte restrita autorizada. O código e o acesso a essa fonte não são distribuídos por este repositório. Revalidar identidade e permissões se o operador fornecer o scanner em outro trabalho.

## O que existe

Scanner Python 0.1.0 local de leitura, com biblioteca padrão, Python >=3.12 e primitivas POSIX exigidas. Linux testado; não presumir homologação Windows/macOS. A CLI fornece `inspect`, `file-id` e MCP `stdio` experimental. `release_inspect` aceita somente `{}` e usa a raiz escolhida pelo operador ao iniciar o processo.

Cobertura sempre `partial`. Examina apenas `.js`, `.cjs`, `.mjs`, `.ts`, `.css`, `.map`, `.json`, `.py` e `.html` admitidos. Regras por marcador: referência `sourceMappingURL`, dois cabeçalhos de chave privada e um marcador de papel de LLM; também identifica texto em `sourcesContent` de source map versão 3 simples.

Referência inline não é decodificada ou buscada. Mapas indexados e formatos inválidos têm lacuna. Marcador de chave não prova chave válida; marcador de conversa não prova prompt injection. Não detecta todos os tipos de segredo ou exposição.

## Tetos e fronteiras

| Controle | Teto ou comportamento |
| --- | --- |
| Entradas | 512 |
| Bytes por arquivo | 262144, 256 KiB |
| Leitura total | 2097152, 2 MiB |
| Profundidade | Oito níveis |
| Prazo | Cinco segundos cooperativos |
| Symlinks, hardlinks, arquivos especiais | Recusados |
| Escrita no alvo, execução do alvo, rede | Não oferecidos pelo scanner |
| ZIP ou outro pacote | Não extrai |
| Relatório | IDs, hashes, regras e limitações; sem conteúdo/caminhos do alvo |

Primitivas de descritor relativo e `O_NOFOLLOW` protegem a admissão, não criam sandbox de processo. Não há snapshot atômico da árvore. Leituras podem atualizar atime. Ordem de enumeração sob limites pode mudar amostra. `traversal_completed` não transforma cobertura parcial em integral. Hash de caminho ou conteúdo não autentica origem e pode permitir inferência por tentativa.

O JSON permanece `radar-release-guard/v1`. Não alterá-lo nem acrescentar um schema de relatório executável silenciosamente. O plugin usa modelos Markdown para revisão humana. Mapeamento por caminho conhecido pode usar `file-id` localmente, sem introduzir caminhos hostis no relatório.

## Usar quando disponível

Obter cópia autorizada em ref fixa, ler código e regras locais, verificar integridade e ambiente. Executar a CLI do checkout com uma cópia local estável escolhida pelo operador. Substituir o argumento somente por caminho autorizado; não construir comandos com interpolação de nomes hostis.

```bash
python3 -m radar_release_guard inspect examples/release
python3 -m unittest discover -s tests -q
```

Esses comandos são da base, não ferramentas nativas deste plugin. Não instalar dependências nem executar scripts desconhecidos só para diagnosticar. Separar execução de código do scanner revisado da execução do alvo, que não ocorre neste modo.

Sem checkout/runtime, seguir revisão assistida e marcar scanner indisponível. Este pacote não inclui ou instala scanner, servidor, REA ou transporte remoto. Não há HTTP/OAuth validado, crawler, análise geral de banco nem proteção automática. Não converter stdio em serviço público por ponte genérica.

## Proveniência

Lidos na criação: README.md, scanner.py, mcp.py, __main__.py, __init__.py, SECURITY.md, AGENTS.md, LICENSE, THIRD_PARTY_NOTICES.md, testes e licença BLA. Inventário privado do ecossistema não foi necessário. Código-base não foi alterado por esta criação. A licença MIT e a atribuição de Carlos Felipe são preservadas. BLA é referência histórica indireta; seus geradores de confusão, exaustão e anti-debug não estão no plugin.
