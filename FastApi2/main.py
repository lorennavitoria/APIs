from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():

    """
    Leitura root. Hello World da minha primeira API.
    """

    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    return {"item_id": item_id, "q": q}
