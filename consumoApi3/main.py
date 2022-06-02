from funcoes1 import hora, timezones_disponiveis, TimezoneValidador
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

disponiveis = timezones_disponiveis()
opcoes_timezone = WordCompleter(disponiveis, ignore_case=True, match_middle=True)
# o ignore_case fará ele ignorar escritas com letras maiusculos/minusculas
# o match_middle faz com que ele procure palavas digitadas pelo usuário em qualquer parte de lista, não só do começo, mas do meio tb, ex: opção America/Brasil/São Paulo, se eu escrver Brasil, ele já vai para as opções que tem Brasil, sem o usuario precisar digitar primeiro o continente


timezone = prompt("Escolha o Timezone:", completer=opcoes_timezone, validator=TimezoneValidador(),
                  validate_while_typing=False)

data_no_timezone = hora(timezone)
print(data_no_timezone.strftime("%d/%m/%Y %H:%M:%S"))
