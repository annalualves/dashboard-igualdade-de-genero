from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir que o React (em localhost:3000) acesse

# RF05: Métricas Chave (Mockado)
@app.route('/api/metricas_chave', methods=['GET'])
def get_metricas():
    # No futuro, isso virá de um DB
    metricas = {
        "total_casos_ultimo_ano": 120500,
        "crescimento_percentual": 15.2,
        "media_idade_vitimas": 29.5
    }
    return jsonify(metricas)

# RF02: Gráficos de Tipologia (Mockado)
@app.route('/api/tipologia', methods=['GET'])
def get_tipologia():
    # No futuro, isso virá de um DB
    # Dados prontos para um gráfico de pizza/barra
    dados = [
        {"tipo": "Física", "casos": 75000},
        {"tipo": "Psicológica", "casos": 35000},
        {"tipo": "Sexual", "casos": 8500},
        {"tipo": "Patrimonial", "casos": 2000}
    ]
    return jsonify(dados)

# RF03: Gráfico de Linha de Tendência (Mockado)
@app.route('/api/tendencia_anual', methods=['GET'])
def get_tendencia():
    # Dados prontos para um gráfico de linha
    dados = [
        {"ano": "2019", "casos": 95000},
        {"ano": "2020", "casos": 105000},
        {"ano": "2021", "casos": 108000},
        {"ano": "2022", "casos": 115000},
        {"ano": "2023", "casos": 120500},
    ]
    return jsonify(dados)

# RF01: Mapa de Incidência (Mockado)
@app.route('/api/casos_por_estado', methods=['GET'])
def get_casos_por_estado():
    # Dados prontos para um mapa. O "id" deve corresponder ao ID do GeoJSON
    # Usaremos o "id" como a sigla do estado (UF)
    dados = [
        {"id": "AC", "casos": 1200},
        {"id": "AL", "casos": 2100},
        {"id": "AP", "casos": 800},
        {"id": "AM", "casos": 3500},
        {"id": "BA", "casos": 8000},
        {"id": "CE", "casos": 7200},
        {"id": "DF", "casos": 4000},
        {"id": "ES", "casos": 3900},
        {"id": "GO", "casos": 5100},            
        {"id": "MA", "casos": 4300},
        {"id": "MT", "casos": 3100},
        {"id": "MS", "casos": 2900},
        {"id": "MG", "casos": 10500},
        {"id": "PA", "casos": 6000},
        {"id": "PB", "casos": 3200},
        {"id": "PR", "casos": 9000},
        {"id": "PE", "casos": 7800},
        {"id": "PI", "casos": 2300},
        {"id": "RJ", "casos": 11500},
        {"id": "RN", "casos": 2800},
        {"id": "RS", "casos": 8800},
        {"id": "RO", "casos": 1900},
        {"id": "RR", "casos": 600},
        {"id": "SC", "casos": 6100},
        {"id": "SP", "casos": 25000},
        {"id": "SE", "casos": 1500},
        {"id": "TO", "casos": 1300}
    ]
    return jsonify(dados)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)