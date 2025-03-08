from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from model.status import Status

class StatusService:
    def __init__(self, database: AsyncSession):
        self.database = database

    async def get_status_by_id(self, status_id: int):
        status = await self.database.get(Status, status_id)
        if not status:
            raise HTTPException(status_code=404, detail="Not Found")
        return status

    async def get_status_by_name(self, name: str):
        status = await self.database.get(Status, name)
        if not status:
            raise HTTPException(status_code=404, detail="Not Found")
        return status


    async def create_status_service(self, status: Status):
        status_db = Status(name = status.name)
        self.database.add(status_db)
        await self.database.commit()
        await self.database.refresh(status_db)
        return status_db


    async def put_status_service(self, data: dict):
        ...

    async def delete_status_service(self, data: dict):
        ...