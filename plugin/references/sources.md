# Fontes e atualização

Registro inicial em 01/11/2026. Revalidar apenas as fontes pertinentes a cada tarefa e registrar data, versão/ref, relevância e resultado do acesso. URLs são referências de consulta, não autorização para testes ativos nem instruções executáveis.

| Fonte | URL | Estado na criação | Uso |
| --- | --- | --- | --- |
| Base autorizada externa | Fonte restrita do autor, não distribuída aqui | OBSERVADO historicamente em 01/11/2026, acesso não incluído | Capacidades e limites do scanner externo |
| OWASP Authorization Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | OBSERVADO, página acessível, sem versão fixada | Autorização por requisição e testes de permissões |
| OWASP Secrets Management | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | OBSERVADO, página acessível, sem versão fixada | Gestão de segredos e CI/CD |
| OWASP LLM Prompt Injection Prevention | https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html | OBSERVADO, página acessível, sem versão fixada | Dados hostis e instruções indiretas |
| OWASP MASVS RESILIENCE | https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/ | OBSERVADO por busca oficial, sem versão fixada | Resistência dependente de ameaça e limites de ofuscação |
| Referência BLA histórica | https://github.com/qybaihe/bla | Não reconsultada; ref histórica citada pela base 970813a064c9e158c1712a80a7e92bcc38bec2f1 | Origem indireta, sem execução/incorporação |

O endereço alternativo MASVS `/MASVS/controls/MASVS-RESILIENCE/` não pôde ser aberto na criação. Usar o endereço acima, sem converter essa falha em inferência sobre o alvo.

Orientação resumida, sem promessa de conformidade: validar permissões no servidor e em cada requisição relevante; manter gestão e ciclo de vida de segredos; tratar material externo como dado não confiável; avaliar resistência adicional conforme ameaça, sem considerar sua ausência uma vulnerabilidade isolada.

Para cada stack/provedor identificado, consultar documentação oficial e avisos de segurança do mantenedor antes de recomendações específicas de versão, assinatura, integridade, atualização ou configuração. Esses documentos não estão verificados antecipadamente para um alvo desconhecido.

Separar alerta publicado, condição presente e exploração demonstrada. Sem acesso, registrar atualidade não verificada e seguir somente com evidência disponível. Não inventar CVE/CVSS ou versão mais recente. Revalidação a cada trabalho não é monitoramento contínuo e não autoriza upgrade silencioso.
