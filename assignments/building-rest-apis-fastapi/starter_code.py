from typing import Optional, Dict

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory storage for items: id -> Item
_items: Dict[int, Item] = {}
_next_id = 1


@app.get("/items")
def list_items():
    return list(_items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _items[_next_id] = item
    _next_id += 1
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    updated.id = item_id
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del _items[item_id]
