import requests

api_url1 = "https://jsonplaceholder.typicode.com/todos/1"  # Serviço/servidor escolhido para fazer o teste. Este serviço retorna um conjunto de dados aleatórios

# GET (pegar)
response = requests.get(api_url1)  # requests: pedir
response.json()  # converte em json para visualizar resultado
print(response.json())
print(response.status_code)  # mostra status da resposta
print(response.headers["Content-Type"])  # mostra cabeçalho

# POST (criar um novo produto/informação etc)

api_url2 = "https://jsonplaceholder.typicode.com/todos"  # serviço/servidor escolhido para fazer o teste
todo = {"userId": 1, "title": "Comprar leite", "completed": False}
response = requests.post(api_url2, json=todo)
print(response.json())
print(response.status_code)

# PUT (atualiza um recurso existente, ou seja, modificar alguma informação já existente)

api_url3 = "https://jsonplaceholder.typicode.com/todos/10"  # serviço/servidor escolhido para fazer o teste
response = requests.get(api_url3)
print(response.json())

dados1 = {"userId": 1, "title": "Lavar o carro", "completed": True}
response = requests.put(api_url3, json=dados1)  # alterando/atualizando os dados
print(response.json())
print(response.status_code)
dados2 = {"userId": 1, "title": "Limpar a casa", "completed": True}
response = requests.put(api_url3, json=dados2)  # alterando/atualizando os dados mais uma vez
print(response.json())
print(response.status_code)

# PATCH (atualiza um recurso existente, mas apenas algumas coisas, que o programador pode escolher)

print(response.json())
dados3 = {"title": "Correndo na rua"}
response = requests.patch(api_url3, json=dados3)
print(response.json())
print(response.status_code)

# DELETE (excluir)

response = requests.delete(api_url3)
print(response.json())
print(response.status_code)

# /////////////////////////////////////


api_url4 = "https://jsonplaceholder.typicode.com/todos/7"

response = requests.get(api_url4)
print(response.json())

response = requests.delete(api_url4)
print(response.json())
