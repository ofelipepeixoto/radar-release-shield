# Como usar

Selecione Radar Release Shield na conversa. Para um trabalho real, envie o repositório ou pacote que você tem autorização para revisar, a versão que será distribuída e o que precisa continuar privado. O plugin aproveita contexto e permissões já definidos.

## Primeiro diagnóstico

```text
Revisar esta solução antes da homologação.
O projeto é meu. A versão a distribuir é [commit ou hash].
Quero preservar [ativos privados] e manter funcionando [jornada crítica].
Comece pela leitura. Mostre evidências, riscos e correções prioritárias.
```

O esperado é uma análise com identidade do alvo, capacidades disponíveis, achados e lacunas. Uma busca sem resultados não prova ausência de exposição.

## Conferir a instalação com dados sintéticos

Cole este cenário. Ele não contém senha, chave ou dado de cliente:

```text
Revisar esta fixture sintética antes da homologação.
Meu frontend público distribui app.js e app.js.map.
O map tem sourcesContent não vazio. Preciso manter o modo offline.
Não execute nada nem copie fonte no relatório.
Explique o risco, uma correção possível e o que ainda falta verificar.
```

Uma resposta adequada reconhece a possível recuperação da fonte distribuída, propõe reduzir divulgação desnecessária e mantém explícito o que não foi testado. Se sugerir servidor, explica custo, rede, latência e impacto offline. Este cenário textual testa a resposta das instruções; não executa scanner nem comprova uma barreira técnica no seu produto.

## Preparar correções

```text
Prepare correções concretas para os achados confirmados no escopo autorizado.
Use uma branch isolada. Explique impacto, teste e reversão.
Preserve o trabalho existente e entregue uma mudança revisável.
```

## Comparar versões

```text
Compare baseline [hash] e candidata [hash].
Use os mesmos objetivos, perfil de acesso, ferramentas e orçamento.
Declare contaminação de contexto e capacidades ausentes.
Não trate timeout como prova de proteção.
```

Kraken AI REA pode apoiar o método quando suas skills ou ferramentas estiverem disponíveis. Sua presença não prova que há um runtime de instrumentação instalado.

## Ler o parecer

| Parecer | Significado |
| --- | --- |
| BLOQUEADO | Há bloqueio relevante no escopo registrado |
| PARCIAL | Faltam evidências para concluir o escopo |
| APTO_PARA_HOMOLOGACAO_NO_ESCOPO | Os critérios examinados sustentam avançar para homologação naquele cenário |
| REAVALIAR_POR_MUDANCA | Mudança relevante exige rever as partes afetadas |

Nenhum desses estados autoriza produção por conta própria. Aprovação humana de riscos é registrada separadamente. Hash novo, dependência, configuração ou exposição nova podem invalidar evidências anteriores.

[Voltar ao início](../README.md)
