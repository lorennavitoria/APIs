from flask import Flask, request

'''
GET dá pra usar dentro da própria URL, mas POST, PUT, etc, nao da pra passar pela url, pois as vezes é muitas
informações para passar através da URL,tem como construir tipo um site inteiro para fazer essas requisições, mas 
é mais trabalhoso. Então para testar as APIS, se usa ferramentas como o Postman ou Insomnia. Eles dão um retorno 
semelhante ao browser, mas é melhor para testar as APIs.
'''


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = {

    1: {
        "id": 1,
        "name": "João"
    },
    2: {
        "id": 2,
        "name": "Ana"
    }
}


def response_users():
    return {"users": list(users_data.values())}


@app.route("/")
def root():
    return "<h1>API com Flask</h>"


@app.route("/users")
def list_users():
    return response_users()


@app.route("/users", methods=[
    'POST'])  # aqui será a mesma rota que o de cima, mas a diferença é que será um POST, tudo na mesma página
def creat_User():
    body = request.json

    ids = list(users_data.keys())
    if ids:  # sgnificado: se eu tenho um id
        new_id = ids[-1] + 1
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }
    return response_users()


@app.route("/users/<int:user_id>", methods=["DELETE"])
# quando coloca <> isso, pode-se colocar um valor direto na url, aqui no caso, será o ID que se quer escluir, e essa função só recebe valores inteiros
def delete(user_id: int):
    user = users_data.get(user_id)  # tem que conferir se esse ID escolhido existe no Banco de Dados
    if user:
        del users_data[user_id]

    return response_users()


@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")

    if user_id in users_data:
        users_data[user_id]["name"] = name

    return response_users()


app.run(debug=True)
