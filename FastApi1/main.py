from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn main:app --reload

app = FastAPI()

@app.get("/")
def paginaPrincipal():
    return {"Olá": "Mundo"}

class Musica(BaseModel):
    id: int
    nome: str
    cantor: str
    ano_lancamento = int

banco_dados=[

    Musica(id=1, nome='Sonhar', cantor='Maria', ano_lancamento=2010),
    Musica(id=2, nome='Céu', cantor='Rita', ano_lancamento=2020),
    Musica(id=3, nome='Vou Embora', cantor='Mario', ano_lancamento=2012)
]


@app.get("/musicas")
def mostrar_todas_musicas():
    return banco_dados


@app.get("/musicas/{id_musica}")
def mostrar_musica_por_id(id_musica:int):
    for m in banco_dados:
        if(m.id == id_musica):
            return m
    return {"Status":404, "Mensagem": "Música não encontrada"}


@app.post('/musicas')
def insere_musica(musica: Musica):
    banco_dados.append(musica)
    return musica

