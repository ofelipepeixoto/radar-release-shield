# Relatório de revisão antes da homologação

Preencha os campos com evidência do trabalho. Remova instruções de preenchimento antes da entrega. Não inclua segredos, dados de clientes, fonte recuperada ou prompts privados.

## Resumo

- Projeto e objetivo: [preencher]
- Data da revisão e responsável técnico, se conhecido: [preencher sem inventar identidade]
- Conclusão técnica: [BLOQUEADO / PARCIAL / APTO_PARA_HOMOLOGACAO_NO_ESCOPO / REAVALIAR_POR_MUDANCA]
- Motivo e efeito prático da conclusão: [preencher]
- Aceitação humana de risco: [pendente / documentada, com referência mínima]
- Próximo passo necessário: [preencher]

Este parecer se limita ao cenário, à versão e ao orçamento registrados. Não constitui aprovação humana de produção.

## Identidade, autorização e escopo

| Campo | Registro |
| --- | --- |
| Proprietário e autorização existente | [origem, ações e limites autorizados] |
| Repositório, cópia local, pacote ou URL | [identificador redigido quando necessário] |
| Commit/ref e hash do artefato | [identidade efetivamente verificada] |
| Ambiente e plataforma | [preencher] |
| Artefato realmente distribuído | [preencher] |
| Ativos confidenciais | [preencher] |
| Perfis e acessos avaliados | [anônimo, autenticado, destinatário ou operador do dispositivo] |
| Jornada crítica e funcionamento offline | [preencher] |
| Objetivos finitos e critérios de sucesso/parada | [preencher] |
| Restrições, orçamento e ações excluídas | [preencher] |

## Capacidades e cobertura

| Capacidade ou superfície | Estado da capacidade | Versão/ferramenta e evidência | Cobertura e lacunas |
| --- | --- | --- | --- |
| [preencher] | [disponível e testada / disponível não testada / proposta / indisponível] | [preencher] | [preencher] |

| Categoria de validação | Estado | Procedimento e resultado observado | Limite da conclusão |
| --- | --- | --- | --- |
| Estrutural | [não executada / executada / bloqueada] | [preencher] | [preencher] |
| Código | [não executada / executada / bloqueada] | [preencher] | [preencher] |
| Comportamento das instruções | [não executada / executada / bloqueada] | [preencher] | [preencher] |
| Simulação técnica com fixtures ou mocks | [não executada / executada / bloqueada] | [preencher] | [preencher] |
| Uso real no ChatGPT | [não executada / executada / bloqueada] | [preencher] | [preencher] |

Declare explicitamente scanner externo, banco conectado, execução instrumentada, REA e recursos de runtime que não foram examinados ou usados. O pacote de instruções não inclui essas capacidades.

## Tabela de riscos

| ID | Natureza da afirmação | Estado do achado | Superfície e ativo | Versão/hash e localização redigida | Ameaça e pré-condições | Evidência | Severidade e motivo | Confiança e motivo | Correção e prioridade | Teste executado e resultado | Limitações e risco residual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ID] | [OBSERVADO / INFERIDO / PROPOSTO / DESCONHECIDO] | [candidate / confirmed / false_positive / accepted_risk] | [preencher] | [preencher] | [preencher] | [referência mínima] | [preencher] | [preencher] | [preencher] | [ou não executado] | [preencher] |

Se a tabela ficar extensa, use uma linha resumida por achado e detalhe cada um abaixo. Não omita campos exigidos. Não use média ou nota global para ocultar um bloqueio crítico.

## Detalhamento do achado [ID]

- Natureza da afirmação e estado: [preencher]
- Superfície, versão/hash e localização redigida: [preencher]
- Ativo, ameaça e pré-condições: [preencher]
- Evidência mínima e origem: [preencher sem valores de segredos]
- Severidade justificada e confiança: [preencher separadamente]
- Correção proposta ou preparada, arquivo/configuração: [preencher]
- Impacto funcional, alternativa e reversão: [preencher]
- Teste executado, ambiente, entradas e resultado: [preencher ou não executado]
- Limitações e risco residual: [preencher]
- Confirmação técnica: [evidência ou pendência]
- Aceitação humana: [pendente ou referência documentada, com escopo e responsável conhecido]

## Plano priorizado

| Ordem | Mudança concreta | Motivo e achados relacionados | Impacto e alternativa | Teste necessário | Reversão | Autorização aplicável e estado |
| --- | --- | --- | --- | --- | --- | --- |
| [preencher] | [arquivo/configuração] | [preencher] | [preencher] | [preencher] | [preencher] | [proposto / preparado / implementado / validado] |

Informe patches preparados e onde podem ser revisados. Diferencie proposta, implementação e validação. Merge, release, deploy e mudanças em produção só entram como executados quando houver autorização e evidência.

## Comparação baseline e candidata

Estado: [não realizada / parcial / realizada]. Motivo: [preencher]. Não preencha resultados presumidos.

| Condição | Baseline | Candidata |
| --- | --- | --- |
| Versão e hash | [preencher] | [preencher] |
| Artefato e perfil de acesso | [preencher] | [preencher] |
| Ferramentas/modelos, ambiente e entradas | [preencher] | [preencher] |
| Orçamento e critérios de parada | [preencher] | [preencher] |
| Fonte privada no contexto do avaliador | [sim/não/desconhecido e evidência] | [sim/não/desconhecido e evidência] |

| Objetivo e critério de sucesso | Baseline: resultado e evidência | Candidata: resultado e evidência | Tempo e recursos medidos | Limitações |
| --- | --- | --- | --- | --- |
| [preencher] | [atingido / não atingido / inconclusivo / não executado] | [atingido / não atingido / inconclusivo / não executado] | [ou não medidos; estimativas separadas] | [preencher] |

Registre itens recuperados e completude sem reproduzir conteúdo confidencial. Não chame o ensaio de cego ou independente se o contexto estiver contaminado. Uma falha do avaliador não prova resistência universal.

## Referências e atualidade

| URL ou fonte | Versão/edição | Data da consulta | Relevância | Atualidade |
| --- | --- | --- | --- | --- |
| [preencher] | [ou não identificada] | [preencher] | [preencher] | [verificada no escopo / não verificada / desatualizada] |

Separe vulnerabilidade publicada, condição presente no alvo e exploração demonstrada. Liste licenças e avisos preservados quando relevantes.

## Orçamento e pendências

- Chamadas, tempo e ciclos efetivamente acompanhados: [preencher ou não medidos]
- Limites de runtime efetivamente verificados: [preencher ou indisponíveis]
- Tetos do scanner externo, se usado, e limites atingidos: [preencher]
- Falhas, repetições seguras, itens não examinados e bloqueios concretos: [preencher]
- Mudanças posteriores que invalidam ou exigem reavaliação: [preencher]
- Evidências reaproveitadas e justificativa de identidade: [preencher]
- Checkpoint para continuidade: [referência mínima]

Consulte [a política de evidência](../references/evidence-policy.md) para interpretar os estados e as categorias.
