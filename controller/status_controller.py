from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from model.status import Status
from DB import get_database
from service.status_service import StatusService

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/{status_id}")
async def get_status(status_id: int, db: AsyncSession = Depends(get_database)):
    status_service = StatusService(db)
    status = await status_service.get_status_by_id(status_id)
    return HTTPException(status_code=200, detail=status)


@router.post("/")
async def create_status(status: Status, db: AsyncSession = Depends(get_database)):
    status_service = StatusService(db)
    status = await status_service.create_status_service(status)
    return HTTPException(status_code=201, detail=status.dict())

