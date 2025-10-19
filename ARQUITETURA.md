# Documentação de Arquitetura: Dashboard de Combate à Violência contra a Mulher

Este documento descreve a arquitetura de software para o projeto, utilizando o C4 Model para visualização.

## 1. Escolhas de Tecnologias

Para entregar um dashboard interativo (RFs) de forma rápida e eficiente, selecionamos as seguintes tecnologias:

* **Frontend (Contêiner "Web App"):**
    * **Framework:** React.js
    * **Justificativa:** É a biblioteca líder de mercado para SPAs (Single Page Applications), com vasta documentação e ecossistema (ex: `create-react-app` para setup rápido). É baseada em componentes, o que facilita a criação de elementos reutilizáveis (gráficos, cartões, filtros).
    * **Bibliotecas-Chave:** `Recharts` (para gráficos - RF02, RF03) e `Axios` (para consumir a API).

* **Backend (Contêiner "API"):**
    * **Linguagem/Framework:** Python com Flask (ou FastAPI)
    * **Justificativa:** Python é a linguagem padrão para análise de dados. Embora o backend "apenas" sirva os dados, é provável que um pré-processamento (ETL) seja necessário. Flask é um micro-framework leve, ideal para criar APIs RESTful rapidamente.
    * **Bibliotecas-Chave:** `Flask`, `Flask-CORS` (para permitir a comunicação com o React) e `Pandas` (para carregar e processar dados de fontes como CSVs).

* **Banco de Dados (Contêiner "Database"):**
    * **Sistema:** PostgreSQL
    * **Justificativa:** Um banco de dados relacional robusto e gratuito. É ideal para armazenar os dados estruturados de violência (ocorrências, datas, tipos, localizações) e realizar consultas agregadas que alimentarão a API.
    * **Alternativa Rápida (para TP3):** Para o primeiro entregável, podemos simular o banco de dados lendo arquivos CSV estáticos diretamente pelo Backend (com Pandas) para acelerar o desenvolvimento.

## 2. Projeto Arquitetural (C4 Model)

### Nível 1: Diagrama de Contexto

O Diagrama de Contexto mostra o sistema como uma "caixa preta" e suas interações com usuários e outros sistemas.

* **Usuários:**
    * **Pesquisador/Ativista/Gestor Público (Persona):** Acessa o dashboard para analisar dados e tendências.
* **Sistema (Nosso):**
    * **Dashboard de Violência (Software System):** A plataforma web que consolida e exibe os dados.
* **Sistemas Externos (Fontes de Dados):**
    * **SINESP (Sistema Nacional de Informações de Segurança Pública):** Fonte de dados de ocorrências.
    * **IBGE:** Fonte de dados demográficos para cruzamento.
    * *(Outras fontes que você for usar)*

*(**Sua Ação:** Crie um diagrama simples no draw.io mostrando [Usuário] -> [Dashboard] <- [Fontes de Dados] e salve-o como `c4-contexto.png` no seu repositório, linkando aqui).*

### Nível 2: Diagrama de Contêineres

O Diagrama de Contêineres detalha a arquitetura *dentro* do nosso sistema.

Nosso sistema é composto por 3 contêineres principais:

1.  **Frontend (Web Application):**
    * Tecnologia: React.js
    * Responsabilidade: Interface do usuário, renderização de gráficos (RF01-RF05) e filtros. É o que o usuário vê no navegador.

2.  **Backend (API REST):**
    * Tecnologia: Python (Flask)
    * Responsabilidade: Servir os dados para o frontend. Ele busca os dados no Banco de Dados, processa (agrega, calcula) e os expõe em endpoints (ex: `/api/total_casos`, `/api/casos_por_tipo`).

3.  **Banco de Dados (Database):**
    * Tecnologia: PostgreSQL
    * Responsabilidade: Armazenar os dados brutos ou pré-processados de forma persistente.

**Fluxo de Dados (Exemplo RF05):**
1.  Usuário abre o site.
2.  O **Frontend (React)** faz uma requisição `GET` para `api/metricas_chave`.
3.  O **Backend (API)** recebe a requisição, faz uma consulta `SQL` ao **Banco de Dados** (ex: `SELECT COUNT(*) FROM casos WHERE ano = 2023`).
4.  O **Banco de Dados** retorna o número.
5.  O **Backend** formata como JSON (ex: `{"total_casos_2023": 15000}`) e envia ao Frontend.
6.  O **Frontend** exibe o número no "Cartão de Métrica".

*(**Sua Ação:** Crie um diagrama no draw.io mostrando [Frontend] <-> [Backend] <-> [Banco de Dados] e salve como `c4-containers.png`, linkando aqui).*

## 3. Justificativa do Modelo

A arquitetura de Contêineres (Frontend SPA + Backend API + DB) foi escolhida por ser:
* **Desacoplada:** Podemos atualizar o frontend (layout, gráficos) sem mexer no backend, e vice-versa.
* **Escalável:** Se a aplicação crescer, podemos escalar o backend e o banco de dados independentemente.
* **Clara:** Separa as responsabilidades: o React cuida da *visualização*, o Python/Flask cuida da *regra de negócio/dados* e o PostgreSQL da *persistência*.
