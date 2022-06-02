import requests

# "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/distritos"


estados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"
responseEstado = requests.get(estados).json()
print(responseEstado)
print("\n")
for x in responseEstado:
    id_Estado = x['id']
    nome_Estado = x['nome']
    print("ID Estado: " + str(id_Estado) + " | Nome do Estado: " + str(nome_Estado))

estadoEscolhido = input("\nEscolha o Estado desejado e digite seu ID:\n")
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/" + str(estadoEscolhido) + "/municipios"
responseMunicipio = requests.get(url).json()

for chave in responseMunicipio:
    idMunicipio = chave['id']
    nomeMunicipio = chave['nome']
    # idEstado = chave['mesorregiao']
    idEstado = responseMunicipio[1][2]
    print("| ID_Estado: " + str(idEstado) + " | cod_IBGE: " + str(idMunicipio) + " | Nome_Município: " + str(
        nomeMunicipio) + "\n")
    # print(response)
