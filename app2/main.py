from fastapi import Depends, FastAPI

from .dependenceis import get_query_token,get_token_header
from .internal import admin
from .routers import items,users

app = FastAPI(docs_url="/doc", redoc_url="/re-doc", dependencies=[Depends(get_query_token)]) 

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies= [Depends(get_token_header)],
    responses= {418:{"description":"i'm a teapot"}},
)

@app.get("/")
async def root():
    return {"message":"hello bigger application"} 
