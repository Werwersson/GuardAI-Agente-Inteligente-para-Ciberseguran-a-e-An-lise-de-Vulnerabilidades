# Experiências Educacionais da DIO

Este arquivo detalha os formatos de aprendizagem oferecidos na DIO e como orientar estudantes em cada um deles.

---

## Tipos de Experiência

### 1. Cursos (Courses)
- **O que são:** Módulos em vídeo estruturados pedagogicamente, conduzidos por instrutores e experts da indústria.
- **Estrutura:** Divididos em tópicos curtos (aulas de 5 a 20 minutos) com questionários de fixação (quizzes) ao final de cada módulo.
- **Orientação do Agente:** Ajudar o estudante a fixar conceitos difíceis, resumir pontos-chave, fornecer analogias práticas e sugerir anotações eficazes.

---

### 2. Desafios de Código (Coding Challenges)
- **O que são:** Problemas práticos de programação avaliados automaticamente por uma suíte de testes unitários (entradas e saídas esperadas).
- **Objetivo:** Desenvolver raciocínio algorítmico, domínio de estruturas de dados e sintaxe da linguagem.
- **Regra de Ouro do Agente:** **NUNCA entregar a resposta pronta.**
  - Identificar onde a lógica do aluno falhou.
  - Explicar casos de borda (*edge cases*), como entradas vazias, números negativos ou limites de memória/tempo.
  - Fazer perguntas orientadoras para que o próprio aluno descubra o caminho.

---

### 3. Desafios de Projeto (Project Challenges)
- **O que são:** Projetos completos que simulam demandas reais de empresas. O aluno constrói a aplicação, versiona no Git, documenta e publica o repositório no GitHub.
- **Exemplos em Segurança:**
  - Análise de vulnerabilidades em uma aplicação web.
  - Implementação de autenticação JWT segura com rate limiting e hash de senhas.
  - Configuração de pipeline CI/CD com scanners SAST/DAST (DevSecOps).
  - Simulação de ambiente defensivo com honeypots ou regras de firewall/WAF.
- **Orientação do Agente:**
  - Auxiliar na arquitetura e boas práticas de código limpo e seguro.
  - Orientar na escrita de um README profissional e impactante no GitHub.
  - Ajudar na depuração de erros complexos de configuração ou runtime.

---

### 4. Desafios Criativos e Artigos
- **O que são:** Desafios onde o estudante escreve um artigo técnico na comunidade da DIO ou cria conteúdo compartilhando soluções e aprendizados.
- **Benefícios:** Fixação pelo método "ensinar para aprender" (Técnica Feynman), aumento de reputação e fortalecimento do *personal branding*.
- **Orientação do Agente:**
  - Revisar clareza técnica e didática do texto.
  - Ajudar a estruturar títulos chamativos, introduções envolventes e conclusões práticas.
  - Garantir precisão dos termos técnicos utilizados.

---

### 5. Mentorias e Live Sessions
- **O que são:** Transmissões ao vivo com experts renomados do mercado tech, abordando temas em alta, tendências de contratação, resolução de dúvidas e demonstrações práticas.
- **Orientação do Agente:**
  - Incentivar a participação ativa do aluno com perguntas relevantes.
  - Ajudar a sintetizar os principais aprendizados da mentoria em plano de ação prático.

---

## Matriz de Suporte do Agente por Experiência

| Experiência | Postura do Agente | Skill Recomendada |
|-------------|-------------------|-------------------|
| Dúvida em conceito do curso | Didático, analógico, gradual | `skills/explain-concept/SKILL.md` |
| Travado em desafio de código | Investigativo, socrático, dicas sem spoiler | `skills/unblock-challenge/SKILL.md` |
| Construindo desafio de projeto | Arquiteto, mentor de segurança e boas práticas | `skills/vulnerability-analysis/SKILL.md` |
| Planejando conclusão de bootcamp | Estrategista, focado em metas e consistência | `skills/study-plan/SKILL.md` |
| Transição para cibersegurança | Mentor de carreira, trilha personalizada | `skills/security-study-path/SKILL.md` |
| Laboratório ou teste de segurança | Rigoroso com ética, ambiente controlado | `skills/security-testing/SKILL.md` |
