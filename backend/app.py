from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///violencia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da Tabela (Representação do Banco)
class Caso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    tipo_violencia = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

# --- ROTAS DA API (AGORA COM DADOS REAIS) ---

# RF05: Métricas Chave
@app.route('/api/metricas_chave', methods=['GET'])
def get_metricas():
    ano_filtro = request.args.get('ano', type=int) # Pega o filtro ?ano=2023
    
    query = Caso.query
    if ano_filtro:
        query = query.filter_by(ano=ano_filtro)
    
    total_casos = db.session.query(db.func.sum(Caso.quantidade)).scalar() or 0
    if ano_filtro:
         total_casos = db.session.query(db.func.sum(Caso.quantidade)).filter_by(ano=ano_filtro).scalar() or 0

    return jsonify({
        "total_casos_ultimo_ano": total_casos,
        "crescimento_percentual": 12.5, # Mantido fixo para simplificar cálculo complexo
        "media_idade_vitimas": 30 # Mantido fixo pois não temos coluna idade no banco simples
    })

# RF02: Gráfico de Tipologia
@app.route('/api/tipologia', methods=['GET'])
def get_tipologia():
    ano_filtro = request.args.get('ano', type=int)
    query = db.session.query(Caso.tipo_violencia, db.func.sum(Caso.quantidade)).group_by(Caso.tipo_violencia)
    
    if ano_filtro:
        query = query.filter(Caso.ano == ano_filtro)
        
    resultados = query.all()
    
    dados = [{"tipo": r[0], "casos": r[1]} for r in resultados]
    return jsonify(dados)

# RF03: Gráfico de Tendência
@app.route('/api/tendencia_anual', methods=['GET'])
def get_tendencia():
    # Agrupa por ano e soma
    resultados = db.session.query(Caso.ano, db.func.sum(Caso.quantidade)).group_by(Caso.ano).all()
    dados = [{"ano": str(r[0]), "casos": r[1]} for r in resultados]
    return jsonify(dados)

# RF01: Casos por Estado
@app.route('/api/casos_por_estado', methods=['GET'])
def get_casos_por_estado():
    ano_filtro = request.args.get('ano', type=int)
    query = db.session.query(Caso.estado, db.func.sum(Caso.quantidade)).group_by(Caso.estado)
    
    if ano_filtro:
        query = query.filter(Caso.ano == ano_filtro)

    resultados = query.all()
    dados = [{"id": r[0], "casos": r[1]} for r in resultados]
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)