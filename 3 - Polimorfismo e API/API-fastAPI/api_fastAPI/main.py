from fastapi import FastAPI, Header
from typing import Union, Optional
# modelo
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    dsc: str
    value: float


app = FastAPI()


@app.get("/")
async def read_root(user_agent: Optional[str] = Header(None)):
    return user_agent


@app.get("/items/{item_id}")
async def read_item(item_id: int, p: bool, q: Union[str, None] = None):
    return {"item_id": item_id, "p": p, "q": q}


@app.post("/items")
async def add_item(novo_item: Item):
    return novo_item
