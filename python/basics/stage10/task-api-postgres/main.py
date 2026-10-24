
from contextlib import asynccontextmanager
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, Task
from schemas import TaskCreate, TaskResponse, TaskUpdate


# 应用启动时创建尚不存在的表
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Task API with PostgreSQL",
    description="Python Stage 10 - SQLAlchemy ORM",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "message": "Task API with PostgreSQL",
        "database": "PostgreSQL",
        "orm": "SQLAlchemy",
    }


# 查询任务列表，支持筛选、搜索和分页
@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    done: bool | None = None,
    priority: Literal["high", "medium", "low"] | None = None,
    keyword: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    statement = select(Task)

    if done is not None:
        statement = statement.where(Task.done == done)

    if priority is not None:
        statement = statement.where(
            Task.priority == priority
        )

    if keyword:
        statement = statement.where(
            Task.title.contains(keyword)
        )

    statement = (
        statement
        .order_by(Task.id.desc())
        .limit(limit)
        .offset(offset)
    )

    tasks = db.scalars(statement).all()
    return tasks


# 搜索接口
@app.get("/tasks/search", response_model=list[TaskResponse])
def search_tasks(
    keyword: str = Query(min_length=1),
    db: Session = Depends(get_db),
):
    statement = (
        select(Task)
        .where(Task.title.contains(keyword))
        .order_by(Task.id.desc())
    )

    return db.scalars(statement).all()


# 按主键获取任务
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


# 新建任务
@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201,
)
def create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
):
    task = Task(
        title=data.title,
        priority=data.priority,
        done=False,
    )

    db.add(task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(task)

    return task


# 完整更新任务
@app.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    task.title = data.title
    task.priority = data.priority
    task.done = data.done

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(task)

    return task


# 删除任务
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    db.delete(task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "message": "任务删除成功",
        "task_id": task_id,
    }
