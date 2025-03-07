from fastapi import APIRouter, HTTPException
from service import user_service

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{id}")
async def get_user(id: int):
    user = await user_service.get_user_service(id)
    return user

@router.post("/")
async def create_user(data: dict):
    user = await user_service.create_user_service(data)
    return HTTPException(status_code=201, detail=user.dict())

@router.put("/{id}")
async def update_user(id: int, data: dict):
    user = await user_service.update_user_service(id, data)
    return HTTPException(status_code=204, detail=user.dict())

@router.delete("/{id}")
async def delete_user(id: int):
    user = await user_service.delete_user_service(id)
    return HTTPException(status_code=204, detail=user.dict())
