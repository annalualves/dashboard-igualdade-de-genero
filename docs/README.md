# Projeto: Dashboard de Combate à Violência contra a Mulher

Dashboard para analisar o objetivo 5 de desenvolvimento sustentável no Brasil - Igualdade de Gênero com foco em violência contra a mulher.

## I. Objetivo
O objetivo deste projeto é criar um dashboard interativo para monitorar, analisar e visualizar dados sobre a violência contra a mulher no Brasil. A solução busca consolidar informações de fontes diversas e torná-las acessíveis de forma clara e visual. Isso permitirá que pesquisadores, estudantes, ativistas, jornalistas e formuladores de políticas públicas tenham uma ferramenta poderosa para entender as tendências, identificar padrões e, assim, apoiar a elaboração de estratégias mais eficazes de combate a esse problema social.

A aplicação aborda diretamente o **Objetivo de Desenvolvimento Sustentável (ODS) 5 - Igualdade de Gênero**, com foco na meta 5.2, que visa eliminar todas as formas de violência contra mulheres e meninas.

## II. Problema
Apesar da gravidade da violência contra a mulher no Brasil, os dados sobre o tema muitas vezes estão dispersos em relatórios, sites governamentais e bases de dados complexas, dificultando a análise integrada. Essa falta de uma plataforma centralizada e visualmente clara impede que a sociedade e os órgãos competentes compreendam a dimensão do problema, como sua distribuição geográfica e a evolução ao longo do tempo.

O problema principal, portanto, é a dispersão e a inacessibilidade dos dados, o que prejudica a conscientização, a pesquisa e a tomada de decisões baseadas em evidências para combater a violência de gênero de forma eficaz.

## III. Tipo de Solução
A solução proposta é um dashboard de dados, uma aplicação web que combina um backend e um frontend.

* **Frontend:** Interface do usuário, responsável por exibir os gráficos e métricas de forma interativa.
* **Backend:** O "motor" da aplicação, responsável por coletar, processar e servir os dados para o frontend através de uma API.

A escolha de um dashboard é a mais adequada porque a solução lida com um grande volume de dados estatísticos. O formato visual do dashboard é ideal para:
* **Síntese de Dados:** Transformar informações complexas em gráficos de fácil compreensão.
* **Análise Rápida:** Permitir que o usuário identifique rapidamente tendências, picos de violência e áreas de maior incidência.
* **Comunicação Efetiva:** Facilitar a comunicação do problema para um público amplo, que pode não ter familiaridade com a análise de dados brutos.

## IV. Requisitos Funcionais (RFs) Implementados

* **RF01: Visualização de Incidência por Estado**
    O sistema exibe um gráfico de barras vertical comparativo, permitindo visualizar o volume de casos por estado de forma ordenada.

* **RF02: Gráficos de Tipologia**
    O sistema apresenta gráficos de pizza para detalhar a proporção dos tipos de violência mais comuns (física, psicológica, sexual, etc.).

* **RF03: Análise de Tendência**
    O sistema inclui um gráfico de linhas para mostrar a evolução temporal dos casos de violência ao longo dos anos.

* **RF04: Filtros de Dados**
    O sistema permite que o usuário filtre todos os gráficos e métricas dinamicamente por **Ano**, recalculando as informações em tempo real.

* **RF05: Métricas Chave (KPIs)**
    O sistema exibe cartões com métricas de destaque no topo, como o total de casos registrados e a média de idade das vítimas.

## V. Diagrama de Caso de Uso
O diagrama de caso de uso a seguir ilustra as principais interações dos atores com o sistema.

![Diagrama de Caso de Uso](docs/diagrama_caso_de_uso.png)

Atores:
* **Usuário:** Qualquer pessoa que acessa o dashboard para visualizar dados.
* **Administrador:** Pessoa responsável por carregar e atualizar os dados no sistema.

---

## VI. Tecnologias Utilizadas

Para o desenvolvimento deste projeto, foram utilizadas as seguintes tecnologias:

* **Frontend:**
    * **React.js:** Biblioteca principal para construção da interface.
    * **Recharts:** Biblioteca para criação dos gráficos responsivos.
    * **Axios:** Cliente HTTP para comunicação com o Backend.
* **Backend:**
    * **Python & Flask:** Framework para criação da API RESTful.
    * **Flask-SQLAlchemy:** ORM para gerenciamento do banco de dados.
    * **Flask-CORS:** Para permissão de acesso entre Frontend e Backend.
* **Banco de Dados:**
    * **SQLite:** Banco de dados relacional (arquivo `violencia.db`) para armazenamento dos casos.

## VII. Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação em seu ambiente local.

### Pré-requisitos
* Node.js e npm instalados.
* Python instalado.

### Passo 1: Configurar e Rodar o Backend
1.  Abra o terminal e entre na pasta do backend:
    ```bash
    cd backend
    ```
2.  Instale as dependências necessárias:
    ```bash
    pip install Flask Flask-CORS Flask-SQLAlchemy
    ```
3.  (Opcional) Se o arquivo `instance/violencia.db` não existir, popule o banco:
    ```bash
    python seed.py
    ```
4.  Inicie o servidor:
    ```bash
    python app.py
    ```
    *O servidor rodará em `http://localhost:5000`.*

### Passo 2: Configurar e Rodar o Frontend
1.  Abra um **novo terminal** e entre na pasta do frontend:
    ```bash
    cd frontend
    ```
2.  Instale as dependências do projeto:
    ```bash
    npm install
    ```
3.  Inicie a aplicação:
    ```bash
    npm start
    ```
    *O dashboard abrirá automaticamente em `http://localhost:3000`.*

## VIII. Estrutura do Repositório

* `/backend`: Código fonte da API, modelo de dados e scripts de banco.
* `/frontend`: Código fonte da interface React e componentes visuais.
* `/docs`: Documentação do projeto (Plano de Testes e Diagramas).
* `/Videos`: Vídeos de apresentação das entregas (Sprints).