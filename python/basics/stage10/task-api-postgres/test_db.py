
from sqlalchemy import select

from database import SessionLocal, engine
from models import Base, Task


def main():
    # 确保表存在
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        # CREATE
        task = Task(
            title="学习SQLAlchemy ORM",
            priority="high",
            done=False,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        task_id = task.id

        print("新增任务：")
        print(task.id, task.title, task.done)

        # READ
        statement = select(Task).where(
            Task.id == task_id
        )

        found = db.scalar(statement)

        print("\n查询任务：")
        print(found.id, found.title)

        # UPDATE
        found.done = True
        db.commit()
        db.refresh(found)

        print("\n修改任务：")
        print(found.id, found.done)

        # DELETE
        db.delete(found)
        db.commit()

        print("\n删除后查询：")
        print(db.get(Task, task_id))


if __name__ == "__main__":
    main()
