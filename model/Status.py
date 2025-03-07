from typing import Optional

from sqlmodel import SQLModel, Field
from datetime import datetime

class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str | str = "ACTIVE"
    created: datetime = datetime.now()
    updated: datetime = datetime.now()