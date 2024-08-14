from pydantic import BaseModel,EmailStr,Field 

# pydantic support dict value(key:value)
class ItemBase(BaseModel):
    title:str
    description:str | None = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id :int 
    owner_id: int

    # support only dict so tell pydantic model 
    # read data if not in dict
    # so use orm_model=true 
    class Config:
        from_attributes =True #after pydantic v2 orm_model rename 

class UserBase(BaseModel):
    email:str    #EmailStr

class UserCreate(UserBase):
    password :str

class User(UserBase):
    id :int
    is_active :bool
    items:list[Item] =  []

    class Config:
        from_attributes = True  