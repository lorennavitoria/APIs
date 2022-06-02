from funcoes2 import listaLocais, horas, validarEscolhaUsuario
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

variavel_buscar_lista = listaLocais()
listaOpcao = WordCompleter(variavel_buscar_lista, ignore_case=True, match_middle=True)
escolha = prompt("Escolha o local: ", completer=listaOpcao, validator=validarEscolhaUsuario(),
                 validate_while_typing=False)
horario = horas(escolha)
print(horario.strftime("%d/%m/%Y %H:%M:%S"))
