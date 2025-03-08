from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from model.user import User
from DB import get_database
from service.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_database)):
    user_service = UserService(db)
    user = await user_service.get_user_by_id(user_id)
    return user

@router.post("/")
async def create_user(user: User, db: AsyncSession = Depends(get_database)):
    user_service = UserService(db)
    user = await user_service.create_user_service(user)
    return HTTPException(status_code=201, detail=user.dict())

@router.put("/{id}")
async def update_user(id: int, data: dict, db: AsyncSession = Depends(get_database)):
    user_service = UserService(db)
    user = await user_service.update_user_service(id, data)
    return HTTPException(status_code=204, detail=user.dict())

@router.delete("/{id}")
async def delete_user(id: int, db: AsyncSession = Depends(get_database)):
    user_service = UserService(db)
    user = await user_service.delete_user_service(id)
    return HTTPException(status_code=204, detail=user.dict())
