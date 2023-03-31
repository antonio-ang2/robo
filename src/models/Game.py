# Modelo da entidade de jogos

from src.models.Base import Base # Classe base para criar as tabelas
from sqlalchemy import Column, Integer, String, Float # Para criar as colunas da tabela

# Classe que representa a tabela de jogos
class Game(Base):

    # Nome da tabela
    __tablename__ = 'games'

    # Colunas da tabela
    id = Column(Integer, primary_key=True) # Chave primária
    name = Column(String)
    device = Column(String)
    price = Column(Float) # Preço em decimal
    quantity = Column(Integer)
    
    # Função que retorna uma representação em string do objeto, com preço em formato brasileiro
    def __repr__(self):
        # Formata o preço para o formato brasileiro (ex: 350,00)
        splitted_price = str(self.price).split('.') # Separa as partes inteira e decimal do preço
        price = splitted_price[0] + ',' + (splitted_price[1] + '0' if len(splitted_price[1]) == 1 else splitted_price[1])

        # Retorna a representação em string do objeto
        return f'{self.name} - {self.device} - R$ {price} - {self.quantity}'
    
    # Função que retorna um dicionário com os dados do objeto
    def return_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'device': self.device,
            'price': self.price,
            'quantity': self.quantity
        }