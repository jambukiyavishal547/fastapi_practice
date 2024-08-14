from typing import Annotated
import uvicorn
from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel

fake_secret_token = "super-secret-token"

fake_db = {
    "foo":{
        "id":"foo",
        "title":"Foo",
        "description":"There goes my hero"
    },
    "bar":{
        "id":"bar",
        "title":"Bar",
        "description":"The bartenders"
    },
}
app = FastAPI()

class Item(BaseModel):
    id:str
    title: str
    description: str | None = None

@app.get("/items/{item_id}",response_model=Item,tags=["Test"])
async def read_main(item_id: str, x_token:Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="item not found")
    return fake_db[item_id]

@app.post("/items/",response_model=Item,tags=["Test"])
async def create_item(item: Item, x_token:Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400,detail="Item already exists")
    fake_db[item.id] = item
    return item 


# Debugging 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)