import requests


url = "https://jsonplaceholder.typicode.com/users"

print("Pesquise pelo nome de usuário:")
user = input("> ")
queryURL = url + f"?username={user}"
response = requests.get(queryURL)

print(response.text)
