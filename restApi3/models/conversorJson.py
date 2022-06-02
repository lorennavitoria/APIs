from flask.json import JSONEncoder


class bancoJson(object):
    new_id = 1

    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        bancoJson.new_id += 1


class bancoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bancoJson):
            return obj.__dict__
        return super(bancoJsonEncoder, self).default(obj)
