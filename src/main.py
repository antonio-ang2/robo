from src.config import db
from src.models.Game import Game

games = db.session.query(Game).all()
for game in games:
    print(game)


