# Programa principal que mostra os jogos cadastrados no banco de dados no console, numa rota API e na página inicial do site

from src.config import db # Conexão com banco de dados
from src.models.Game import Game # Modelo de tabela de jogos
from flask import Flask, render_template # Framework web

# Pega todos os jogos cadastrados no banco de dados
games = db.session.query(Game).all()

# Mostra os jogos cadastrados no console
for game in games:
    print(game)

# Cria o servidor web
app = Flask(__name__)

# Rota API que retorna todos os jogos cadastrados no banco de dados
@app.route('/games')
def get_games():
    # Retorna os jogos em formato JSON
    return [game.return_json() for game in games]

# Rota que mostra a página inicial do site
@app.route('/')
def index():

    # Retorna os jogos em formato JSON
    games_in_json = [game.return_json() for game in games]

    # Formata o preço dos jogos para o formato brasileiro
    for game in games_in_json:
        splitted_price = str(game['price']).split('.') # Separa as partes inteira e decimal do preço

        # Formata o preço para o formato brasileiro (ex: 350,00)
        game['price'] = splitted_price[0] + ',' + (splitted_price[1] + '0' if len(splitted_price[1]) == 1 else splitted_price[1])

    # Retorna a página inicial do site com os jogos em formato JSON
    return render_template('index.html', games=games_in_json)

# Inicia o servidor web
if __name__ == '__main__':
    app.run(debug=True)