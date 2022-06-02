import requests
from flask import Flask, jsonify

url = 'http://127.0.0.1:5000/ganhadores'
response = requests.get(url)
response = response.json()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def mostrar_ganhadores():
    return jsonify(response)


app.run(port=5001)
