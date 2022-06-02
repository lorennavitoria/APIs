from flask import Flask, jsonify
import pandas as pd

# sempre que importar o Flask, é preciso fazer 2 coisas para ele funcionar
# 1º coisa -> inicializar o Flask:

app = Flask(__name__)


# cada função construída, será uma página:


@app.route('/')
def homepage():
    return 'A API está no ar'


@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('baseDadosExemplo.csv')
    total_vendas = tabela['VendasQtd'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


# 2º coisa -> rodar a api:
app.run()
