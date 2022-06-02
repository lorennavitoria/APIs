from flask import Flask, jsonify

'''
Todas as vezes que execultar esse código, ele, por padrão abrirá na rota raiz (a rota inicial (/)). Mas se eu quizer ver a rota 2 (a segunda rota), ou a rota 3,etc, basta eu adicionar, já na url 
carregada no navegador, a rota que eu quero ver.
ex:
será carregada a pagina inicial/raiz e aparecerá isso:
conteudo da url:http://127.0.0.1:5000/
conteudo da página:Olá mundo!
para carregar a rota 2, basta eu adicionar no navegador:
conteudo da url:http://127.0.0.1:5000/rota2
conteudo da página: Essa é a segunda rota da aplicação
'''

app = Flask(__name__)


@app.route('/')
def raiz():
    return 'Olá mundo!'


@app.route('/rota2')
def rota2():
    return '<H1>Essa é a segunda rota da aplicação</h1>'


'''
Nas linhas de baixo, criei uma rota chamada pessoas, e que vai receber 2 paramentros: <string:nome>/<string:cidade>
o nome da pessoa e da cidade eu coloco diretamente na url:
escreve na url: http://127.0.0.1:5000/pessoas/Maria/Rio%20de%20Janeiro
da enter
aparece na url: http://127.0.0.1:5000/pessoas/Maria/Rio%20de%20Janeiro
aparece na página: 
{
  "Cidade": "Rio de Janeiro", 
  "Nome": "Maria"
}
'''


@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoas(nome, cidade):
    return jsonify({'Nome': nome, 'Cidade': cidade})


app.run(debug=True)  # isso é apenas para rodar o código.
