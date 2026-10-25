# Fundamentos de Cibersegurança

Este arquivo é a base de conhecimento de segurança do GuardAI Agent. Ele contém os conceitos fundamentais que o agente precisa dominar para conduzir análises de vulnerabilidades e orientar estudantes.

---

## Conceitos Essenciais

### Vulnerabilidade

Uma **vulnerabilidade** é uma fraqueza ou falha em um sistema, aplicação, processo ou controle que pode ser explorada por um agente de ameaça para comprometer a segurança. Exemplos: ausência de validação de entrada, uso de criptografia fraca, permissões excessivas, software desatualizado.

Uma vulnerabilidade por si só não é um incidente — ela se torna um risco quando existe uma ameaça capaz de explorá-la.

### Ameaça

Uma **ameaça** é qualquer circunstância ou evento com potencial de causar dano a um sistema ou organização. As ameaças podem ser:

- **Humanas intencionais:** hackers, insiders maliciosos, grupos APT (Advanced Persistent Threat).
- **Humanas não intencionais:** erros de configuração, engenharia social, negligência.
- **Ambientais:** desastres naturais, falhas de hardware, interrupções de energia.

### Risco

**Risco** é a combinação da probabilidade de uma ameaça explorar uma vulnerabilidade com o impacto que essa exploração causaria:

```
Risco = Probabilidade × Impacto
```

A avaliação de risco é o que permite priorizar correções: nem toda vulnerabilidade merece atenção imediata. A severidade deve considerar o contexto do negócio.

### Exploit

Um **exploit** é um código, técnica ou procedimento que tira proveito de uma vulnerabilidade específica. Um exploit transforma uma fraqueza teórica em um ataque prático. Exemplos: scripts de SQL Injection, payloads de buffer overflow, kits de phishing.

---

## Tríade CIA (Confidencialidade, Integridade e Disponibilidade)

A tríade CIA é o pilar central da segurança da informação. Toda análise de risco deve considerar o impacto em cada um dos três pilares:

### Confidencialidade

Garante que a informação seja acessível **apenas** a quem tem autorização. Violações de confidencialidade incluem:

- Vazamento de dados pessoais (LGPD/GDPR).
- Acesso não autorizado a credenciais ou chaves de API.
- Interceptação de tráfego de rede (sniffing).

**Controles comuns:** criptografia (em trânsito e em repouso), controle de acesso (RBAC), autenticação multifator (MFA), classificação da informação.

### Integridade

Garante que a informação não seja **alterada ou destruída** de forma não autorizada. Violações de integridade incluem:

- Modificação de registros de banco de dados via SQL Injection.
- Alteração de arquivos de configuração por malware.
- Commits maliciosos em repositórios de código.

**Controles comuns:** hashing (SHA-256), assinaturas digitais, controle de versão, checksums, logs de auditoria imutáveis.

### Disponibilidade

Garante que os sistemas e informações estejam **acessíveis quando necessário**. Violações de disponibilidade incluem:

- Ataques DDoS (Distributed Denial of Service).
- Ransomware que cifra e bloqueia acesso a dados.
- Falhas de infraestrutura sem plano de recuperação.

**Controles comuns:** redundância, backups automatizados, balanceamento de carga, plano de recuperação de desastres (DRP), monitoramento contínuo.

---

## OWASP Top 10 (Referência para AppSec)

O OWASP Top 10 é a referência mais conhecida para segurança de aplicações web. O GuardAI deve conhecer cada categoria:

| # | Categoria | Descrição resumida | Exemplo |
|---|-----------|--------------------|---------| 
| A01 | Broken Access Control | Falha na aplicação de permissões. Usuários acessam recursos que não deveriam. | IDOR, escalação de privilégios |
| A02 | Cryptographic Failures | Uso inadequado ou ausência de criptografia para proteger dados sensíveis. | Senhas em texto plano, HTTP sem TLS |
| A03 | Injection | Dados não confiáveis enviados a um interpretador como parte de um comando. | SQL Injection, Command Injection, XSS |
| A04 | Insecure Design | Falhas de arquitetura que não podem ser corrigidas com implementação perfeita. | Ausência de rate limiting, falta de threat modeling |
| A05 | Security Misconfiguration | Configurações padrão inseguras, incompletas ou ad hoc. | Headers de segurança ausentes, diretório listável |
| A06 | Vulnerable and Outdated Components | Uso de bibliotecas, frameworks ou softwares com vulnerabilidades conhecidas. | Log4Shell, dependências sem atualização |
| A07 | Identification and Authentication Failures | Falhas em confirmar a identidade do usuário. | Senhas fracas, falta de MFA, sessões sem expiração |
| A08 | Software and Data Integrity Failures | Falhas em proteger a integridade do código e da infraestrutura. | CI/CD inseguro, dependências não verificadas |
| A09 | Security Logging and Monitoring Failures | Falta de logs e monitoramento para detectar atividades maliciosas. | Ausência de alertas, logs sem proteção |
| A10 | Server-Side Request Forgery (SSRF) | A aplicação busca um recurso remoto sem validar a URL fornecida pelo usuário. | Acesso a metadados de cloud via SSRF |

---

## MITRE ATT&CK (Referência para Táticas e Técnicas)

O MITRE ATT&CK é um framework que cataloga táticas e técnicas reais usadas por adversários. O GuardAI deve referenciá-lo ao explicar como um ataque funciona.

### Estrutura

- **Tática:** o *objetivo* do adversário (ex: Initial Access, Execution, Persistence, Lateral Movement).
- **Técnica:** o *como* o adversário alcança a tática (ex: T1190 — Exploit Public-Facing Application).
- **Sub-técnica:** variação específica de uma técnica (ex: T1059.001 — PowerShell).

### Táticas principais

| ID | Tática | Descrição |
|----|--------|-----------|
| TA0001 | Initial Access | Como o adversário entra na rede ou sistema |
| TA0002 | Execution | Como o adversário roda código malicioso |
| TA0003 | Persistence | Como o adversário mantém acesso após reinício |
| TA0004 | Privilege Escalation | Como o adversário obtém permissões mais altas |
| TA0005 | Defense Evasion | Como o adversário evita detecção |
| TA0006 | Credential Access | Como o adversário rouba credenciais |
| TA0007 | Discovery | Como o adversário mapeia o ambiente |
| TA0008 | Lateral Movement | Como o adversário se move pela rede |
| TA0009 | Collection | Como o adversário coleta dados de interesse |
| TA0010 | Exfiltration | Como o adversário extrai dados do ambiente |
| TA0011 | Command and Control | Como o adversário controla sistemas comprometidos |
| TA0040 | Impact | Como o adversário causa dano (destruição, ransomware) |

---

## NIST Cybersecurity Framework (CSF)

O NIST CSF organiza a segurança em 5 funções:

1. **Identify (Identificar):** conhecer os ativos, dados e riscos da organização.
2. **Protect (Proteger):** implementar salvaguardas para garantir a entrega de serviços.
3. **Detect (Detectar):** monitorar e identificar a ocorrência de eventos de segurança.
4. **Respond (Responder):** tomar ação frente a um incidente de segurança detectado.
5. **Recover (Recuperar):** restaurar capacidades e serviços afetados por um incidente.

---

## CWE — Common Weakness Enumeration

CWEs são identificadores padronizados para tipos de fraquezas de software. O GuardAI deve referenciá-los nas análises:

| CWE | Nome | Descrição |
|-----|------|-----------|
| CWE-89 | SQL Injection | Neutralização imprópria de elementos especiais em comandos SQL |
| CWE-79 | Cross-site Scripting (XSS) | Neutralização imprópria de entrada em páginas web |
| CWE-78 | OS Command Injection | Neutralização imprópria de elementos especiais em comandos do SO |
| CWE-22 | Path Traversal | Limitação imprópria de nome de caminho a um diretório restrito |
| CWE-287 | Improper Authentication | Verificação imprópria de autenticação |
| CWE-862 | Missing Authorization | Verificação de autorização ausente |
| CWE-200 | Information Exposure | Exposição de informações sensíveis |
| CWE-502 | Deserialization of Untrusted Data | Deserialização de dados não confiáveis |
| CWE-918 | Server-Side Request Forgery | Falsificação de requisição do lado do servidor |
| CWE-306 | Missing Authentication for Critical Function | Ausência de autenticação para função crítica |

---

## Boas Práticas Defensivas

### Desenvolvimento Seguro (AppSec)

1. **Validação de entrada:** toda entrada do usuário é potencialmente maliciosa. Valide tipo, formato, tamanho e conteúdo. Prefira listas de permissão (allowlist) a listas de bloqueio (blocklist).
2. **Consultas parametrizadas:** nunca construa SQL concatenando strings. Use prepared statements ou ORM com binding de parâmetros.
3. **Sanitização de saída:** encode a saída conforme o contexto (HTML, URL, JavaScript, CSS) para prevenir XSS.
4. **Princípio do menor privilégio:** cada componente deve ter apenas as permissões estritamente necessárias.
5. **Gerenciamento de segredos:** nunca hardcode senhas, chaves de API ou tokens no código. Use variáveis de ambiente ou cofres de segredos (Vault, AWS Secrets Manager).
6. **Dependências atualizadas:** monitore e atualize bibliotecas regularmente. Use ferramentas de SCA (Software Composition Analysis).
7. **Headers de segurança:** configure Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, Strict-Transport-Security.
8. **Tratamento de erros seguro:** nunca exponha stack traces, queries SQL ou caminhos internos em mensagens de erro para o usuário.

### Infraestrutura Segura

1. **Hardening:** remova serviços desnecessários, desabilite contas padrão, aplique patches de segurança regularmente.
2. **Firewall e segmentação:** segmente redes para limitar o impacto de uma invasão (microsegmentação).
3. **Autenticação forte:** implemente MFA para todos os acessos administrativos.
4. **Logs e monitoramento:** centralize logs (SIEM), configure alertas para atividades suspeitas, mantenha logs por tempo suficiente para investigação.
5. **Backup e recuperação:** faça backups regulares, teste a restauração, mantenha cópias off-site.
6. **Atualizações automáticas:** automatize a aplicação de patches quando possível. Para sistemas críticos, teste antes em staging.

### DevSecOps

1. **Shift-left:** integre segurança desde o início do ciclo de desenvolvimento, não apenas antes do deploy.
2. **SAST no CI/CD:** rode análise estática de código em cada pull request.
3. **DAST no staging:** rode varreduras dinâmicas automatizadas contra o ambiente de staging.
4. **SCA contínua:** monitore dependências automaticamente para novas CVEs.
5. **Infrastructure as Code (IaC) scanning:** valide templates Terraform, CloudFormation, Kubernetes para configurações inseguras.
6. **Secret scanning:** bloqueie commits que contenham credenciais ou chaves.

---

## Modelo de Classificação de Severidade

O GuardAI usa uma escala de 5 níveis para classificar achados de segurança:

| Severidade | Critério | Ação esperada |
|------------|----------|---------------|
| **Crítica** | Permite execução remota de código, acesso total ao sistema ou vazamento massivo de dados. Exploração trivial. | Correção imediata. Parar o deploy se necessário. |
| **Alta** | Permite acesso não autorizado significativo, escalação de privilégios ou vazamento de dados sensíveis. | Correção na próxima sprint ou em até 7 dias. |
| **Média** | Permite acesso limitado ou vazamento de informações de baixo impacto. Requer condições específicas para exploração. | Correção planejada em até 30 dias. |
| **Baixa** | Impacto mínimo. Difícil de explorar ou requer acesso prévio ao sistema. | Correção conforme disponibilidade. |
| **Informativa** | Observação de melhoria ou desvio de boa prática, sem impacto direto de segurança. | Considerar em futuras melhorias. |

---

## Formato Padronizado de Relatório

Toda análise de vulnerabilidade deve seguir este formato:

```
## [SEVERIDADE] Nome da Vulnerabilidade

**CWE:** CWE-XXX — Nome
**OWASP:** A0X:20XX — Categoria
**MITRE ATT&CK:** TXXXX — Técnica

### Descrição
O que é a vulnerabilidade e onde ela foi encontrada.

### Impacto
O que um atacante pode fazer se explorar esta vulnerabilidade.
Qual pilar da tríade CIA é afetado.

### Probabilidade
Quão fácil é explorar (trivial, moderada, difícil).
Requer acesso prévio? Requer interação do usuário?

### Evidência
Trecho de código, configuração ou log que demonstra a vulnerabilidade.

### Recomendação
Como corrigir, com exemplo de código ou configuração segura.

### Referências
Links para documentação oficial, artigos ou CWE/CVE relevantes.
```
