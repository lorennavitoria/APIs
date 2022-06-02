# é preciso instalar as dependencias: fastapi uvicorn
# criando API com FASTAPI
# para rodar este código, é preciso digitar no terminal toda vez que for execultar o código: uvicorn main:app --reload


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"Olá": "Mundo"}
