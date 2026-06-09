from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


DB: Dict[int, Item] = {}
NEXT_ID = 1


@app.get("/items")
def list_items():
    return [{"id": id_, **item.dict()} for id_, item in DB.items()]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = DB.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **item.dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global NEXT_ID
    item_id = NEXT_ID
    DB[item_id] = item
    NEXT_ID += 1
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    DB[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    del DB[item_id]
