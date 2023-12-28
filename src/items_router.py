from fastapi import APIRouter, HTTPException
from service import Service
from models import Item
import os

router = APIRouter()
service = Service()
machine_name = os.environ.get('MACHINE_NAME', 'unknown')

#  Healthy check
@router.get("/health")
def health():
    return { "status": "ok",
            "machine_name": machine_name}

# Route to create an item
@router.post("/items/", response_model=Item)
def create_item(item: Item):
    item = service.create_item(item)
    return item


# Endpoint to retrieve a list of items
@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10):
    return service.read_items(skip, limit)
    
   
# Route to read an item
@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = service.read_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Route to update an item
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    item = service.update_item(item_id, item)
    item.id = item_id
    return item

# Route to delete an item
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    service.delete_item(item_id)
    return {"id": item_id}
