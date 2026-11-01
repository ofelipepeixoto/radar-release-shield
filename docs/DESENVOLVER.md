# Manter, verificar e empacotar

Requisito para os scripts: Python 3.12 ou superior. Sem dependência externa de runtime e sem chamada de rede. Os scripts operam sobre a fonte do plugin, não executam a solução que será analisada.

Na raiz do repositório:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/package_tools.py check
python3 scripts/package_tools.py build
python3 scripts/package_tools.py verify
```

`check` confere a estrutura. `build` gera o ZIP com um único diretório raiz e o arquivo SHA-256. `verify` relaciona o pacote distribuído à fonte e ao checksum. As validações têm escopo e tetos explícitos no código; não são um scanner de vulnerabilidades nem um extrator para arquivos recebidos arbitrariamente.

Os testes negativos verificam falhas de estrutura, referências, links, metadados e integridade. Consulte os nomes dos testes em [tests](../tests) e o resultado da rodada em [avaliação pública](avaliacao-publica.md).

## Alterar o plugin

1. Edite `plugin/`.
2. Incremente a versão nos dois manifestos, preservando identidade e compatibilidade.
3. Execute os testes e reconstrua o ZIP.
4. Faça uma revisão do diff e do conteúdo distribuído.
5. Reavalie os cenários afetados. Registre o que foi feito e o que não foi testado.

Não altere resultados históricos para parecerem novos. O workflow do GitHub usa leitura de conteúdo, valida o pacote e executa os testes. Não usa segredos, não publica versões no ChatGPT e não implanta uma aplicação.

Não adicione `.app.json` e vínculo de apps a um pacote de submissão ao diretório público sem seguir os requisitos oficiais atuais. O ZIP deste repositório é para criação/importação privada compatível, não uma submissão verificada pela OpenAI.

## Origem da edição pública

O autor forneceu a exportação 0.1.0. Seu SHA-256 original foi conferido: `f9bd9c102f71365865e9eabdeacb162a2341839481a03e1339fbb3e01a6557e2`.

Na 0.1.1 foram removidos contato de conta e referências internas de aquisição. Licenças e atribuições foram mantidas. Nenhum código do scanner externo ou inventário de repositórios privados foi incorporado. A cópia privada já existente no ChatGPT permaneceu na versão 0.1.0.

[Voltar ao início](../README.md)
