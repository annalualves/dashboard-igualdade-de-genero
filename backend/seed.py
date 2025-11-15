from app import app, db, Caso

# Cria o contexto da aplicação para acessar o banco
with app.app_context():
    # 1. Cria as tabelas (apaga se já existirem para reiniciar limpo)
    db.drop_all()
    db.create_all()

    # 2. Cria dados fictícios, mas estruturados no Banco
    print("Populando banco de dados...")
    
    dados = [
        # 2022
        {"ano": 2022, "estado": "SP", "tipo": "Física", "quantidade": 15000},
        {"ano": 2022, "estado": "RJ", "tipo": "Física", "quantidade": 8000},
        {"ano": 2022, "estado": "MG", "tipo": "Psicológica", "quantidade": 5000},
        {"ano": 2022, "estado": "BA", "tipo": "Física", "quantidade": 4000},
        {"ano": 2022, "estado": "SP", "tipo": "Sexual", "quantidade": 2000},
        # 2023
        {"ano": 2023, "estado": "SP", "tipo": "Física", "quantidade": 18000},
        {"ano": 2023, "estado": "RJ", "tipo": "Física", "quantidade": 9500},
        {"ano": 2023, "estado": "MG", "tipo": "Psicológica", "quantidade": 6000},
        {"ano": 2023, "estado": "BA", "tipo": "Física", "quantidade": 4500},
        {"ano": 2023, "estado": "SP", "tipo": "Sexual", "quantidade": 2500},
    ]

    for d in dados:
        novo_caso = Caso(
            ano=d['ano'],
            estado=d['estado'],
            tipo_violencia=d['tipo'],
            quantidade=d['quantidade']
        )
        db.session.add(novo_caso)

    db.session.commit()
    print("Banco de dados 'violencia.db' criado e populado com sucesso!")