# Documentação de Arquitetura: Dashboard de Combate à Violência contra a Mulher

Este documento descreve a arquitetura de software para o projeto, utilizando o C4 Model para visualização.

## 1. Escolhas de Tecnologias

Para entregar um dashboard interativo (RFs) de forma rápida e eficiente, selecionamos as seguintes tecnologias:

* **Frontend (Contêiner "Web App"):**
    * **Framework:** React.js
    * **Justificativa:** É a biblioteca líder de mercado para SPAs (Single Page Applications), baseada em componentes reutilizáveis.
    * **Bibliotecas-Chave:** `Recharts` (para gráficos) e `Axios` (para comunicação HTTP).

* **Backend (Contêiner "API"):**
    * **Linguagem/Framework:** Python com Flask
    * **Justificativa:** Flask é um micro-framework leve, ideal para criar APIs RESTful rapidamente. Python facilita a manipulação de dados.
    * **Bibliotecas-Chave:** `Flask`, `Flask-CORS`, `Flask-SQLAlchemy`.

* **Banco de Dados (Contêiner "Database"):**
    * **Sistema:** SQLite
    * **Justificativa:** Optamos pelo SQLite por ser um banco de dados relacional "serverless" (baseado em arquivo). Para o escopo deste projeto acadêmico, ele oferece persistência de dados real sem a complexidade de configurar um servidor PostgreSQL dedicado, facilitando a portabilidade do projeto (o banco vai junto com o código).

## 2. Projeto Arquitetural (C4 Model)

### Nível 1: Diagrama de Contexto
*(Mantém o diagrama anterior)*

### Nível 2: Diagrama de Contêineres

O sistema é composto por 3 contêineres principais:

1.  **Frontend (Web Application):**
    * Tecnologia: React.js
    * Responsabilidade: Interface do usuário, renderização de gráficos e filtros.

2.  **Backend (API REST):**
    * Tecnologia: Python (Flask)
    * Responsabilidade: Servir os dados para o frontend e realizar consultas ao banco via SQLAlchemy.

3.  **Banco de Dados (Database):**
    * Tecnologia: SQLite (Arquivo `violencia.db`)
    * Responsabilidade: Armazenar os dados de ocorrências, estados e tipos de violência de forma persistente no disco local.

## 3. Justificativa do Modelo

A arquitetura de Contêineres (Frontend SPA + Backend API + DB) foi mantida conforme o plano original, garantindo o desacoplamento. A substituição do PostgreSQL pelo SQLite na camada de dados foi uma decisão estratégica para agilizar o desenvolvimento e a configuração do ambiente de testes, mantendo todas as características de um banco relacional (SQL) necessárias para o projeto.