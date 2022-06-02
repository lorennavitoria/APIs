import requests

TOKEN = ""
tipoConsulta = 2

# "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token"


if tipoConsulta == 1:
    cidade = input("Informe o nome da cidade:")
    url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(cidade) + "&token=" + str(TOKEN)
    response = requests.get(url)  # ou: response = requests.request("GET", url)
    response = response.json()  # sempre lembra que na variável response será armazenado uma lista/tupla, por isso, para acessar os dados, é preciso coloca-lo dentro de um for.

    for chave in response:
        id = chave['id']
        nome = chave['name']
        estado = chave['state']
        pais = chave['country']
        print("ID: " + str(id) + " | Nome: " + str(nome) + " | Estado: " + str(estado) + " | País: " + str(pais) + "\n")
        # print(response)

    newCidade = input("Informe o ID da cidade desejada:")
    url = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + str(TOKEN) + "/locales"
    payload = "localeId[]=" + str(newCidade)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.put(url, headers=headers, data=payload)
    print(response)

if tipoConsulta == 2:
    url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/5959/current?token=" + str(TOKEN)
    response = requests.get(url)
    response = response.json()
    print(response)
