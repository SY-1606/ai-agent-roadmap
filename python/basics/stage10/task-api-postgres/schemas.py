
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Priority = Literal["high", "medium", "low"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: Priority = "medium"


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: Priority
    done: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    done: bool

    model_config = ConfigDict(
        from_attributes=True
    )
