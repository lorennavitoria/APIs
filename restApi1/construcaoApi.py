
from flask import Flask, jsonify  # o jsonify é um conversor do Flask que converte o objeto em json
from restApi.construcaoApiVersao1.models.ngo import NGO, NGOEncoder
from restApi.construcaoApiVersao1.extensions import db  # aqui estamos importando o banco de dados bd do arquivo extensions.py

app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = NGOEncoder


@app.route('/')
def index():
    return '<h1>Encontre uma ONG</h1>' + '<p> Este site é um protótio de API para encontrar ONGs pelo Brasil.</p>'


# eu posso nomear a rota como eu quiser, outro exemplo de nome para esta rota: '/api/lista' ou 'api/bancodados/pag1', ou só '/api', etc
@app.route('/api/v1/resources/ngos', methods=[
    'GET'])  # eu preciso juntar esta rota com a rota raiz (rota raiz: http://127.0.0.1:5000),(rota para 'get' lista: http://127.0.0.1:5000/api/v1/resources/ngos)
def list_all():
    return jsonify({'ngos': db})


# agora é só fazer o POST, DELETE, PATCH, PUT

app.run()
