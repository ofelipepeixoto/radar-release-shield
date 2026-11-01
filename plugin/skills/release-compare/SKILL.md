---
name: release-compare
description: "Comparar baseline e candidata protegida com objetivos verificáveis de recuperação e adulteração autorizadas; usar Kraken AI REA quando suas capacidades reais estiverem disponíveis."
---

# Comparar versões com Kraken

Ler [regras comuns](../../references/working-rules.md), [protocolo de comparação](../../references/kraken-comparison.md) e [evidência](../../references/evidence-policy.md). A presença desta skill não instala REA ou cria avaliador independente.

1. Definir objetivos finitos e acessos autorizados antes da análise, usando [plano comparativo](../../templates/comparison.md).
2. Fixar baseline/candidata, hashes, perfil, ambiente, ferramentas/modelos, entradas, orçamento, critérios de sucesso e parada. Não comparar cenários com acessos diferentes sem declarar a assimetria.
3. Entregar ao avaliador apenas os artefatos e acessos previstos. Se houver fonte, respostas ou patch no contexto do avaliador, registrar contaminação; não chamar o ensaio de cego ou independente. Não instruir o avaliador a desistir de engenharia reversa.
4. Usar ferramentas anunciadas. Sem REA disponível, executar somente inspeção estática possível e marcar instrumentação não realizada. Código desconhecido requer isolamento e limites reais verificados.
5. Medir apenas o que as ferramentas observarem. Separar tempo de parede, CPU, memória, tokens e custos medidos dos estimados ou desconhecidos. Timeout, silêncio, erro ou limite de tokens não provam proteção.
6. Executar o mesmo conjunto de objetivos em ambas as versões, preservar regressões funcionais e registrar objetivos atingidos, itens recuperados e completude. Não publicar material confidencial recuperado.
7. Entregar comparação por objetivo com limitações e risco residual. Relacionar cada conclusão ao cenário, acessos e orçamento. Não extrapolar para toda IA, ferramenta ou adversário.

Salvar [checkpoint](../../templates/checkpoint.md) se o cenário não puder ser concluído. Avaliação de instruções em subagente é simulação de comportamento do plugin, não teste da resistência de uma release.
