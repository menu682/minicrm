from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from model import Role, Status

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstName: str
    lastName: str
    phone: str
    role_id: int = Field(foreign_key="role.id")
    status_id: int = Field(foreign_key="status.id")
    created: datetime = datetime.now()
    updated: datetime = datetime.now()

