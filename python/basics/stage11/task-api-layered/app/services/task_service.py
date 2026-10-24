
from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories import task_repository


ALLOWED_PRIORITIES = {"high", "medium", "low"}


def validate_task(
    title: str,
    priority: str,
) -> str:
    title = title.strip()

    if not title:
        raise ValueError("任务标题不能为空")

    if priority not in ALLOWED_PRIORITIES:
        raise ValueError("优先级不合法")

    return title


def list_tasks(
    db: Session,
    done: bool | None = None,
    priority: str | None = None,
) -> list[Task]:
    if (
        priority is not None
        and priority not in ALLOWED_PRIORITIES
    ):
        raise ValueError("优先级不合法")

    return task_repository.list_tasks(
        db,
        done=done,
        priority=priority,
    )


def get_task(
    db: Session,
    task_id: int,
) -> Task | None:
    return task_repository.get_task_by_id(
        db,
        task_id,
    )


def search_tasks(
    db: Session,
    keyword: str,
) -> list[Task]:
    keyword = keyword.strip()

    if not keyword:
        raise ValueError("搜索关键词不能为空")

    return task_repository.search_tasks(
        db,
        keyword,
    )


def create_task(
    db: Session,
    title: str,
    priority: str,
) -> Task:
    title = validate_task(title, priority)

    return task_repository.create_task(
        db,
        title,
        priority,
    )


def update_task(
    db: Session,
    task_id: int,
    title: str,
    priority: str,
    done: bool,
) -> Task | None:
    task = task_repository.get_task_by_id(
        db,
        task_id,
    )

    if task is None:
        return None

    title = validate_task(title, priority)

    task.title = title
    task.priority = priority
    task.done = done

    return task_repository.update_task(
        db,
        task,
    )


def complete_task(
    db: Session,
    task_id: int,
) -> Task | None:
    task = task_repository.get_task_by_id(
        db,
        task_id,
    )

    if task is None:
        return None

    if task.done:
        return task

    task.done = True

    return task_repository.update_task(
        db,
        task,
    )


def delete_task(
    db: Session,
    task_id: int,
) -> bool:
    task = task_repository.get_task_by_id(
        db,
        task_id,
    )

    if task is None:
        return False

    task_repository.delete_task(db, task)

    return True
