from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn main:app --reload
app = FastAPI()

@app.get("/")
def paginaPrincipal():
    return {"Olá": "Mundo"}


class Sorvete(BaseModel):
    id: int
    sabor: str
    preco: float


banco_de_dados=[

    Sorvete(id=1, sabor='Morango', preco=5.0),
    Sorvete(id=2, sabor='Chocolate', preco=5.50),
    Sorvete(id=3, sabor='Manga', preco=7.00),
    Sorvete(id=4, sabor='Amora', preco=4.00)
]


@app.get("/sorvetes")
def get_todos_sorvetes():
    return banco_de_dados


@app.get("/sorvetes/{id_sorvete}")
def get_sorvete_por_id(id_sorvete:int):
    for sorvete in banco_de_dados:
        if(sorvete.id == id_sorvete):
            return sorvete

    return {"Status": 404, "Mensagem": "Sorvete não encontrado"}


@app.post("/sorvetes")
def insere_sorvete(sorvete: Sorvete):
    banco_de_dados.append(sorvete)
    return sorvete
