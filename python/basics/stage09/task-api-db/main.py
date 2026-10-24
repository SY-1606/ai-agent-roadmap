
from contextlib import asynccontextmanager
from typing import Literal

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from database import (
    create_table,
    list_tasks,
    find_task,
    insert_task,
    update_task,
    mark_task_done,
    remove_task,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时创建数据库表
    create_table()
    yield


app = FastAPI(
    title="Task API with SQLite",
    description="Python Stage 09 数据库持久化实战",
    version="1.0.0",
    lifespan=lifespan,
)


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    priority: Literal[
        "high", "medium", "low"
    ] = "medium"


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    priority: Literal[
        "high", "medium", "low"
    ]
    done: bool


@app.get("/")
def root():
    return {
        "message": "Task API with SQLite",
        "database": "SQLite",
    }


@app.get("/tasks")
def get_tasks(
    done: bool | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return list_tasks(
        done=done,
        limit=limit,
        offset=offset,
    )


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    return insert_task(
        title=task.title,
        priority=task.priority,
    )


@app.put("/tasks/{task_id}")
def replace_task(task_id: int, data: TaskUpdate):
    task = update_task(
        task_id=task_id,
        title=data.title,
        priority=data.priority,
        done=data.done,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    success = mark_task_done(task_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return find_task(task_id)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = remove_task(task_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return {
        "message": "任务已删除",
        "task_id": task_id,
    }
