from src.models.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    device = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
    def __repr__(self):
        print(str(self.price))
        return f'{self.name} - {self.device} - R$ - {self.quantity})'