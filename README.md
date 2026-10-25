# 🛡️ GuardAI — Agente Inteligente para Cibersegurança e Análise de Vulnerabilidades

> Mentor de IA especializado em cibersegurança que analisa vulnerabilidades como um profissional — perguntando antes de agir, avaliando impacto, probabilidade e severidade, e orientando a correção.

Evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent), especializado em **cibersegurança e análise de vulnerabilidades**. O agente não recebeu nenhum treinamento especial — ele aprendeu pelo que está escrito nos arquivos de skill, conhecimento e persona.

---

## 🎯 Especialização: por que cibersegurança?

O DIO Agent original é um mentor generalista. O **GuardAI** expande esse conceito para a área de segurança da informação, com um diferencial claro:

| Chat genérico de IA | GuardAI Agent |
|---------------------|---------------|
| Aponta a falha e entrega a correção pronta | **Pergunta o contexto** antes de analisar |
| Não classifica severidade | Classifica com **impacto, probabilidade e severidade** |
| Não referencia frameworks | Usa **OWASP Top 10, MITRE ATT&CK, CWE** |
| Não ensina o processo | **Ensina a conduzir** a análise, não apenas o resultado |
| Pode sugerir ações sem contexto | **Confirma ambiente e autorização** antes de qualquer orientação |

---

## 📁 Arquivos criados e alterados

### Arquivos novos (segurança)

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| `skills/vulnerability-analysis/SKILL.md` | Skill | Roteiro completo de análise de vulnerabilidades em 7 etapas |
| `skills/vulnerability-analysis/README.md` | Documentação | Explica a skill para humanos |
| `skills/security-testing/SKILL.md` | Skill | Orienta testes de segurança (pentest, SAST, DAST) em lab |
| `skills/security-testing/README.md` | Documentação | Explica a skill para humanos |
| `skills/security-study-path/SKILL.md` | Skill | Monta trilhas de estudo personalizadas em cibersegurança |
| `skills/security-study-path/README.md` | Documentação | Explica a skill para humanos |
| `agent/knowledge/security-basics.md` | Conhecimento | Base de cibersegurança: tríade CIA, OWASP, MITRE, CWE, boas práticas |
| `app.py` | Código vulnerável | App Flask com SQL Injection e outras falhas (para teste) |
| `app_secure.py` | Código corrigido | Mesma app com todas as vulnerabilidades mitigadas |
| `test_lab.py` | Testes automatizados | Suíte com 8 testes unitários comprovando falhas e mitigações |
| `requirements.txt` | Dependências | Dependências do laboratório (Flask, Werkzeug, pytest, requests) |

### Arquivos alterados (do DIO Agent original)

| Arquivo | O que mudou |
|---------|-------------|
| `AGENTS.md` | Adicionada persona de segurança, base de conhecimento de segurança, 3 novas skills na tabela, regras de conduta em segurança |
| `agent/persona.md` | Personalidade reescrita para mentor de cibersegurança com valores éticos, especialidades técnicas e limites de atuação |

### Arquivos herdados e complementares (do DIO Agent)

| Arquivo | Descrição |
|---------|-----------|
| `skills/study-plan/SKILL.md` & `README.md` | Plano de estudos (skill original e doc) |
| `skills/unblock-challenge/SKILL.md` & `README.md` | Destravar desafio (skill original e doc) |
| `skills/explain-concept/SKILL.md` & `README.md` | Explicar conceito (skill original e doc) |
| `agent/knowledge/dio-platform.md` | Conhecimento sobre a plataforma DIO, bootcamps e gamificação |
| `agent/knowledge/learning-experiences.md` | Tipos de experiências educacionais e desafios da DIO |
| `CLAUDE.md` | Compatibilidade com Claude Code |
| `docs/glossary.md` | Glossário de termos do projeto e de cibersegurança |

---

## 🚀 Como rodar o agente no Harness

### 1. Instale um Harness

| Harness | Documentação |
|---------|-------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |

### 2. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/guardai-agente-ciberseguranca.git
cd guardai-agente-ciberseguranca
```

### 3. Abra no Harness

> ⚠️ **Importante:** abra o terminal na pasta do projeto. Se abrir em outro lugar, o harness não encontra os arquivos.

**Com Hermes:**
```bash
cd guardai-agente-ciberseguranca
hermes
```

**Com Antigravity:**
```bash
cd guardai-agente-ciberseguranca
agy
```

**Com Claude Code:**
```bash
cd guardai-agente-ciberseguranca
claude
```

O harness lê automaticamente o `AGENTS.md` e carrega toda a configuração do agente.

---

## 🧪 Teste: análise do app.py vulnerável

### Passo 1 — Peça a análise

Abra o harness na pasta do projeto e envie:

```
Como especialista em AppSec, analise o arquivo app.py.
Encontre as vulnerabilidades, explique como um atacante as exploraria,
cite a técnica do MITRE ATT&CK correspondente e reescreva o código corrigido.
```

### O que o agente faz (diferente de um chat genérico):

1. **Pergunta o contexto** — É produção ou lab? Quem acessa? Que dados processa?
2. **Analisa com framework** — Identifica SQL Injection (CWE-89, OWASP A03), senhas em plaintext (CWE-256, OWASP A02), etc.
3. **Classifica cada achado** — Impacto, probabilidade, severidade (Crítica/Alta/Média/Baixa).
4. **Explica a exploração** — Como `admin' OR '1'='1' --` funciona, com referência ao MITRE ATT&CK (T1190).
5. **Orienta a correção** — Mostra consultas parametrizadas, hashing de senhas, variáveis de ambiente.
6. **Gera relatório padronizado** — No formato definido em `security-basics.md`.

### Passo 2 — Valide a correção

Depois de corrigir (ou veja `app_secure.py`), peça:

```
Analise o app_secure.py e confirme se as vulnerabilidades do app.py foram mitigadas.
```

### Passo 3 — Teste com cenário de infraestrutura

```
Tenho um servidor Ubuntu de laboratório exposto na internet, rodando SSH na porta 22,
Apache na 80 e MySQL na 3306. O que devo verificar primeiro?
```

O agente deve **perguntar** antes de sugerir:
- É ambiente de produção ou lab?
- Quem administra o servidor?
- Existe firewall configurado?
### Passo 4 — Executar a suíte de testes automatizada

Você pode comprovar a eficácia das mitigações executando a suíte de testes inclusa:

```bash
# Instale as dependências se necessário
pip install -r requirements.txt

# Execute os 8 testes automatizados
python test_lab.py
```

A suíte executará 8 asserções de segurança:
- `test_sql_injection_bypass`: comprova que a injeção SQL burla a autenticação no `app.py`.
- `test_sql_injection_blocked`: comprova que o `app_secure.py` bloqueia o payload (HTTP 401).
- `test_plaintext_password_in_db`: comprova a ausência de hash no `app.py`.
- `test_password_hashed_in_db`: valida hash PBKDF2:SHA256 no `app_secure.py`.
- `test_security_headers_present`: valida headers `nosniff`, `DENY` e `CSP`.
- `test_unauthenticated_users_endpoint_blocked`: valida proteção de rota com 401/403.

---

## 🔍 Vulnerabilidades encontradas no app.py

| # | Vulnerabilidade | Severidade | CWE | OWASP |
|---|----------------|-----------|-----|-------|
| 1 | SQL Injection no login | **Crítica** | CWE-89 | A03:2021 |
| 2 | Senhas em texto plano | **Alta** | CWE-256 | A02:2021 |
| 3 | Secret key hardcoded | **Alta** | CWE-798 | A02:2021 |
| 4 | Debug mode ativo | **Alta** | CWE-489 | A05:2021 |
| 5 | Senha retornada na API | **Alta** | CWE-200 | A01:2021 |
| 6 | Endpoint /users sem autorização | **Alta** | CWE-862 | A01:2021 |
| 7 | Mensagem de erro expõe query SQL | **Média** | CWE-209 | A09:2021 |
| 8 | Sem rate limiting | **Média** | CWE-307 | A07:2021 |
| 9 | Sem headers de segurança | **Baixa** | CWE-693 | A05:2021 |

---

## 🌟 Melhorias implementadas (além do desafio base)

1. **Skill de testes de segurança** (`skills/security-testing/`) — orienta pentest, SAST, DAST e montagem de lab.
2. **Skill de trilha de estudos em cibersegurança** (`skills/security-study-path/`) — plano personalizado por perfil.
3. **Saída padronizada** — todo achado segue o formato: Impacto → Probabilidade → Severidade → Evidência → Recomendação.
4. **Código corrigido** (`app_secure.py`) — demonstra antes/depois com todas as mitigações.
5. **Suíte de testes de segurança automatizada** (`test_lab.py`) — validação prática dos testes de intrusão e defesas.
6. **Base de conhecimento abrangente** — OWASP Top 10, MITRE ATT&CK, CWE, NIST CSF, boas práticas de AppSec, infraestrutura e DevSecOps.

---

## 📂 Estrutura do projeto

```
guardai-agente-ciberseguranca/
├── AGENTS.md                              # Configuração principal do agente
├── CLAUDE.md                              # Compatibilidade com Claude Code
├── README.md                              # Documentação completa do projeto
├── app.py                                 # ⚠️ App Flask VULNERÁVEL (para teste)
├── app_secure.py                          # ✅ App Flask CORRIGIDA
├── test_lab.py                            # 🧪 Suíte de testes automatizados (8 testes)
├── requirements.txt                       # Dependências do laboratório
├── .gitignore
│
├── agent/
│   ├── persona.md                         # Personalidade do GuardAI
│   └── knowledge/
│       ├── security-basics.md             # Base de cibersegurança (OWASP, MITRE, CIA)
│       ├── dio-platform.md                # Base sobre a DIO, bootcamps e reputação
│       └── learning-experiences.md        # Formatos pedagógicos e regras de mentoria
│
├── skills/
│   ├── vulnerability-analysis/            # 🆕 Skill principal (7 etapas)
│   │   ├── SKILL.md
│   │   └── README.md
│   ├── security-testing/                  # 🆕 Skill de testes ofensivos/defensivos
│   │   ├── SKILL.md
│   │   └── README.md
│   ├── security-study-path/               # 🆕 Skill de trilhas em cibersegurança
│   │   ├── SKILL.md
│   │   └── README.md
│   ├── study-plan/                        # Herdada do DIO Agent
│   │   ├── SKILL.md
│   │   └── README.md
│   ├── unblock-challenge/                 # Herdada do DIO Agent
│   │   ├── SKILL.md
│   │   └── README.md
│   └── explain-concept/                   # Herdada do DIO Agent
│       ├── SKILL.md
│       └── README.md
│
└── docs/
    └── glossary.md                        # Glossário de termos técnicos
```

---

## 📚 Referências

- [DIO Agent (repositório base)](https://github.com/digitalinnovationone/dio-agent)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

## ⚖️ Aviso Legal

Este projeto é **exclusivamente educacional**. O código vulnerável (`app.py`) foi criado para demonstrar falhas de segurança em ambiente controlado. **Nunca** use técnicas de exploração em sistemas sem autorização explícita do proprietário. Testes de segurança sem permissão são crime (Art. 154-A do Código Penal Brasileiro).
