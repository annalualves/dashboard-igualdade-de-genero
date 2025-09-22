# Projeto: Dashboard de Combate à Violência contra a Mulher
Dashboard para analisar o objetivo 5 de desenvolvimento sustentável no Brasil - Igualdade de Gênero com foco em violência contra a mulher.

# I. Objetivo
O objetivo deste projeto é criar um dashboard interativo para monitorar, analisar e visualizar dados sobre a violência contra a mulher no Brasil. A solução busca consolidar informações de fontes diversas e torná-las acessíveis de forma clara e visual. Isso permitirá que pesquisadores, estudantes, ativistas, jornalistas e formuladores de políticas públicas tenham uma ferramenta poderosa para entender as tendências, identificar padrões e, assim, apoiar a elaboração de estratégias mais eficazes de combate a esse problema social.

A aplicação aborda diretamente o Objetivo de Desenvolvimento Sustentável (ODS) 5 - Igualdade de Gênero, com foco na meta 5.2, que visa eliminar todas as formas de violência contra mulheres e meninas.

# II. Problema
Apesar da gravidade da violência contra a mulher no Brasil, os dados sobre o tema muitas vezes estão dispersos em relatórios, sites governamentais e bases de dados complexas, dificultando a análise integrada. Essa falta de uma plataforma centralizada e visualmente clara impede que a sociedade e os órgãos competentes compreendam a dimensão do problema, como sua distribuição geográfica e a evolução ao longo do tempo.

O problema principal, portanto, é a dispersão e a inacessibilidade dos dados, o que prejudica a conscientização, a pesquisa e a tomada de decisões baseadas em evidências para combater a violência de gênero de forma eficaz.

# III. Tipo de Solução
A solução proposta é um dashboard de dados, uma aplicação web que combina um backend e um frontend.

Frontend: Será a interface do usuário, responsável por exibir os gráficos, mapas e métricas de forma interativa.

Backend: Será o "motor" da aplicação, responsável por coletar, processar e servir os dados para o frontend através de uma API.

A escolha de um dashboard é a mais adequada porque a solução lida com um grande volume de dados estatísticos. O formato visual do dashboard é ideal para:

Síntese de Dados: Transformar informações complexas em gráficos e mapas de fácil compreensão.

Análise Rápida: Permitir que o usuário identifique rapidamente tendências, picos de violência e áreas de maior incidência.

Comunicação Efetiva: Facilitar a comunicação do problema para um público amplo, que pode não ter familiaridade com a análise de dados brutos.

# IV. Requisitos
Requisitos Funcionais (RFs)
- RF01: Dashboard de Incidência
  
    O sistema deve exibir um mapa interativo do Brasil que mostre a incidência de violência contra a mulher por estado ou cidade, usando um mapa de calor.

- RF02: Gráficos de Tipologia
  
    O sistema deve apresentar gráficos de barras e de pizza para detalhar os tipos de violência mais comuns (física, psicológica, sexual, etc.).

- RF03: Análise de Tendência
  
    O sistema deve incluir um gráfico de linhas para mostrar a evolução dos casos de violência ao longo dos anos.

- RF04: Filtros de Dados
  
    O sistema deve permitir que o usuário filtre os dados por tipo de violência, faixa etária da vítima, tipo de agressor e ano.

- RF05: Métricas Chave
  
    O sistema deve exibir cartões com métricas de destaque, como o total de casos registrados no último ano e a porcentagem de crescimento em relação ao ano anterior.

# V. Diagrama de Caso de Uso
O diagrama de caso de uso a seguir ilustra as principais interações dos atores com o sistema.

![Diagrama de Caso de Uso](docs/diagrama_caso_de_uso.png)

Atores:

- Usuário: Qualquer pessoa que acessa o dashboard para visualizar dados.

- Administrador: Pessoa responsável por carregar e atualizar os dados no sistema.

Casos de Uso:

- Visualizar Gráficos de Incidência: O usuário acessa e interage com os gráficos e mapas.

- Filtrar Dados: O usuário ajusta a visualização dos dados com base em critérios como período ou tipo de violência.

- Exportar Relatórios: O usuário salva os gráficos e dados para uso externo.

- Acessar Métricas Chave: O usuário consulta os números de destaque do dashboard.

- Gerenciar Dados: O administrador insere ou atualiza os dados da base de dados do backend.
