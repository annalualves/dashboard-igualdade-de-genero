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

if __name__ == '__main__':
    app.run(debug=True, port=5000)