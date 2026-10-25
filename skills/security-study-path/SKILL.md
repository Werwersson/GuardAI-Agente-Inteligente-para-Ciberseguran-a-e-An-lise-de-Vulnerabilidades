---
name: security-study-path
description: Use quando o estudante quer montar um plano de estudos para entrar ou evoluir na área de cibersegurança. Cria uma trilha personalizada com base no nível atual, objetivo de carreira e tempo disponível.
---

# Skill: Trilha de Estudos em Cibersegurança

Ajuda o estudante a construir um plano de estudos personalizado para a carreira em cibersegurança, com base no seu nível, objetivos e disponibilidade.

## Quando usar

O estudante quer:
- Entrar na área de cibersegurança e não sabe por onde começar.
- Evoluir de uma área adjacente (desenvolvimento, infraestrutura, redes) para segurança.
- Se preparar para certificações de segurança (CompTIA Security+, CEH, OSCP, etc.).
- Montar um roteiro de estudos estruturado.

## Princípio mais importante

**Personalização com base em contexto real.** Não existe trilha única para todos. Um desenvolvedor que quer migrar para AppSec tem um caminho diferente de alguém que quer ser pentester ou analista de SOC. Pergunte antes de montar.

## Processo

### 1. Entenda o perfil e o objetivo

Pergunte, uma questão por vez:

- **Qual é o seu objetivo na área de segurança?** (primeiro emprego, transição de carreira, promoção interna, certificação específica)
- **Qual é o seu nível atual?** (nunca estudou segurança, sabe o básico, já trabalha na área)
- **De onde você vem?** (desenvolvimento, infraestrutura, redes, suporte, nenhuma experiência em TI)
- **Quanto tempo por semana você pode dedicar?** E por quanto tempo (meses)?
- **Tem alguma certificação ou formação relevante?** (graduação em TI, cursos anteriores, certificações de outras áreas)

### 2. Mapeie os domínios de conhecimento

Com base no objetivo, identifique quais domínios o estudante precisa dominar:

| Perfil desejado | Domínios prioritários |
|-----------------|----------------------|
| Analista de SOC | Redes, monitoramento, SIEM, resposta a incidentes, logs |
| Pentester | Redes, sistemas operacionais, web, scripting, metodologias de teste |
| AppSec Engineer | Desenvolvimento seguro, OWASP, SAST/DAST, DevSecOps |
| Engenheiro de Segurança | Infraestrutura, cloud, IaC, hardening, automação |
| GRC / Compliance | Frameworks (NIST, ISO 27001, LGPD), gestão de riscos, políticas |

### 3. Construa a trilha em fases

Organize o plano em fases progressivas. Cada fase deve ter:

- **Objetivo claro:** o que o estudante saberá fazer ao final.
- **Tópicos:** lista dos assuntos, na ordem certa.
- **Recursos:** cursos da DIO (se houver), livros, plataformas de prática, labs.
- **Prazo estimado:** com base na disponibilidade informada.
- **Marco de validação:** como o estudante saberá que concluiu a fase (lab resolvido, CTF completo, certificação obtida).

**Modelo de trilha em 4 fases:**

```
Fase 1 — Fundamentos (semanas 1-4)
  Objetivo: entender os conceitos base de segurança
  Tópicos: Tríade CIA, tipos de ameaças, redes básicas (TCP/IP, DNS, HTTP),
           Linux básico, criptografia essencial
  Prática: TryHackMe - Pre Security Path
  Marco: completar o módulo + explicar a tríade CIA com exemplos

Fase 2 — Especialização inicial (semanas 5-12)
  [Depende do perfil escolhido]

Fase 3 — Prática intensiva (semanas 13-20)
  [Labs, CTFs, projetos práticos]

Fase 4 — Certificação / portfólio (semanas 21-26)
  [Preparação para certificação ou montagem de portfólio]
```

### 4. Sugira recursos concretos

Para cada fase, recomende:

**Plataformas de prática (gratuitas):**
- TryHackMe (caminhos estruturados por nível)
- HackTheBox Academy (conteúdo didático + labs)
- OverTheWire (wargames para iniciantes — Bandit, Natas)
- PicoCTF (CTF para iniciantes)
- CyberDefenders (blue team — análise de incidentes)

**Certificações por nível:**
| Nível | Certificação | Foco |
|-------|-------------|------|
| Iniciante | CompTIA Security+ | Fundamentos amplos |
| Intermediário | CompTIA CySA+ | Blue team / análise |
| Intermediário | eJPT (INE) | Pentest prático |
| Avançado | OSCP (OffSec) | Pentest avançado |
| Avançado | CISSP (ISC²) | Gestão de segurança |

**Ferramentas para dominar (conforme o perfil):**
- Wireshark, Nmap, Burp Suite, OWASP ZAP, Metasploit (em lab)
- Splunk / ELK Stack (SOC)
- Semgrep / Bandit (AppSec)

### 5. Acompanhe e ajuste

Depois de montar o plano:

- Pergunte se o ritmo parece realista.
- Ofereça para ajustar se o estudante avançar mais rápido ou mais devagar.
- Sugira checkpoints regulares (ex: a cada 2 semanas, revisar o progresso).

## Regras

1. **Sempre pergunte o perfil antes de sugerir um caminho.** Não existe trilha genérica boa.
2. **Priorize prática sobre teoria.** Segurança se aprende fazendo. Labs e CTFs são mais valiosos que vídeos passivos.
3. **Seja realista com prazos.** Não prometa "se torne pentester em 30 dias". Segurança é uma jornada.
4. **Conecte com a DIO quando possível.** Se houver Bootcamps, Formações ou cursos na DIO sobre o tema, recomende.
5. **Celebre cada marco.** Cada fase concluída é uma conquista.
