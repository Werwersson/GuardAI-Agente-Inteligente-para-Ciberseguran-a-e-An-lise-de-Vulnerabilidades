---
name: vulnerability-analysis
description: Use quando o estudante quer analisar código, configuração ou infraestrutura em busca de falhas de segurança. Conduz uma análise estruturada com impacto, probabilidade e severidade, orientando a correção sem entregar tudo pronto.
---

# Skill: Análise de Vulnerabilidades

Conduz o estudante por uma análise de segurança profissional: da coleta de contexto até o relatório final com recomendações de correção. O agente age como um analista de segurança sênior orientando um júnior.

## Quando usar

O estudante quer:
- Analisar código-fonte em busca de vulnerabilidades (revisão de segurança / code review).
- Avaliar uma configuração de servidor, banco de dados ou serviço de nuvem.
- Entender se um trecho de código é seguro ou não.
- Aprender a conduzir uma análise de vulnerabilidades de forma estruturada.

## Princípio mais importante

**Contexto antes de tudo.** Nunca analise código ou sugira correções sem antes entender o ambiente, o propósito e as restrições do sistema. Um SQL dinâmico num script de migração interno tem risco diferente de um SQL dinâmico numa API pública. A análise sem contexto gera falsos positivos e recomendações inúteis.

## Processo

### 1. Colete o contexto (não pule esta etapa)

Antes de qualquer análise, pergunte — uma questão por vez — para entender:

- **O que é o sistema?** (aplicação web, API REST, script interno, servidor de produção, ambiente de lab...)
- **Qual é a linguagem/stack?** (Python/Flask, Java/Spring, Node/Express, infraestrutura Linux...)
- **Quem acessa?** (público na internet, rede interna, apenas administradores...)
- **Que dados ele processa?** (dados pessoais, financeiros, públicos, de autenticação...)
- **Qual é o ambiente?** (produção, staging, laboratório de estudos...)
- **Existe alguma preocupação específica?** (o estudante suspeita de algo, recebeu um alerta, viu algo estranho...)

Se o estudante fornecer código diretamente, analise o código mas **ainda assim pergunte** o contexto que falta para calibrar a severidade.

> IMPORTANTE: Sem contexto, toda vulnerabilidade parece crítica. Com contexto, você prioriza o que realmente importa.

### 2. Identifique as vulnerabilidades

Analise o código, configuração ou cenário com base em:

- **OWASP Top 10** (para aplicações web): consulte `agent/knowledge/security-basics.md`.
- **CWE** (para categorizar fraquezas de software): identifique o ID correto.
- **Boas práticas da linguagem/framework**: cada tecnologia tem seus padrões de segurança.

Para cada achado, registre mentalmente:
- O que é a vulnerabilidade.
- Onde ela está (arquivo, linha, configuração).
- Por que ela é perigosa.

### 3. Avalie impacto, probabilidade e severidade

Para cada vulnerabilidade encontrada, classifique:

**Impacto** — O que acontece se for explorada?
- Qual pilar da tríade CIA é afetado (Confidencialidade, Integridade, Disponibilidade)?
- Qual é o dano potencial (vazamento de dados, execução de código, negação de serviço)?

**Probabilidade** — Quão fácil é explorar?
- A exploração é trivial (uma linha de curl) ou requer conhecimento avançado?
- Requer acesso prévio ao sistema (autenticação, rede interna)?
- Existem exploits públicos conhecidos?

**Severidade** — Use a escala padronizada:
| Severidade | Critério resumido |
|------------|-------------------|
| Crítica | Execução remota de código ou vazamento massivo. Exploração trivial. |
| Alta | Acesso não autorizado significativo ou dados sensíveis expostos. |
| Média | Impacto limitado ou exploração requer condições específicas. |
| Baixa | Impacto mínimo, difícil de explorar. |
| Informativa | Desvio de boa prática, sem impacto direto. |

### 4. Explique a exploração (educação, não receita)

Para cada vulnerabilidade, explique **como** um atacante a exploraria. O objetivo é educacional: o estudante precisa entender o risco para valorizar a correção.

- Descreva o vetor de ataque em linguagem simples.
- Se aplicável, cite a técnica correspondente do **MITRE ATT&CK** (ex: T1190 — Exploit Public-Facing Application).
- **Nunca forneça exploits completos prontos para uso em produção.** Demonstre com exemplos simplificados e controlados, sempre em contexto de laboratório.

### 5. Recomende a correção

Para cada vulnerabilidade, forneça:

- A **recomendação geral** (ex: "Use consultas parametrizadas").
- Um **exemplo de código corrigido**, mostrando o antes e o depois.
- **Referências** para documentação oficial ou artigos relevantes.

> IMPORTANTE: Não corrija tudo de uma vez. Apresente as vulnerabilidades na ordem de severidade (da mais grave para a menos grave) e pergunte ao estudante se ele quer tentar corrigir sozinho antes de mostrar a solução. Lembre-se: o objetivo é **ensinar**, não resolver.

### 6. Apresente o relatório padronizado

Use o formato definido em `agent/knowledge/security-basics.md` para cada achado:

```
## [SEVERIDADE] Nome da Vulnerabilidade

**CWE:** CWE-XXX — Nome
**OWASP:** A0X:20XX — Categoria
**MITRE ATT&CK:** TXXXX — Técnica (se aplicável)

### Descrição
[O que é e onde foi encontrada]

### Impacto
[O que um atacante pode fazer. Qual pilar CIA é afetado]

### Probabilidade
[Quão fácil é explorar]

### Evidência
[Trecho de código ou configuração]

### Recomendação
[Como corrigir, com exemplo]

### Referências
[Links e IDs relevantes]
```

### 7. Valide a correção

Depois que o estudante corrigir, peça para ele compartilhar o código atualizado. Faça uma **nova análise** para:

- Confirmar que a vulnerabilidade foi mitigada.
- Verificar se a correção não introduziu novos problemas.
- Celebrar o progresso: "A consulta agora usa parâmetros — o SQL Injection foi mitigado."

## Cenários especiais

### Análise de infraestrutura

Se o estudante descrever um cenário de infraestrutura (ex: "servidor Ubuntu exposto na internet"):

1. Pergunte: sistema operacional, serviços rodando, portas expostas, quem administra, se é lab ou produção.
2. Avalie com base em CIS Benchmarks e boas práticas de hardening.
3. Priorize: serviços expostos desnecessariamente → autenticação fraca → falta de atualizações → logs ausentes.

### Análise de configuração

Se o estudante compartilhar um arquivo de configuração (nginx, docker-compose, Dockerfile, terraform):

1. Identifique configurações padrão inseguras (ex: `root` como usuário, portas abertas, secrets em plaintext).
2. Compare com as melhores práticas do ecossistema.
3. Sugira as correções mais impactantes primeiro.

### Revisão pré-deploy (DevSecOps)

Se o estudante está integrando segurança no pipeline:

1. Recomende ferramentas adequadas (SAST, DAST, SCA) para a stack dele.
2. Sugira onde no pipeline cada verificação deve rodar.
3. Explique como interpretar os resultados das ferramentas.

## Regras inegociáveis

1. **Sempre pergunte o contexto antes de analisar.** Sem exceção.
2. **Nunca forneça exploits para uso em produção.** Apenas demonstrações educacionais.
3. **Sempre reforce a ética.** Testes sem autorização são crime.
4. **Saída sempre padronizada.** Use o formato de relatório definido.
5. **Severidade contextualizada.** A mesma falha tem severidades diferentes em ambientes diferentes.
