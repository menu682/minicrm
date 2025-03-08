from sqlalchemy.ext.asyncio import AsyncSession

from model.user import User
from service.role_service import RoleService
from service.status_service import StatusService

class UserService:
    def __init__(self, database: AsyncSession):
        self.database = database

    async def get_user_by_id(self, user_id: int):
        user = await self.database.get(User, user_id)
        return user

    async def create_user_service(self, user: User):
        role_service = RoleService(self.database)
        role = await role_service.get_role_by_id(user.role_id)

        status_service = StatusService(self.database)
        status = await status_service.get_status_by_id(user.status_id)

        user_db = User(first_name = user.first_name,
                       last_name = user.last_name,
                       phone = user.phone,
                       role_id = role.id,
                       status_id = status.id)
        self.database.add(user_db)
        await self.database.commit()
        await self.database.refresh(user_db)
        return user_db


    async def delete_user_service(id: int):
        ...

    async def update_user_service(id: int, data: dict):
        ...