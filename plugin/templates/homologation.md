# Checklist de homologação no escopo

Preencher com SIM, NÃO, PENDENTE ou NÃO APLICÁVEL justificado e evidência identificada. Não usar caixas vazias como aprovação presumida.

| Verificação | Estado | Evidência ou limite |
| --- | --- | --- |
| Autorização, alvo, versão/hash e distribuição fixados | PENDENTE | |
| Perfis, ativos e ameaças relevantes definidos | PENDENTE | |
| Capacidades reais e controles de runtime separados de instruções | PENDENTE | |
| Segredos e material privado ausentes da distribuição examinada ou achados tratados | PENDENTE | |
| Autorização de recursos privados testada no servidor com fixtures e perfis pertinentes | PENDENTE | |
| Critérios essenciais de acesso entre clientes cobertos, além de resposta isolada 401/403 | PENDENTE | |
| Pacote, assinatura, atualização e cadeia de build revisados quando aplicáveis | PENDENTE | |
| Prompts, ferramentas e documentos privados revistos quando aplicáveis | PENDENTE | |
| Licenças e avisos preservados | PENDENTE | |
| Jornadas e fluxos de erro afetados preservados, incluindo offline quando exigido | PENDENTE | |
| Testes estruturais, código, comportamento, simulações e uso real separados | PENDENTE | |
| Comparação antes/depois concluída ou ausência explicitada | PENDENTE | |
| Referências pertinentes revalidadas ou marcadas não verificadas | PENDENTE | |
| Achados, lacunas, cobertura e risco residual documentados | PENDENTE | |
| Hash e configuração continuam compatíveis com as evidências | PENDENTE | |

Parecer técnico: escolher `BLOQUEADO`, `PARCIAL`, `APTO_PARA_HOMOLOGACAO_NO_ESCOPO` ou `REAVALIAR_POR_MUDANCA` com justificativa. Bloqueio crítico confirmado impede apto. Lacuna essencial impede conclusão irrestrita; justificar bloqueado ou parcial conforme o escopo. Mudança relevante exige reavaliar partes afetadas.

Aceitação humana do risco: PENDENTE ou DOCUMENTADA, com responsável e registro reais se disponíveis. Autorização de produção: registrar separadamente, sem presumir a partir do parecer. Não criar nota global de segurança.
