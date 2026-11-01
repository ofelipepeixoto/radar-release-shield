---
name: release-refresh
description: "Revalidar referências oficiais, versões e evidências do Radar Release Shield a cada trabalho ou mudança relevante; usar para atualizar conhecimento e revisar nova versão sem atualização silenciosa de produção."
---

# Revalidar referências e versão

Ler [regras comuns](../../references/working-rules.md), [fontes](../../references/sources.md) e [base do scanner](../../references/base-scanner.md).

1. Identificar mudanças de hash, build, dependências, exposição, configuração e modelo de ameaça. Preservar checkpoints e testes ainda válidos com justificativa.
2. Conferir estado atual do repositório-base e ferramentas pelos contratos reais, em vez de confiar no snapshot deste pacote. Registrar ref consultada, URL e data, mais diferenças relevantes em relação à base registrada.
3. Consultar documentação oficial da stack/provedor, OWASP e avisos dos mantenedores que respondam às perguntas atuais. Registrar versão, data, relevância e acesso observado. Fonte inacessível ou não consultada fica não verificada; não inventar versão mais recente, CVE, CVSS, preço ou compatibilidade.
4. Separar vulnerabilidade publicada, condição presente no alvo e exploração demonstrada. Não importar alertas de uma dependência de nome parecido ou versão não comprovada.
5. Atualizar relatório e plano de reteste das partes afetadas. Atualizar referências não autoriza alterar bibliotecas, pacote do plugin ou produção silenciosamente.
6. Encerrar após resolver perguntas finitas ou alcançar orçamento. Monitoramento contínuo exige solicitação, agendador, escopo, fontes e orçamento próprios. Instalar este plugin não cria agendamento.

Salvar [checkpoint](../../templates/checkpoint.md) e declarar atualidade por fonte. Quando o pedido for atualizar o plugin, preservar identidade e público e seguir o fluxo atual do Plugin Creator.
