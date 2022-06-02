from flask import Flask, request
from mainPostman2 import insertUsuario

'''
aqui está sendo criado uma API, e está sendo testado no Postman
'''

app = Flask("Youtube")


@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "Mundo"}


@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    '''
    no Postman eu adiciono/cadastro um novo usuário através de Json,
    e pra mim pegar o cadastro que eu fiz no Postman e trazer pra cá (Python), eu trago através do Body,
    o Body é quem guarda os dados da requisição.
    '''

    body = request.get_json()  # aqui com "request.get_json()" eu consigo pegar o body da requisição

    if ("nome" not in body):
        return geraResponse(400, "O parametro nome é obrigatório")

    if ("email" not in body):
        return geraResponse(400, "O parametro email é obrigatório")

    if ("senha" not in body):
        return geraResponse(400, "O parametro senha é obrigatório")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])  # chamamos este método para mostrar o cadastro...
    # ...feito (mas mostra apenas o nome e email, a senha é secreta). Para liberar acesso as informações cadastradas...
    # ... é pedido como paramentro no método, o nome, email e senha, se estiver tudo certo, é liberado as informações
    return geraResponse(200, "Usuário criado", "user", usuario)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response


app.run()
