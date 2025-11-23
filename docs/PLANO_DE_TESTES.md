# Plano de Testes: Dashboard de Combate à Violência contra a Mulher

Este documento descreve os casos de teste para validar os Requisitos Funcionais (RFs) da aplicação.

---

### RF01: Dashboard de Incidência (Gráfico de Barras por Estado)

| ID     | Descrição                                         | Passos para Execução                                      | Resultado Esperado                                                                    |
| :----- | :------------------------------------------------ | :-------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| CT01.1 | Visualizar o gráfico de barras de incidência por estado. | 1. Abrir a página principal do dashboard.                 | O componente do gráfico de barras deve ser renderizado, mostrando os estados no eixo X e o número de casos no eixo Y. |
| CT01.2 | Verificar os dados e ordenação.                   | 1. Observar o gráfico.<br>2. Verificar se os estados estão ordenados (ex: do maior para o menor número de casos). | As barras devem representar corretamente o volume de casos por estado, e a ordenação deve ser visível. |
| CT01.3 | Verificar tooltip (mouse-over) na barra.          | 1. Passar o mouse sobre uma barra (ex: "SP").             | Um tooltip deve aparecer mostrando a sigla do estado e o número exato de casos.         |

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

### Resultados da Execução dos Testes (Sprint TP5)

| ID TC  | Data Execução | Status   | Observação |
| :----- | :------------ | :------- | :--------- |
| CT01.1 | 15/11/2025    | Aprovado | Gráfico de barras carregou corretamente com dados do SQLite. |
| CT02.1 | 15/11/2025    | Aprovado | Tipologia exibida corretamente. |
| CT04.2 | 15/11/2025    | Aprovado | **Teste de Filtro:** Ao selecionar "2022", o total de casos mudou para 34.000. Ao selecionar "2023", mudou para 40.500. Validado. |
| CT05.1 | 15/11/2025    | Aprovado | Cards exibidos com sucesso. |


---

## 3. Validação Final (Entrega TP6)

Execução completa de todos os fluxos com a aplicação integrada ao Banco de Dados SQLite.

| ID TC  | Data Execução | Responsável | Status   | Resultado Observado |
| :----- | :------------ | :---------- | :------- | :------------------ |
| CT01.1 | 23/11/2025    | [Seu Nome]  | Aprovado | Gráfico de barras por estado renderizado corretamente. |
| CT02.1 | 23/11/2025    | [Seu Nome]  | Aprovado | Gráfico de pizza exibe as categorias vindas do banco. |
| CT03.1 | 23/11/2025    | [Seu Nome]  | Aprovado | Gráfico de linha mostra a evolução temporal corretamente. |
| CT04.2 | 23/11/2025    | [Seu Nome]  | Aprovado | **Filtros Funcionais:** A troca de ano atualiza KPI, Barras e Pizza instantaneamente. |
| CT05.2 | 23/11/2025    | [Seu Nome]  | Aprovado | KPIs refletem a soma exata dos dados no banco SQLite. |