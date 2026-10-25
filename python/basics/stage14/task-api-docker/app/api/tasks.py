from typing import Literal

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)
from app.services import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


# GET /tasks
@router.get(
    "",
    response_model=list[TaskResponse],
)
def get_tasks(
    done: bool | None = None,
    priority: Literal["high", "medium", "low"] | None = None,
    db: Session = Depends(get_db),
):
    return task_service.list_tasks(
        db,
        done=done,
        priority=priority,
    )


# GET /tasks/search?keyword=Python
# 固定路径放在动态路径前面
@router.get(
    "/search",
    response_model=list[TaskResponse],
)
def search_tasks(
    keyword: str = Query(min_length=1),
    db: Session = Depends(get_db),
):
    try:
        return task_service.search_tasks(
            db,
            keyword,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        ) from e


# GET /tasks/{task_id}
@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = task_service.get_task(
        db,
        task_id,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


# POST /tasks
@router.post(
    "",
    response_model=TaskResponse,
    status_code=201,
)
def create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
):
    try:
        return task_service.create_task(
            db,
            data.title,
            data.priority,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        ) from e


# PUT /tasks/{task_id}
@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
):
    try:
        task = task_service.update_task(
            db,
            task_id,
            data.title,
            data.priority,
            data.done,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        ) from e

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


# PATCH /tasks/{task_id}/complete
@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse,
)
def complete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = task_service.complete_task(
        db,
        task_id,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return task


# DELETE /tasks/{task_id}
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    success = task_service.delete_task(
        db,
        task_id,
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="任务不存在",
        )

    return {
        "message": "删除成功",
        "task_id": task_id,
    }
