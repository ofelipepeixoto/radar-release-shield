---
name: release-surfaces
description: "Revisar exposição de código, frontend, API, aplicativos, binários, bancos, agentes, prompts ou MCP antes de distribuir software autorizado. Usar para aprofundar uma superfície específica."
---

# Revisar por superfície

Ler [regras comuns](../../references/working-rules.md), [superfícies](../../references/surfaces.md) e [evidência](../../references/evidence-policy.md). Se faltar identidade ou escopo, aplicar release-diagnose primeiro.

1. Selecionar apenas as superfícies presentes e as perguntas relevantes. Para cada ativo, relacionar perfil de acesso, confidencialidade esperada e barreira técnica.
2. Inspecionar fonte e configuração permitidas; comparar com o material efetivamente distribuído quando disponível. Registrar quando só houver fonte interna ou só captura de interface.
3. Para API e isolamento, usar fixtures e perfis definidos com testes positivos e negativos. Resposta isolada 401/403 não demonstra separação entre clientes. Se não houver autorização para teste ativo, preparar a matriz e declarar execução pendente.
4. Para banco, preferir schema, migrações, grants e políticas. Sem conector autorizado, não afirmar que o banco real foi examinado. Não coletar linhas de clientes para descobrir estrutura nem executar migrações no diagnóstico.
5. Para binários ou pacotes, registrar suporte real do formato; análise estática não equivale a instrumentação. Não executar software desconhecido sem controles de runtime verificados conforme as regras comuns.
6. Preservar licença, atribuição, diagnóstico autorizado, acessibilidade, SEO e modo offline requeridos. Ao propor mover lógica ao servidor, explicitar custo novo ou desconhecido, rede/latência sem medição inventada, efeito offline e decisão necessária. Ausência de ofuscação ou anti-debug sozinha não confirma vulnerabilidade.
7. Preencher [relatório](../../templates/report.md) com evidências redigidas, limitações e risco residual. Identificar o próximo teste específico que resolveria cada incerteza.

Revalidar documentação aplicável usando [fontes](../../references/sources.md). Não transformar escolhas de arquitetura em garantias de irrecuperabilidade.
