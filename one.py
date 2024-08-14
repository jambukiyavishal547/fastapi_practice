
# from enum import Enum

# from fastapi import (FastAPI, Query, Body,Cookie,Header,File,UploadFile ,
#                       HTTPException, Request,status, Depends)
# from fastapi.exception_handlers import http_exception_handler,request_validation_exception_handler
# from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
# from requests import Session
# from starlette.responses import PlainTextResponse
# from pydantic import HttpUrl,BaseModel , Field, EmailStr
# tags_metadata = [
#     {
#         "name": "users",
#         "description": "Operations with users. The **login** logic is also here.",
#     },
#     {
#         "name": "items",
#         "description": "Manage items. So _fancy_ they have their own docs.",
#         "externalDocs": {
#             "description": "Items external docs",
#             "url": "https://fastapi.tiangolo.com/",
#         },
#     },
# ]
# app = FastAPI(openapi_tags=tags_metadata)
# app = FastAPI()
# from typing import Union, Annotated ,Literal,Any
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"} 







# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(...,title="The ID of the item to get")],
#     q: Annotated[Union[str, None], Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results




# @app.get("/item/{item_id}")
# async def read_items(
#     *,
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q and size:
#         results.update({"q": q})
#         results.update({"size": size})
#     return results



# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=30
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None

# class Item1(BaseModel):
#     name: str
#     description: str | None = None
#     price : float
#     tax : float | None = None   

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }

# class Item2(BaseModel):
#     name: str = Field(max_length=100)
#     description: str | None = Field(default=None, description='the discription of the item2')
#     price : float = Field(gt=0)
#     tax : float | None = Field(default=None, gt=0)
#     tags  : list[str] = []
    


# @app.get('/item/{item_id}')
# async def get_item(item_id: int, item:Annotated[str,Query(title='the title of query',alias='alias')]):
#     return {'item':item}


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# class Image(BaseModel):
#     url : HttpUrl
#     name : str


# class Item(BaseModel):
#     name : str 
#     des : str | None = None
#     price  :  float
#     tax :float | None = None
#     tags : list [str] = []
#     image: list[Image] | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item  ):
#     results = {"item_id": item_id, "item": item}
#     return results



## Declare Request Example Data

# class Item(BaseModel):
#     name : str 
#     des : str | None = None
#     price  :  float
#     tax :float | None = None

#     # model_config = {
#     #     "json_schema_extra": {
#     #         "examples": [
#     #             {
#     #                 "name": "Foo",
#     #                 "description": "A very nice Item",
#     #                 "price": 35.4,
#     #                 "tax": 3.2,
#     #             }
#     #         ]
#     #     }
#     # }


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, 
#     item: Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal":{
#                     "summary":"a normal example",
#                     "description":"a **normal** item work correctly",
#                     "value":
#                     {
#                         'name':'foo',
#                         'des':'desctiption of declare request',
#                         'price':34.43,
#                         'tax':6, 
#                     },
#                 },
#                 "converted":{
#                     "summary":"an example with converted data",
#                     "description":"fastapi can __convert__ price 'string' to _actual_ 'number' auto",
#                     "value":{
#                         "name":"Baz",
#                         "prince":"35.4", 
#                     },
#                 },
#                 "invalid":{
#                     "summary":"Invalid data is rejected with an error",
#                     "value":{
#                         "name":"Bar",
#                         "price":"thirty five point four", 
#                     },
#                 },
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results





## extra data type

# from datetime import datetime, time, timedelta
# from typing import Annotated
# from uuid import UUID

# @app.put("/items/{item_id}")
# async def read_items(
#     item_id : UUID,
#     start_datetime: datetime = Body(),
#     end_datetime  : datetime = Body(),
#     process_after : timedelta = Body(),
#     repeat_at : time| None = Body(None),
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return{
#         "item_id":item_id,
#         "start_datetime":start_datetime,
#         "end_datetime": end_datetime,
#         "process_after":process_after,
#         "repeat_at":repeat_at,
#         "start_process":start_process,
#         "duration":duration,
#     }



## Cookie Header Parameters

# @app.get("/items/")
# async def read_items(
#     cookie_id:str | None = Cookie(None),
#     accept_encoding:str | None = Header(None),
#     connection : str | None = Header(None),
#     sec_ch_ua : str | None = Header(None),datetime
#     user_agent : str | None = Header(None),
#     Host : str | None = Header(None),
#     Sec_Fetch_Site: str | None = Header(None),

#     ):
#     return {
#         "cookie_id":cookie_id,
#         "accept_encodig":accept_encoding,
#         "connection": connection,
#         "sec_ch_ua":sec_ch_ua,
#         "user_agent":user_agent,
#         "Host":Host,
#         "Sec-Fetch-Site":Sec_Fetch_Site,
#     }


## Response Model - Return Type

# class Items(BaseModel):
#     name:str
#     des :str | None =None
#     price : float
#     tax :  float = 10.5
#     tags : list[str] =[]

# items ={
#     "foo":{"name":"foo", "price":50.2},
#     "bar":{"name":"bar", "des":"the bar","price":62,"tax":20.2},
#     "baz":{"name":"baz", "des":None, "price":50.2, "tax":10.5,"tags":[]},
# }

# # @app.get('/items/{item_id}',response_model=Items,response_model_exclude_unset=True)
# # async def read_item(item_id:Literal["foo","bar","baz"]):
# #     return items[item_id]

# # @app.post("/items/",response_model=Items)
# # async def create_item(item:Items):
# #     return item


# @app.post("/items/",response_model=Items)
# async def create_item(item: Items) -> Any:
#     return item


# @app.get("/items/",response_model=list[Items])
# async def read_itsems() -> Any:
#     return [
#         Items(name="Portal Gun", price=42.0),
#         Items(name="Plumbus", price=32.0),
#     ]

# class Userbase(BaseModel):
#     username :str
#     fullname : str | None = None
#     email : EmailStr

# class UserIn(Userbase):
#     password : str

# class userout(BaseModel):
#     ...


# @app.post("/users/")
# async def create_user(user:UserIn) -> Userbase:
#     return user 

# @app.get(
#         "/items/{item_id}/name",
#         response_model=Items,
#         response_model_include={"name","des"},
#         )
# async def read_item_name(item_id:Literal['foo','bar','baz']):
#     return items[item_id]

# @app.get(
#         "/items/{item_id}/public",
#         response_model=Items,
#         response_model_exclude={"tax"},
#         )
# async def read_items_public(item_id:Literal["foo","bar","baz"]):
#     return items[item_id]


##Extra Models

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: str | None = None


# def fake_password_hasher(raw_password:str):
#     return "supersecret" + raw_password

# def fake_save_user(user_in:UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(),hashed_password=hashed_password)
#     print("user saved")
#     return user_in_db

# @app.post("/user/",response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved 


## request files
#uploadfile file 
#file       byte

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}


#Handling Errors

# items = {"foo": "The Foo Wrestlers"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(404, detail="Item not found",headers={"X-Error":"There goes my error"},)
#     return {"item": items[item_id]}



# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# @app.exception_handler(UnicornException)
# async def unicorn_exception_hedler(request:Request, exc:UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message":f"Oops! {exc.name} did somthing. there goes a rainbow..."},
#     )
# @app.get("/ /{name}")
# async def read_unicorn(name:str):
#     if name == 'yolo':
#         raise UnicornException(name=name)
#     return {"unicorn_name":name}

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request,exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request,exc):
#     return PlainTextResponse(str(exc), status_code=400)

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id":item_id}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request:Request, exc:RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail":exc.errors(), "body":exc.body}),
#     )

# class Item(BaseModel):
#     title:str
#     size : int

# @app.post("/items/")
# async def  create_item(item: Item):
#     return item 

# @app.exception_handler(HTTPException)
# async def custom_http_exception_handler(request,exc):
#     print(f"OMG! An HTTP error!:{repr(exc)}")
#     return await http_exception_handler(request,exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request,exc):
#     print(f"OMG! the client sent invalid data!:{exc}")
#     return await request_validation_exception_handler(request,exc)

# @app.get("/items/{item_id}",status_code=status.HTTP_202_ACCEPTED)
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I Don't like 3")
#     return {"item_id":item_id}


## path operation configuration


# class Items(BaseModel):
#     name :str =Field(example="abcd")
#     des : str | None = Field(None,example="abcdefghi")
#     price : float = Field(example=34)
#     tax : float | None = Field(example=3)
#     tags: set[str] = Field(set(),example=['a','b'])


# class Tags(Enum):
#     items = "Items"
#     users = "Users"
    

# @app.post(
#         "/items/",
#         response_model=Items, 
#         tags=[Tags.items],
#         summary="create an item",
#         response_description="The created item", 
#         )
# async def create_item(item:Items):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name 
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# @app.get("/items/",tags=[Tags.items])  # deprecated=True
# async def read_items():
#     return [{"name":"foo","price":42}]

# @app.get("/users/",tags=[Tags.users])
# async def read_users():
#     return [{"username":"johndoe"}]



# JSON Compatible Encoder

# fake_db = {}

# class Item(BaseModel):
#     title:str
#     timestamp:datetime
#     description:str | None = None

# @app.put("/items{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data 


# body update

# class Items(BaseModel):
#     name :str  | None = None
#     des : str | None = None
#     price : float | None = None
#     tax : float = 10.5
#     tags: list[str] = []

# items = {
#     "foo":{"name":"Foo", "price":50.2},
#     "bar":{"name":"Bar", "description":"the bartenders","price":62, "tax":20.2},
#     "baz":{"name":"Baz", "description":None, "price":50.2,"tax":10.5,"tags":[]},
# }

# @app.get("/items/{item_id}", response_model=Items)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.put("/items/{item_id}",response_model=Items)
# async def update_item(item_id: str, item:Items):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded

# @app.patch("/items/{item_id}",response_model=Items)
# async def update_item(item_id: str, item:Items):
#     stored_item_data = items[item_id]
#     stored_item_model = Items(**stored_item_data)
#     update_data = item.dict(exclude_unset=True)
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     return updated_item

## Dependencies

# class as Dependencies
# fuction depends 
# async def common_parameters(q:str | None = None, skip: int = 0, limit: int = 100):
#     return {"q":q, "skip":skip, "limit":limit}

# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons

# @app.get("/users/")
# async def read_users(commons:Annotated[dict, Depends(common_parameters)]):
#     return commons 

#class depends
# fake_items_db = [
#     {"item_name":"foo"},
#     {"item_name":"Bar"},
#     {"item_name":"Baz"} 
# ]

# class CommonQueryParams:
#     def __init__(self,q: str| None = None, skip: int = 0, limit: int = 100) :
#         self.q= q
#         self.skip = skip
#         self.limit = limit

# @app.get("/items/")
# async def read_items(commons:Annotated[CommonQueryParams, Depends()]):
#     response = {}
#     if commons.q:
#         response.update({"q":commons.q})
#     items = fake_items_db[commons.skip:commons.skip+commons.limit]
#     response.update({"items":items})
#     return response 

# sub-dependencies

# def query_extractor(q: str | None = None):
#     return q

# def query_or_cookie_extractor(
#         q:Annotated[str, Depends(query_extractor)],
#         last_query:Annotated[str | None,Cookie()] = None,
# ):
#     if not q:
#         return last_query
#     return q
# @app.get("/items/")
# async def read_query(
#     query_or_default:Annotated[str, Depends(query_or_cookie_extractor)],
# ):
#     return {"q_or_cookie":query_or_default}


# dependancies in path operations

# async def verify_token(x_token: Annotated[str, Header()]):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


# async def verify_key(x_key: Annotated[str, Header()]):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#     return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]   

#global dependancies
# async def verify_token(x_token:Annotated[str, Header()]):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-token header invalid")
    
# async def verify_key(x_key:Annotated[str,Header()]):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400,detail="x-key header invalid")
#     return x_key

# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

# @app.get("/items/")
# async def read_items():
#     return [
#         {"item":"portal gun"},
#         {"item":"plumbus"}]

# @app.get("/users/")
# async def read_users():
#     return [
#         {"username":"rick"},
#         {"username":"morty"}]

#dependencies with yield

#sub- dependencies with yeild

# data = {
#     "plumbus":{"description":"freshly pickled plumbus","owner":"Morty"},
#     "portal-gun":{"description":"gun to create portals","owner":"Rick"},
# }

# class OwnerError(Exception):
#     ...

# def get_username():
#     try:
#         yield "Rick"
#     except OwnerError as e:
#         raise HTTPException(status_code=400, detail=f"owner error:{e}")
    
# @app.get("/items/{item_id}")
# def get_item(items_id: str, username:Annotated[str, Depends(get_username)]):
#     if items_id not in data:
#         raise HTTPException(status_code=404, detail="Item not found")
#     item = data[items_id]
#     if item["owner"] != username:
#         raise OwnerError(username)
#     return item 

# class InternalError(Exception):
#     pass 

# def get_username():
#     try:
#         yield "Rick"
#     except InternalError:
#         print("Oops, we didn't raise again, Britney")
#         raise

# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
#     if item_id == "portal-gun":
#         raise InternalError(
#             f"The portal gun is too dangerous to be owned by {username}"
#         )
#     if item_id != "plumbus":
#         raise HTTPException(
#             status_code=404, detail="Item not found, there's only a plumbus here"
#         )
#     return item_id 


# class MySuperContextManager:
#     def __init__(self):
#         self.db = Session()

#     def __enter__(self):
#         return self.db

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.db.close()


# async def get_db():
#     with MySuperContextManager() as db:
#         yield db 

#security 
#security first step
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token} 

#get current user
# class User(BaseModel):
#     username : str
#     email : str | None = None
#     fullname : str | None = None
#     disabled : bool | None = None

# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@gmail.com", fullname="john doe"
#     )

# async def get_current_user(token: Annotated[str,Depends(oauth2_scheme)]):
#     user = fake_decode_token(token)
#     return user

# @app.get("/users/me")
# async def read_user_me(current_user:Annotated[User, Depends(get_current_user)]):
#     return current_user

#Simple OAuth2 with Password and Bearer

# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True,
#     },
# }


# def fake_hash_password(password: str):
#     return "fakehashed" + password


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str 


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict) 


# def fake_decode_token(token): 
#     user = get_user(fake_users_db, token) 
#     return user 


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]): 
#     user = fake_decode_token(token) 
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user


# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token") 
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password") 

#     return {"access_token": user.username, "token_type": "bearer"}


# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return current_user  

## OAuth2 with Password (and hashing), Bearer with JWT tokens

# from datetime import datetime, timedelta, timezone
# from typing import Annotated

# import jwt
# import time
# from fastapi import Depends, FastAPI, HTTPException, status,Body
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt.exceptions import InvalidTokenError
# from passlib.context import CryptContext
# from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
# SECRET_KEY = "0e6dc6266aa62e54ce214c9466d3294ba0ec6ff9531761e21354f9cb683e0541"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     },
#     "bazboo":{
#         "username":"bazboo",
#         "full_name":"Baz Boo",
#         "email":"bazboo@example.com",
#         "hashed_password":"$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     },
#     "barkoo":{
#         "username":"barkoo",
#         "full_name":"Bar koo",
#         "email":"barkoo@example.com",
#         "hashed_password":"$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled":True 
#     }
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# app = FastAPI()


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token")
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
# ) -> Token:
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")


# @app.get("/users/me/", response_model=User)
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]

# middleware 
#simple middleware

# @app.middleware("http")
# async def add_prosecc_time_header(request:Request, call_next):
#     start_time =time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time 
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

# --> CORS(cross-origin resource sharing)
# import uvicorn
# from starlette.middleware.cors import CORSMiddleware


# origins = [
#     "hhtp://localhost.tiangolo.com",
#     "http://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials =True,
#     allow_methods = ["*"],
#     allow_headers = ["*"], 
# )

# @app.get("/")
# async def main():
#     return {"message":"hello world"} 

# @app.post("/")
# async def main():
#     return {"message":"hello world in post"} 

# @app.put("/")
# async def main():
#     return {"message":"hello world in put"}

# @app.delete("/")
# async def main():
#     return {"message":"hello world in delete"}

# @app.patch("/")
# async def main():
#     return {"massage":"hello world in patch"}

# @app.options("/")
# async def main():
#     return {"massage":"hello from option method"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", ports=8001)


# -->SQL(Relational) Databases ---> database.py


# background tasks
# from starlette.background import BackgroundTasks
# from pydantic import EmailStr
# from typing import Union
#metadata and document url
# description = """
# ChimichangApp API helps you do awesome stuff. 🚀 

# ## Items

# You can **read items**.

# ## send notification.

# You will be able to:

# * **send notification** (_not implemented_).
# * **Read items** (_not implemented_). \n
# the description of the fastapi 
# """

# app = FastAPI(
#     # document url change
#     docs_url="/UI",
#     #--------------------
#     title="background task",
#     description= description,
#     summary= "the symmry of the fastapi argument",
#     version="0.0.0.1",
#     terms_of_service="https://linkofterms.com/terms/",
#     contact={
#         "name":"Synchronized codelab",
#         "url":"https://google.com/contact",
#         "email":"contact@fb.com",
#     },
#     license_info={
#         "name":"apache 2.0",
#         "url":"https://www.apache.org/licenses/LICENSE-2.0.html",
#         # "identifier":"MIT" 
#     },
# )

#metadata for tags

# tags_m = [
#     {
#         "name":"users",
#         "description":"Operations with users ",
#     },
#     {
#         "name":"items",
#         "description":"Manage items",
#         "externalDocs":{
#             "description":"Items external docs", 
#             "url":"https://fastapi.tiangolo.com/", 
#         },
#     },
# ]

# app = FastAPI(openapi_tags=tags_m) 

# @app.get("/items/",tags=["items"])
# async def read_items():
#     return [{"name":"Katana"}]

# def Write_notification(email: str, message=""):
#     with open("log.txt", mode="a") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)

# @app.post("/send-notification/{email}",tags=["users"])
# async def send_notification(email: EmailStr, msg:str,background_task:BackgroundTasks):
#     background_task.add_task(Write_notification, email, msg)
#     return {"message":"notification sent in the background"} 



# def write_log(message: str):
#     with open("log.txt", mode="a") as log:
#         log.write(message)


# def get_query(background_tasks: BackgroundTasks, q: Union[str, None] = None):
#     if q:
#         message = f"found message: {q}\n"
#         background_tasks.add_task(write_log, message)
#     return q


# @app.post("/send-notification/{email}")
# async def send_notification(
#     email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
# ):
#     message = f"message for {email}\n"
#     background_tasks.add_task(write_log, message)
#     return {"message": "Message sent"}    




# --> OpenAPI URL
# from fastapi import FastAPI

# app = FastAPI(openapi_url="/api/v1/openapi.json")

# @app.get("/items/")
# async def read_items():
#     return [{"name":"Foo"}]


# -->   docs url 
# from fastapi import FastAPI

# app = FastAPI(docs_url="/documentation", redoc_url=None)


# @app.get("/items/")
# async def read_items():
#     return [{"name": "Foo"}]


# --> static files

'''
The creation of two or more APIs and using them in a project consumes more memory
The more efficient way is to mount the APIs on each other, 
which will consume less memory and give a different path to each API
'''
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# from fastapi import FastAPI
# app = FastAPI()


# @app.get("/app")
# def main_app():
# 	return "Main app called!"


# subapp = FastAPI()


# @subapp.get("/app2")
# def sub_app():
# 	return "Sub app called!"


# app.mount("/subapp", subapp) 


# --> Testing 

# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app = FastAPI()

# @app.get("/",tags=["Testing"])
# async def read_main():
#     return {"msg":"This is Testing"}

# client = TestClient(app)
# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg":"This is Testing"}



#Debugging
# import uvicorn
# from fastapi import FastAPI

# app = FastAPI() 


# @app.get("/",tags=["Test"])
# def root():
#     a = "a"
#     b = "b" + a
#     return {"hello world": b}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=1000) 


from fastapi import FastAPI,Body,Path,Query
from typing import Annotated

app = FastAPI()

fake_db = {
    "foo":{
        "name":"Foo",
        "title":"foo"
    },
    "bar":{
        "name":"Bar",
        "title":"bar"
    }
}
@app.get("/user/{u_id}")
async def read_user(u_id:str | Annotated[None,Path(max_length=3)]):
    return fake_db[u_id]

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=5)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results 




from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password,hashed_password)
    
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)
    
    @staticmethod
    def get_password_plain(hash_password):
        return pwd_context.encrypt(hash_password)
    
    @staticmethod
    def verify_password_encrypt(encrypt_password, hashed_password):
        return pwd_context.verify(encrypt_password,hashed_password)
    

# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# class Hasher():
#     @staticmethod
#     def verify_password(plain_password, hashed_password):
#         return pwd_context.verify(plain_password, hashed_password)

#     @staticmethod
#     def get_password_hash(password):
#         return pwd_context.hash(password) 