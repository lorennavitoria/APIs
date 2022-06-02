from flask import Flask, jsonify
from restApi.construcaoApiVersao3.models.conversorJson import bancoJson, bancoJsonEncoder
from restApi.construcaoApiVersao3.bancoDados import bancoDados


app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = bancoJsonEncoder


@app.route('/')
def paginaIncial():
    return '<h1>Lista dos Sorteados para o Prêmio Principal<h1>' + '<p>Confira a lista...</p>'

@app.route('/ganhadores', methods=['GET'])
def ganhadores():
    return jsonify({'Ganhadores': bancoDados})


app.run()
