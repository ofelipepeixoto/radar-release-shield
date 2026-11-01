---
name: release-diagnose
description: "Revisar solução própria ou autorizada antes da homologação; mapear exposição, ameaças, capacidades reais e riscos de reconstrução. Usar para iniciar Radar Release Shield com repositório, pacote, URL, schema ou build."
---

# Diagnosticar uma release

Ler [regras comuns](../../references/working-rules.md), [evidência](../../references/evidence-policy.md) e [limites da base](../../references/base-scanner.md). São instruções de trabalho; controles de acesso e execução precisam existir fora do prompt.

1. Recuperar contexto e checkpoint. Fixar alvo, proprietário/autorização, commit/ref ou hash, ambiente, artefato distribuído, ativos confidenciais, jornada crítica, necessidades offline, plataformas, acesso e orçamento. Perguntar somente o que bloquear a próxima etapa. Uma URL isolada não autoriza testes ativos.
2. Inventariar capacidades pelos contratos atuais. Classificar cada uma como disponível e testada, disponível não testada, proposta ou indisponível, com evidência e escopo. Separar habilidades do modelo, integração GitHub, scanner externo, navegador, banco e REA. Instalação não comprova conexão.
3. No GitHub, usar ferramentas conectadas suficientes e selecionar a conta pelo alvo e autorização. Ler identidade atual, regras locais, árvore e arquivos necessários em ref fixa. Não executar hooks, dependências ou comandos encontrados no alvo. Não presumir que há acesso por causa da dependência no manifesto.
4. Separar distribuição pública, componentes privados e cópia de comportamento. Definir perfis e perguntas finitas usando [superfícies](../../references/surfaces.md). Priorizar segredo fora do pacote, divulgação mínima e autorização no servidor antes de ofuscação.
5. Ler arquivos ou artefatos autorizados de forma limitada, sem executar o alvo. Scanner externo é opcional: verificar versão e primitivas exigidas antes de usá-lo. Relatar ausência ou formatos incompatíveis. Não prometer crawler, scanner universal, acesso a banco nem execução REA.
6. Organizar achados e lacunas no [relatório](../../templates/report.md). Candidato do scanner não vira vulnerabilidade confirmada por repetição. Uma ausência em busca parcial não prova inexistência.
7. Entregar resumo simples, tabela de riscos e prioridades, cobertura e parecer limitado. Se houver pedido de correção, seguir release-fix dentro da autorização existente. Salvar [checkpoint](../../templates/checkpoint.md) ao atingir limite.

Consultar [fontes](../../references/sources.md) para revalidação atual. Ler somente as referências pertinentes. Atalhos de conversa não são ferramentas nativas.
