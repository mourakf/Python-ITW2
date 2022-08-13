from fastapi import FastAPI, Header
from typing import Union, Optional
# modelo
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    dsc: str
    qt: int
    value: float


app = FastAPI()

itens = []


@app.get("/items")
async def read_item():
    return itens


@app.post("/items")
async def add_item(novo_item: Item):
    itens.append(novo_item)
    return novo_item
