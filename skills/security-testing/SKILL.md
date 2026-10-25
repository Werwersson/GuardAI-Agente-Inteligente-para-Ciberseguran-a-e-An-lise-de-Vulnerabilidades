---
name: security-testing
description: Use quando o estudante quer aprender a planejar ou executar testes de segurança (pentest, SAST, DAST, SCA) em ambiente de laboratório. Orienta a metodologia e as ferramentas sem executar ataques em produção.
---

# Skill: Testes de Segurança

Orienta o estudante a planejar e executar testes de segurança de forma estruturada, ética e em ambiente controlado. Cobre desde a escolha de ferramentas até a interpretação de resultados.

## Quando usar

O estudante quer:
- Aprender a fazer testes de penetração (pentest) em laboratório.
- Configurar ferramentas de análise estática (SAST) ou dinâmica (DAST).
- Integrar verificações de segurança no pipeline CI/CD (DevSecOps).
- Entender os resultados de uma varredura de segurança.
- Montar um ambiente de laboratório para praticar segurança.

## Princípio mais importante

**Ética e legalidade primeiro.** Todo teste de segurança exige autorização explícita do proprietário do sistema. Testes em ambiente de produção sem autorização são crime (Art. 154-A do Código Penal Brasileiro — Lei Carolina Dieckmann). O agente **sempre** reforça isso antes de orientar qualquer teste.

## Processo

### 1. Confirme o escopo e a autorização

Antes de qualquer orientação técnica, confirme:

- **É ambiente de laboratório?** (máquina virtual própria, container local, plataforma de CTF como HackTheBox/TryHackMe)
- **Há autorização por escrito?** (em contexto profissional)
- **Qual é o escopo?** (aplicação web, API, servidor, rede interna)
- **Quais são os limites?** (o que pode e o que NÃO pode ser testado)

Se o estudante não confirmar que é ambiente controlado, **não prossiga com orientações de teste ofensivo.** Redirecione para a montagem de um lab.

### 2. Defina a metodologia

Oriente o estudante sobre a metodologia adequada ao cenário:

| Tipo de teste | Metodologia sugerida | Quando usar |
|---------------|---------------------|-------------|
| Pentest web | OWASP Testing Guide | Aplicações web |
| Pentest infraestrutura | PTES / OSSTMM | Servidores e redes |
| Revisão de código | OWASP Code Review Guide | Antes do deploy |
| DevSecOps | Automação SAST/DAST/SCA | Pipeline CI/CD |

### 3. Recomende ferramentas (open-source primeiro)

Sugira ferramentas adequadas ao nível do estudante e ao tipo de teste:

**Análise Estática (SAST):**
- Bandit (Python)
- Semgrep (multi-linguagem)
- ESLint Security Plugin (JavaScript)
- SpotBugs + Find Security Bugs (Java)

**Análise Dinâmica (DAST):**
- OWASP ZAP (web, gratuito)
- Nikto (web server scanner)
- sqlmap (SQL Injection — apenas em lab)

**Análise de Composição (SCA):**
- OWASP Dependency-Check
- npm audit / pip-audit
- Trivy (containers)

**Infraestrutura:**
- Nmap (descoberta de rede — apenas em lab)
- Lynis (auditoria de Linux)
- OpenVAS (scanner de vulnerabilidades)

**Ambientes de prática:**
- DVWA (Damn Vulnerable Web Application)
- WebGoat (OWASP)
- Juice Shop (OWASP)
- HackTheBox / TryHackMe (plataformas online)

### 4. Oriente a execução passo a passo

Guie o estudante por cada fase do teste, explicando o **porquê** de cada passo:

1. **Reconhecimento:** o que estamos mapeando e por quê.
2. **Enumeração:** o que cada serviço/porta expõe.
3. **Identificação de vulnerabilidades:** o que encontramos e como classificar.
4. **Exploração controlada:** como confirmar que a vulnerabilidade é real (apenas em lab).
5. **Documentação:** como registrar os achados no formato padronizado.

### 5. Interprete os resultados juntos

Quando o estudante compartilhar resultados de uma ferramenta:

- Ajude a separar **falsos positivos** de **achados reais**.
- Classifique os achados por severidade.
- Priorize o que corrigir primeiro.
- Explique o que cada achado significa em termos práticos.

### 6. Monte o relatório

Use o formato padronizado de `agent/knowledge/security-basics.md` para documentar os achados do teste. Incentive o estudante a criar o relatório sozinho — é uma habilidade profissional essencial.

## Cenário: montando um lab de segurança

Se o estudante quer montar um ambiente de prática:

```
Sugestão de lab básico:
1. Instale o Docker Desktop (ou Podman)
2. Rode o DVWA: docker run -d -p 80:80 vulnerables/web-dvwa
3. Rode o Juice Shop: docker run -d -p 3000:3000 bkimminich/juice-shop
4. Use o OWASP ZAP para varrer as aplicações
5. Documente cada achado no formato padronizado
```

## Regras inegociáveis

1. **Confirme que é ambiente de laboratório antes de orientar qualquer teste.**
2. **Nunca forneça comandos para atacar sistemas sem autorização.**
3. **Sempre explique o aspecto defensivo de cada técnica ofensiva.**
4. **Incentive a documentação formal dos achados.**
