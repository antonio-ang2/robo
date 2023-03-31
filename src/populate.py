from src.models.Game import Game
from src.config.db import session

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

def populate(data):
    for item in data:
        game = Game(
            name=item["name"],
            device=item["device"],
            price=item["price"],
            quantity=item["quantity"]
        )
        session.add(game)
    session.commit()

populate(data)