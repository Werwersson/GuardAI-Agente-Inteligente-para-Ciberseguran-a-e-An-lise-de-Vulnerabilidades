# Skill: Análise de Vulnerabilidades

## O que é

Esta skill transforma o GuardAI Agent em um mentor de análise de vulnerabilidades. Em vez de simplesmente apontar falhas, ele conduz o estudante por todo o processo que um analista de segurança profissional seguiria:

1. **Coleta de contexto** — entender o sistema antes de analisar.
2. **Identificação** — encontrar vulnerabilidades usando OWASP Top 10 e CWE.
3. **Classificação** — avaliar impacto, probabilidade e severidade.
4. **Explicação** — mostrar como a falha seria explorada (educação, não receita de ataque).
5. **Correção** — orientar a mitigação com exemplos de código.
6. **Relatório** — documentar tudo num formato padronizado e profissional.
7. **Validação** — verificar se a correção foi efetiva.

## Por que ela existe

Um chat genérico de IA, ao receber código vulnerável, tende a:
- Apontar a falha e entregar a correção pronta, sem explicar o porquê.
- Não perguntar o contexto (ambiente, quem acessa, que dados processa).
- Não classificar severidade com base em risco real.
- Não usar frameworks de referência (OWASP, MITRE ATT&CK, CWE).

O GuardAI com esta skill **pergunta antes de agir**, **classifica com critério** e **ensina o processo**, não apenas o resultado.

## Como usar

Abra o projeto no harness e converse com o agente. Exemplos de prompts:

- "Analise este código Python e me diga se tem alguma vulnerabilidade."
- "Tenho um servidor Ubuntu exposto na internet. O que devo verificar?"
- "Este Dockerfile está seguro para produção?"
- "Revise esta configuração do nginx antes do deploy."

O agente vai perguntar o contexto, analisar, classificar e orientar a correção.

## Estrutura

```
skills/vulnerability-analysis/
├── SKILL.md    # Roteiro que o agente segue (lido automaticamente pelo harness)
└── README.md   # Este arquivo (documentação para humanos)
```

## Formato de saída

Toda análise segue o formato padronizado definido em `agent/knowledge/security-basics.md`:

```
## [SEVERIDADE] Nome da Vulnerabilidade
CWE, OWASP, MITRE ATT&CK
Descrição → Impacto → Probabilidade → Evidência → Recomendação → Referências
```

## Referências

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
