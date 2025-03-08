from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    status_id: int = Field(foreign_key="status.id")
    created: datetime = datetime.now()
    updated: datetime = datetime.now()
