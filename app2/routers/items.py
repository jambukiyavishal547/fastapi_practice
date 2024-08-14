from fastapi import APIRouter, Depends, HTTPException
from ..dependenceis import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={400:{"description":"not found"}},
)

fake_item_db = {"plumbus":{"name":"plumbus"}, "gun":{"name":"portal gun"}}

@router.get("/")
async def read_items():
    return fake_item_db

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_item_db:
        raise HTTPException(status_code=404, detail="item not found")
    return {"name":fake_item_db[item_id]["name"],"item_id":item_id}

@router.put(
        "/{item_id}",
        tags=["custom"], 
        responses={403:{"description":"operation forbidden"}},
    )
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403,
            detail="you can only update item:plumbus"
        )
    return {"item_id":item_id, "name":"the great plumbus"}
