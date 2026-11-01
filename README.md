# Radar Release Shield

**Proteção antes da publicação.**

Um plugin para ajudar você a revisar uma solução no ChatGPT antes de homologar. Ele organiza o que está exposto, o que precisa continuar privado, quais correções merecem prioridade e como verificar o resultado.

[Baixar o plugin ZIP](https://github.com/ofelipepeixoto/radar-release-shield/raw/refs/heads/main/dist/radar-release-shield-v0.1.1.zip) · [Instalar no ChatGPT](docs/INSTALAR.md) · [Como usar](docs/USAR.md) · [Eficácia e limites](docs/EFICACIA.md)

## Para que serve

- Revisar código e arquivos de distribuição de projetos próprios ou autorizados.
- Procurar exposição desnecessária de fontes, mapas, regras de negócio, dados, prompts e segredos, com as ferramentas realmente disponíveis.
- Preparar correções com impacto, teste e reversão explicados.
- Comparar duas versões com os mesmos objetivos e acessos.
- Registrar evidências, lacunas e um parecer antes da homologação.

O código-fonte do plugin são suas **instruções, manifestos, referências e modelos**. Esta versão não inclui um scanner próprio, servidor, acesso automático a banco ou mecanismo de blindagem. Os scripts Python deste repositório verificam e empacotam o plugin; não analisam vulnerabilidades de aplicações.

## Comece por aqui

1. [Baixe o ZIP](https://github.com/ofelipepeixoto/radar-release-shield/raw/refs/heads/main/dist/radar-release-shield-v0.1.1.zip).
2. Siga o [passo a passo de instalação](docs/INSTALAR.md).
3. Selecione Radar Release Shield numa conversa e envie seu projeto ou repositório autorizado.
4. Peça: **“Revisar esta solução antes da homologação.”**

Você recebe um resumo simples, tabela de riscos, prioridades, testes realizados e o que ainda falta verificar. Para repositórios, a leitura depende da conexão e das permissões do seu GitHub.

## Os seis fluxos

| Pedido | Fluxo |
| --- | --- |
| Revisar antes da homologação | Diagnóstico e escopo |
| Examinar frontend, API, banco, aplicativo ou agente | Revisão por superfície |
| Preparar correções para reduzir exposição | Correção revisável |
| Comparar duas releases com o Kraken | Comparação por objetivos, quando houver ferramentas |
| Saber se pode seguir para homologação | Checklist e parecer limitado |
| Revisar uma versão nova | Atualização de fontes e evidências |

São pedidos de conversa. Não são comandos nativos ou controles de segurança instalados na sua aplicação.

## Funciona mesmo?

As instruções têm uma avaliação inicial por cenários, registrada com seus limites. O projeto também oferece testes reproduzíveis de estrutura, integridade e empacotamento. O [relatório de eficácia](docs/EFICACIA.md) separa isso dos 27 testes históricos de um scanner externo, que não vem neste ZIP.

**A utilidade inicial é organizar e melhorar a revisão. Ainda não há evidência de proteção geral contra engenharia reversa.** Uma análise só pode concluir sobre o artefato, os acessos, as ferramentas e os testes registrados. Código entregue ao cliente continua sujeito a análise.

## O que tem no repositório

| Pasta | Conteúdo |
| --- | --- |
| [plugin](plugin) | Fonte completa do plugin, seis skills, referências e modelos |
| [dist](dist) | ZIP instalável e SHA-256 |
| [docs](docs) | Instalação, uso, eficácia, privacidade e manutenção |
| [scripts](scripts) | Validação e empacotamento em Python |
| [tests](tests) | Testes dos scripts, inclusive entradas inválidas |

## Para quem desenvolve

Com Python 3.12 ou superior, na raiz do projeto, sem pacotes externos:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/package_tools.py check
python3 scripts/package_tools.py build
python3 scripts/package_tools.py verify
```

Consulte [como manter e testar](docs/DESENVOLVER.md). O fluxo automático no GitHub verifica o pacote; ele não substitui avaliação do modelo ou teste de uma solução real.

## Versão e licença

Edição pública **0.1.1**, preparada a partir do pacote privado 0.1.0 fornecido pelo autor. Mudanças desta edição: minimização de metadados, documentação pública e ferramentas de empacotamento. A lógica das seis skills foi preservada. A cópia privada existente no ChatGPT não é atualizada automaticamente.

Publicar este repositório não publica o plugin no diretório da OpenAI. Cada pessoa cria ou importa sua cópia, conforme os recursos e permissões da conta. Este projeto não tem selo de verificação da OpenAI.

Autoria: **Carlos Felipe**. [Licença MIT](LICENSE) · [Origem e atribuições](THIRD_PARTY_NOTICES.md) · [Segurança](SECURITY.md).
