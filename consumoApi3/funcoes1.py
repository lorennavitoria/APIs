import requests
from datetime import datetime
from prompt_toolkit.validation import Validator, ValidationError

timezones = []


# link da API: http://worldtimeapi.org/pages/examples

def hora(timezone):
    url = "http://worldtimeapi.org/api/timezone/" + timezone
    response = requests.get(url)
    hora = datetime.fromisoformat(response.json()['datetime'])  # significado: do formato ISO, tranforme em Datetime
    return hora


def timezones_disponiveis():
    global timezones

    # para não carregar a API toda vez que execultar o código, se a lista já foi chamada e armazenada, ele só retorna a lista. Entao quando ele entrar na linha do primeiro return, ele já sairá
    # da função timezones_disponiveis sem execultar as linhas que é chamada a api/url. Se for a primeira vez execultando o código
    # ele não entrará no if, e execultará as próximas 4 linhas abaixo
    if (len(timezones) > 0):
        return timezones

    url = 'http://worldtimeapi.org/api/timezone/'
    response = requests.get(url)
    timezones = response.json()
    return timezones


class TimezoneValidador(Validator):
    def validate(self, document):
        texto = document.text

        if texto not in timezones_disponiveis():
            raise ValidationError(message="Timezone não disponível: " + texto)
