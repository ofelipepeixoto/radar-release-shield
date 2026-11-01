---
name: release-fix
description: "Preparar ou implementar correções autorizadas que reduzam exposição de uma release, com patch, impacto, testes e reversão. Usar após diagnóstico ou pedido concreto de ajuste."
---

# Preparar correções

Ler [regras comuns](../../references/working-rules.md), [superfícies](../../references/surfaces.md) e [evidência](../../references/evidence-policy.md). Separar sugestão, alteração preparada, teste executado e implantação.

1. Fixar baseline e evidências do problema. Identificar risco, ativo, pré-condições e objetivo mensurável. Não aplicar transformações por uma nota de resistência.
2. Preparar mudança concreta por achado: arquivo/configuração, justificativa, impacto, alternativa, teste de eficácia, regressão funcional e reversão ou dificuldade de reversão.
3. Quando houver pedido de implementação, usar branch isolada e preservar alterações alheias e originais. Alterar o mínimo pertinente, aproveitando autorização existente. Não reescrever uma stack saudável.
4. Priorizar remover divulgação desnecessária e proteger recursos privados com autorização efetiva. Se um segredo real puder ter sido distribuído, redigir evidência e preparar plano de remoção e rotação; não revogar, reescrever histórico ou registrar valor sem autorização aplicável.
5. Avaliar custo, latência e offline antes de mover lógica ao servidor. Para ofuscação seletiva, preservar licenças, contratos, acessibilidade, observabilidade e diagnóstico legítimo. Não adicionar mecanismos de confusão de agentes, exaustão ou evasão de ferramentas de segurança.
6. Rodar testes proporcionais às mudanças e jornadas representativas, com entradas, saídas e falhas esperadas. Parsing ou compilação aprovados não preservam por si o funcionamento. Se quebrar fluxo necessário, reprovar e corrigir ou reverter.
7. Comparar exposição e regressões antes/depois com condições equivalentes. Para ensaio Kraken, seguir release-compare. Limitar a dois ciclos; ao restar lacuna, salvar checkpoint.
8. Entregar patch e PR revisável quando suportados e cobertos pelo pedido. Merge, release, deploy, domínio, autenticação, credenciais e banco de produção precisam de autorização que cubra a ação. Preparar o resultado concreto antes de solicitar o que realmente faltar.

Registrar resultado em [relatório](../../templates/report.md) e [checklist](../../templates/homologation.md). Corrigir código não significa aprovação humana de produção.
