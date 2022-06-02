import requests
from datetime import datetime
from prompt_toolkit.validation import Validator, ValidationError

listaLoc = []


def horas(timezone):
    url = 'http://worldtimeapi.org/api/timezone/' + timezone
    response = requests.get(url)
    response = datetime.fromisoformat(response.json()['datetime'])
    return response


def listaLocais():
    global listaLoc
    if (len(listaLoc) > 0):
        return listaLocais
    url = 'http://worldtimeapi.org/api/timezone/'
    response = requests.get(url)
    response = response.json()
    return response


class validarEscolhaUsuario(Validator):

    def validate(self, document):
        escolha = document.text
        if escolha not in listaLocais():  # listaLocais() retornará a lista dos locais, e então o not in irá verificar se tem ou não dentro da lista
            raise ValidationError(message="Escolha não disponível: " + escolha)
