from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str | str = "USER"
    status: str | str = "ACTIVE"
    created: datetime = datetime.now()
    updated: datetime = datetime.now()
