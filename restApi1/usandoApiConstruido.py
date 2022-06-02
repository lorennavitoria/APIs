import requests
import json
from flask import Flask, jsonify

# esta url foi a que eu construi. Está dentro do diretório 'construcaoApiVersao1'
url = 'http://127.0.0.1:5000/api/v1/resources/ngos'  # para usar esta api, ela precisa estar aberto no navegador
response = requests.get(url)
response = response.json()
print(response)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def buscar_dados():
    return jsonify(response)


app.run(port=5001)  # para o código rodar corretamente, é preciso usar uma porta diferente da porta da API construida
