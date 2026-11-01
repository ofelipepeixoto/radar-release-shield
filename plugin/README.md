# Radar Release Shield 0.1.1

Proteção antes da publicação.

Plugin privado de instruções e referências para revisar exposição de soluções próprias ou autorizadas antes da homologação. Organiza riscos, evidências, correções revisáveis e comparação entre versões. Inclui seis workflows e integração declarada com o GitHub já disponível ao usuário. Não cria servidor novo.

## Como usar

Selecionar o plugin no chat e fornecer repositório, pacote, URL autorizada, schema ou build, mais a versão que será distribuída. Reaproveitar o contexto e as autorizações já existentes. Pedir, por exemplo:

- “Revisar esta solução antes da homologação.”
- “Mapear o que um agente consegue recuperar desta release.”
- “Preparar correções para reduzir exposição.”
- “Comparar baseline e candidata com o Kraken.”
- “Revalidar proteção desta nova versão.”

São atalhos de conversa. Não são ferramentas nativas nem comandos de segurança instalados no alvo.

## O que cada workflow faz

| Workflow | Resultado |
| --- | --- |
| release-diagnose | Identidade, escopo, capacidades e prioridades |
| release-surfaces | Revisão assistida da superfície escolhida |
| release-fix | Correções concretas, testes e PR quando autorizados |
| release-compare | Comparação por objetivos e orçamento, com Kraken quando disponível |
| release-homologate | Checklist e parecer técnico limitado |
| release-refresh | Revalidação rastreável de versões, fontes e evidências |

Consultar os [modelos de relatório](templates/report.md), [checklist](templates/homologation.md), [comparação](templates/comparison.md) e [checkpoint](templates/checkpoint.md). A política de evidência está em [references/evidence-policy.md](references/evidence-policy.md); os 14 critérios de comportamento em [evaluation/acceptance-cases.md](evaluation/acceptance-cases.md).

## Limites reais

O scanner Radar Release Guard é externo e opcional, com cobertura parcial. Este pacote não inclui executável, scanner universal, crawler, acesso a banco, servidor MCP próprio, OAuth próprio, sandbox, REA instalado, proteção automática ou agendador. Instruções de orçamento precisam ser acompanhadas e controles de execução precisam existir no runtime.

GitHub depende da conexão e permissões da sessão. Banco, navegador e REA precisam estar realmente disponíveis para uso. O plugin não promete impedir toda engenharia reversa ou reconstrução por IA. Código entregue ao cliente continua sujeito a análise; o objetivo é reduzir exposição e proteger partes privadas com barreiras técnicas verificáveis.

Criação do plugin, seleção no chat e uso real são estados diferentes. A validação do pacote e as simulações não homologam aplicações do usuário nem autorizam produção. Consultar o relatório de validação entregue com a versão para saber o que foi executado.

Não há nova hospedagem ou serviço pago no pacote. Os produtos e runtimes usados mantêm suas próprias condições. Sem monitoramento contínuo automático; referências são revalidadas a cada trabalho.

## Origem

Origem: scanner experimental externo do mesmo autor, consultado com autorização em 01/11/2026. Seu código não faz parte deste pacote público. Atribuições e licença em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) e [LICENSE](LICENSE). Não houve modificação do repositório-base por esta criação.

A edição pública 0.1.1 remove contato de conta e referências internas desnecessárias. Não atualiza automaticamente a cópia privada 0.1.0. Instruções de instalação e evidência nova estão na documentação do repositório público.
