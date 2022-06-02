# estas classes só são para converter o objeto em json


from flask.json import JSONEncoder


class NGO(object):
    new_id = 1

    def __init__(self, nome, fundador, setor):
        self.nome = nome
        self.fundador = fundador
        self.setor = setor
        self.id = NGO.new_id
        NGO.new_id += 1


class NGOEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NGO):
            return obj.__dict__
        return super(NGOEncoder, self).default(obj)
