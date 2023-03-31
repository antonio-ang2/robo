# Programa auxiliar que popula o banco de dados com alguns jogos

from src.models.Game import Game # Modelo de tabela de jogos
from src.config.db import session # Conexão com banco de dados

# Dados dos jogos
data = [
        {
            "name": "DEAD SPACE REMAKE",
            "device": "PS5",
            "price": 350,
            "quantity": 10
        },
        {
            "name": "FORSPOKEN",
            "device": "PC",
            "price": 299,
            "quantity": 8
        },
        {
            "name": "DEAD ISLAND 2",
            "device": "PS5",
            "price": 350,
            "quantity": 10
        },
        {
            "name": "HOGWARTS LEGACY",
            "device": "PC",
            "price": 219,
            "quantity": 7
        },
        {
            "name": "WILD HEARTS",
            "device": "Xbox Series",
            "price": 350,
            "quantity": 7
        },
        {
            "name": "RESIDENT EVIL 4",
            "device": "PS5",
            "price": 289,
            "quantity": 10
        },
        {
            "name": "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
            "device": "Switch",
            "price": 350,
            "quantity": 10
        },
]

# Função que popula o banco de dados com os jogos
def populate(data):
    # Para cada jogo no dicionário de dados
    for item in data:
        # Cria um objeto do tipo Game
        game = Game(
            name=item["name"],
            device=item["device"],
            price=item["price"],
            quantity=item["quantity"]
        )
        # Adiciona o jogo no banco de dados
        session.add(game)
    # Salva as alterações no banco de dados
    session.commit()

# Popula o banco de dados com os jogos
populate(data)