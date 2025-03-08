from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from model.role import Role
from service.status_service import StatusService

class RoleService:
    def __init__(self, database: AsyncSession):
        self.database = database


    async def get_role_by_id(self, id: int):
        role = await self.database.get(Role, id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    async def get_role_by_name(self, name: str):
        role = await self.database.get(Role, name)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    async def create_role(self, role: Role):
        status_service = StatusService(self.database)
        status = await status_service.get_status_by_id(role.status_id)

        role_db = Role(name = role.name, status_id = status.id)
        self.database.add(role_db)
        await self.database.commit()
        await self.database.refresh(role_db)
        return role_db

    async def put_role_service(self, data: dict):
        ...

    async def delete_role_service(self, data: dict):
        ...