# Plano de Testes: Dashboard de Combate à Violência contra a Mulher

Este documento descreve os casos de teste para validar os Requisitos Funcionais (RFs) da aplicação.

---

### RF01: Dashboard de Incidência (Mapa)

| ID     | Descrição                                 | Passos para Execução                                | Resultado Esperado                                                              |
| :----- | :---------------------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------------ |
| CT01.1 | Visualizar o mapa do Brasil.              | 1. Abrir a página principal do dashboard.           | O componente do mapa deve ser renderizado, mostrando o contorno dos estados.    |
| CT01.2 | Verificar o mapa de calor (Choropleth).   | 1. Abrir a página.<br>2. Observar o mapa.           | Os estados devem estar coloridos com intensidades diferentes (ex: SP mais escuro). |
| CT01.3 | Verificar tooltip (mouse-over) no estado. | 1. Abrir a página.<br>2. Passar o mouse sobre um estado (ex: "MG"). | Um tooltip deve aparecer mostrando o nome do estado e o número de casos.         |

### RF02: Gráficos de Tipologia (Pizza/Barra)

| ID     | Descrição                                 | Passos para Execução                                      | Resultado Esperado                                                                |
| :----- | :---------------------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| CT02.1 | Visualizar o gráfico de tipologia.        | 1. Abrir a página principal.                              | O gráfico de pizza (ou barras) deve ser renderizado com as diferentes categorias. |
| CT02.2 | Verificar legendas e dados.               | 1. Observar o gráfico.<br>2. Comparar com os dados mockados. | As legendas ("Física", "Psicológica", etc.) e as porcentagens estão corretas.    |
| CT02.3 | Verificar tooltip (mouse-over) na fatia.  | 1. Passar o mouse sobre uma fatia (ex: "Física").         | Um tooltip deve aparecer mostrando o nome da categoria e o valor exato de casos.  |

### RF03: Análise de Tendência (Gráfico de Linha)

| ID     | Descrição                                    | Passos para Execução                                      | Resultado Esperado                                                                    |
| :----- | :------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| CT03.1 | Visualizar o gráfico de tendência temporal.  | 1. Abrir a página principal.                              | Um gráfico de linha deve ser renderizado.                                             |
| CT03.2 | Verificar eixos do gráfico.                  | 1. Observar o gráfico.                                    | O eixo X (horizontal) deve mostrar os anos (ex: 2020, 2021, 2022). O eixo Y (vertical) deve mostrar o número de casos. |
| CT03.3 | Verificar tooltip (mouse-over) nos pontos.   | 1. Passar o mouse sobre um ponto da linha.                | Um tooltip deve aparecer mostrando o ano específico e o número de casos daquele ano. |

### RF04: Filtros de Dados

| ID     | Descrição                                    | Passos para Execução                                      | Resultado Esperado                                                                    |
| :----- | :------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| CT04.1 | Visualizar os componentes de filtro.         | 1. Abrir a página.                                        | Os campos de filtro (ex: Dropdown "Ano", Dropdown "Tipo de Violência") devem estar visíveis. |
| CT04.2 | Aplicar um filtro de Ano.                    | 1. Selecionar um ano (ex: "2022") no filtro.<br>2. Clicar em "Aplicar". | Todos os gráficos (Mapa, Tipologia, Tendência) e Métricas devem atualizar para mostrar apenas os dados de 2022. |
| CT04.3 | Limpar filtros.                              | 1. Aplicar um filtro.<br>2. Clicar no botão "Limpar Filtros". | Todos os gráficos e métricas devem retornar ao estado inicial (mostrando todos os dados). |

### RF05: Métricas Chave (Cartões)

| ID     | Descrição                                 | Passos para Execução                                      | Resultado Esperado                                                              |
| :----- | :---------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------ |
| CT05.1 | Visualizar os cartões de métricas.        | 1. Abrir a página.                                        | Os três cartões (Total de Casos, Crescimento, Média de Idade) devem ser exibidos. |
| CT05.2 | Verificar carregamento dos dados.         | 1. Abrir a página e aguardar o carregamento.              | Os cartões devem exibir os números vindos da API (ex: "120.500") e não "..." ou "0". |
| CT05.3 | Verificar formatação dos números.         | 1. Observar os cartões.                                   | Os números devem estar formatados corretamente (ex: `120.500` com ponto, `15.2%` com símbolo de porcentagem). |