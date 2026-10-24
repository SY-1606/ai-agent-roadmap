
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task


def list_tasks(
    db: Session,
    done: bool | None = None,
    priority: str | None = None,
) -> list[Task]:
    statement = select(Task)

    if done is not None:
        statement = statement.where(Task.done == done)

    if priority is not None:
        statement = statement.where(
            Task.priority == priority
        )

    statement = statement.order_by(Task.id.desc())

    return list(db.scalars(statement).all())


def get_task_by_id(
    db: Session,
    task_id: int,
) -> Task | None:
    return db.get(Task, task_id)


def search_tasks(
    db: Session,
    keyword: str,
) -> list[Task]:
    statement = (
        select(Task)
        .where(Task.title.contains(keyword))
        .order_by(Task.id.desc())
    )

    return list(db.scalars(statement).all())


def create_task(
    db: Session,
    title: str,
    priority: str,
) -> Task:
    task = Task(
        title=title,
        priority=priority,
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


def update_task(
    db: Session,
    task: Task,
) -> Task:
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(task)
    return task


def delete_task(
    db: Session,
    task: Task,
) -> None:
    db.delete(task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise
