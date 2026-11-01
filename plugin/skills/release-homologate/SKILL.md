---
name: release-homologate
description: "Consolidar evidências e checklist de uma release antes da homologação, emitir parecer limitado e reavaliar quando hash, configuração ou exposição mudarem."
---

# Emitir parecer no escopo

Ler [regras comuns](../../references/working-rules.md), [evidência](../../references/evidence-policy.md) e [checklist](../../templates/homologation.md).

1. Conferir identidade dos artefatos, ambiente e escopo contra os testes. Hash diferente invalida automaticamente a aplicação irrestrita do parecer anterior; mapear partes afetadas. Reutilizar evidência de código idêntico por mudança documental somente com justificativa verificável.
2. Revisar achados `candidate`, `confirmed`, `false_positive` e `accepted_risk`. Aceitação humana não apaga confirmação técnica. Não inventar responsável ou aprovação.
3. Separar validação estrutural de pacote, testes automatizados, avaliação comportamental das instruções, simulações e uso real no ChatGPT. Cada categoria precisa de evidência própria ou estado pendente/não aplicável justificado.
4. Verificar funcionalidade e fluxos de erro afetados. Parser ou build verde não substitui jornada funcional. Testes não executados continuam pendentes, sem presumir resultado.
5. Aplicar critérios do checklist. Bloqueio crítico confirmado no escopo impede parecer apto; lacuna em controle essencial permanece bloqueio ou parcial justificado. Não usar nota média para encobrir bloqueios.
6. Emitir um dos pareceres: `BLOQUEADO`, `PARCIAL`, `APTO_PARA_HOMOLOGACAO_NO_ESCOPO` ou `REAVALIAR_POR_MUDANCA`. Registrar separadamente aceitação de risco pendente ou documentada e autorização de produção.
7. Entregar [relatório](../../templates/report.md) com risco residual e [checkpoint](../../templates/checkpoint.md). Parecer técnico não autoriza merge, deploy ou publicação.

Para avaliar o próprio plugin, usar [casos de aceitação](../../evaluation/acceptance-cases.md). Não confundir a aprovação do pacote de instruções com a segurança do alvo do usuário.
