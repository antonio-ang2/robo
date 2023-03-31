from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models.Base import Base
from src.models.Game import Game

engine = create_engine('sqlite:///db.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)