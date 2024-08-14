from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated
from sqlalchemy.orm import session 
from .import crud, models, schemas
from .database import sessinonlocal, engine

models.Base.metadata.create_all(bind=engine) 

app=FastAPI()

#embed = true
#dependency  --> for re-use and maintain the application at code level becomes easy 
def get_db():
    db = sessinonlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/",response_model=schemas.User)
def create_user(user:schemas.UserCreate, db: session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/",response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int =100, db: session = Depends(get_db)):
    users = crud.get_users(db,skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}",response_model=schemas.User)
def read_user(user_id: int,db: session = Depends(get_db)):
    get_id = schemas.User
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    return db_user

@app.post("/users/{user_id}/items/",response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item:schemas.ItemCreate, db:session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/",response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: session = Depends(get_db)):
    items = crud.get_items(db,skip=skip, limit=limit) 
    return items
    


# path peramiter formet check 

# @app.get("/users/{user_id}")
# async def read_usersss(user_id: int = None  | None):
#     return {"user_id": user_id}