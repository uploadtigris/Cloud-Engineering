from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# creating a base model class
class Item(BaseModel):
       text: str = None
       is_done: bool = False

items = []

# this decorator creates the path in FastAPI
@app.get("/")
def root():
        return {"Hello": "World"}

@app.post("/items")
# item here is an input parameter. 
# So, once the path receives the item, the item will be added to the "items" list.
def create_item(item: Item):
        items.append(item)
        return items

app.get("/items")
def list_items(limit: int = 10):
       return items[0:limit]

# {} --> used to query items from the list
@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
        if item_id < len(items):
                return items[item_id]
        else:
            raise HTTPException(status_code=404, detail=f'Item {item_id} not found')