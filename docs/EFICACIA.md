# Eficácia: o que foi verificado

Data: 01/11/2026. Edição pública: 0.1.1. O objeto desta revisão é um plugin de instruções e referências, não uma ferramenta de blindagem aplicada a uma solução.

**Conclusão: há utilidade metodológica inicial. A eficácia contra engenharia reversa de aplicações reais ainda não foi demonstrada.** Não há base para porcentagem de proteção, nota geral de segurança ou promessa contra toda IA.

## Evidências separadas

| Categoria | Evidência | O que sustenta | O que não sustenta |
| --- | --- | --- | --- |
| Estrutura atual | Manifestos, seis skills, referências, fonte/ZIP e hash verificados pelos scripts publicados | Integridade e organização do pacote examinado | Segurança de uma aplicação ou qualidade universal de respostas |
| Código atual | Testes automatizados dos scripts, incluindo ZIPs inválidos, divergências e limites | Comportamento dos validadores/empacotador nos casos executados | Detecção de vulnerabilidades, segredos ou resistência de binários |
| Comportamento histórico | 14 cenários textuais na criação 0.1.0; um precisou de ajuste e reteste | Respostas consideradas adequadas naquele conjunto | Independência, cegamento ou taxa geral de acerto |
| Comportamento atual | Quatro novos cenários textuais da edição pública, registrados separadamente | Uso das instruções no conjunto atual | Execução real de scanner, banco, API ou alvo |
| Código externo histórico | 27 testes de um scanner local externo e fixture de três sinais sintéticos | Funcionamento daquele scanner nos testes registrados | Scanner dentro deste plugin, teste executado novamente aqui ou nova integração no ChatGPT |
| Uso real do plugin original | O proprietário selecionou a cópia 0.1.0 nesta tarefa; as instruções foram usadas na revisão assistida | Um uso assistido com GitHub disponível nesta sessão | Instalação da 0.1.1 em outra conta, comportamento universal ou homologação de produto |
| Ensaio adversarial instrumentado | Não realizado | Nenhuma conclusão de resistência | Proteção contra reconstrução, extração ou adulteração em geral |

O [registro da criação](../plugin/evaluation/results.md) e as [respostas históricas resumidas](../plugin/evaluation/scenario-responses.md) foram preservados como histórico. Não são testes novos da edição pública. O modelo usado nessa avaliação histórica não foi identificado de forma verificável; há resumos do criador, não transcrições completas. O conjunto de critérios estava acessível ao avaliador.

O [registro atual](avaliacao-publica.md) descreve comandos, resultados e cenários desta publicação. Os testes de código podem ser repetidos sem API paga ou modelo, usando apenas Python. A avaliação de linguagem depende do modelo e da sessão e precisa de nova observação para cada contexto relevante.

## Resultado prático esperado

O plugin deve ajudar a separar uma suspeita de um problema confirmado, evitar cópia de segredos no relatório, reconhecer material necessariamente público, organizar correções e impedir conclusões baseadas apenas em timeout, build verde ou uma única resposta 401/403.

As instruções **não impõem** autorização, isolamento, orçamento de processo ou bloqueio de rede. Esses controles precisam existir no ambiente. O vínculo com GitHub depende da conexão individual e das permissões reais. Não há crawler, análise geral de banco, ofuscador, REA ou scanner instalado pelo ZIP.

## O que falta medir

- Ensaios baseline/candidata com artefatos reais autorizados, mesmos acessos, objetivos e orçamento.
- Avaliadores com fonte privada e patch fora do contexto quando a plataforma permitir, registrando contaminação residual.
- Recuperação por objetivo, completude, tempo e recursos efetivamente medidos.
- Regressões funcionais, acessibilidade, desempenho e modo offline após correções.
- Instalação e uso por pessoas de outras contas, com suas conexões e permissões.

Não calcular eficácia como “quantidade de achados evitados” sem controlar o que foi entregue ao avaliador. Falha de ferramenta, timeout ou falta de acesso significam limite do ensaio. Um aplicativo que deixa de funcionar também não é uma candidata aprovada.

## Risco residual

Quem recebe código, dados ou regras no próprio dispositivo pode analisá-los. Tirar divulgação desnecessária e aplicar autorização no servidor reduz exposição, mas há decisões de custo, rede, latência e funcionamento offline. Minificação, compilação, WASM ou instruções para o avaliador parar não garantem sigilo.

Evidências antigas só são reaproveitadas quando a identidade e a relevância forem justificadas. Mudanças documentais e de metadados da edição pública preservaram os bytes das seis skills, conforme a comparação registrada. Isso sustenta reutilizar o histórico como histórico, sem convertê-lo em ensaio independente novo.

[Voltar ao início](../README.md)
