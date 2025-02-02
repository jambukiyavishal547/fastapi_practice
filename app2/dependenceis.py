from typing import Annotated

from fastapi import Header, HTTPException

async def get_token_header(x_token:Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(
            status_code=400, 
            detail="x-token header invalid"
        )
    
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=400,
            detail="no jessica token provided"
        ) 