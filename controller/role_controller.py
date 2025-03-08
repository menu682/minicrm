from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from model.role import Role
from DB import get_database
from service.role_service import RoleService

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/{id}")
async def get_role(id: int, db: AsyncSession = Depends(get_database)):
    role_service = RoleService(db)
    role = await role_service.get_role_by_id(id)
    return role

@router.post("/")
async def create_role(role: Role, db: AsyncSession = Depends(get_database)):
    role_service = RoleService(db)
    role = await role_service.create_role(role)
    return HTTPException(status_code=201, detail=role.dict())