# Protocolo de comparação

Pergunta: o que um analista autorizado consegue recuperar dos artefatos distribuídos e quais mudanças reduzem a exposição no cenário testado?

1. Definir conjunto finito de objetivos: recuperar fonte por map entregue, localizar segredo sintético, acessar recurso privado sem permissão no ambiente de teste, inferir regra marcada como sensível ou adulterar pacote sem detecção. Marcar não aplicável com justificativa.
2. Fixar duas versões comparáveis, seus hashes, distribuição, perfil do analista, acessos, ferramentas/modelos, ambiente, entradas, orçamento e critérios de sucesso/parada antes da execução.
3. Fornecer somente o artefato e os acessos do perfil. Manter fonte privada, respostas esperadas e patch fora do contexto do avaliador quando a plataforma permitir. Não presumir isolamento entre agentes ou chats. Registrar o que foi exposto; se contaminado, não chamar de cego ou independente.
4. Avaliar baseline e candidata com o mesmo protocolo, usando instâncias separadas quando disponíveis para reduzir aprendizagem cruzada. Registrar ordem e contaminação residual. Se o mesmo avaliador retiver conhecimento da baseline, declarar essa assimetria.
5. Kraken AI REA é referência de método e skills; descobrir ferramentas reais. Fonte integral normalmente usa ferramentas comuns de repositório. REA só é necessário para questões de artefato distribuído, decompilação, instrumentação ou comportamento que a leitura não esclareceu.
6. Separar estática de execução. Sem ferramenta anunciada ou instalação verificada, marcar REA não realizado. Execução de binários ou pacotes exige isolamento e limites reais verificados antes de começar.
7. Registrar objetivos atingidos, material recuperado em descrição mínima redigida, completude e recursos medidos. Não inventar CPU, memória, tempo, tokens ou gasto. Separar medição, estimativa e desconhecido.
8. Timeout, falha de parser, incompatibilidade, silêncio ou orçamento esgotado significam limite do ensaio. Não significam irrecuperabilidade. Um agente cooperativo que obedece a aviso para parar não mede barreira técnica.
9. Preservar jornada, erros, acessibilidade, desempenho e offline pertinentes. Parsing/build aprovados não demonstram equivalência funcional. Regressão importante reprova a candidata mesmo que reduza recuperação.
10. Relatar resultados por objetivo e acesso, mais lacunas e risco residual. Conclusões só valem para versões, cenário e orçamento testados. Não inferir proteção contra todos os modelos, ferramentas ou adversários.

Não há exigência de multiagentes. Pode haver revisão estática por uma única sessão, declarada como tal. Não gerar prompt injection, exaustão de tokens, anti-debug invasivo ou instruções de desistência como contraparte do teste.
