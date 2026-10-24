
import sqlite3
from contextlib import closing
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_FILE)

    # 让查询结果支持 row["title"] 访问
    connection.row_factory = sqlite3.Row

    return connection


def create_table():
    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    priority TEXT NOT NULL DEFAULT 'medium',
                    done INTEGER NOT NULL DEFAULT 0
                )
            """)


def add_task(title, priority="medium"):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                INSERT INTO tasks (title, priority, done)
                VALUES (?, ?, 0)
                """,
                (title, priority),
            )
            return cursor.lastrowid


def get_tasks():
    with closing(get_connection()) as connection:
        rows = connection.execute(
            "SELECT * FROM tasks ORDER BY id ASC"
        ).fetchall()

        return [dict(row) for row in rows]


def get_task(task_id):
    with closing(get_connection()) as connection:
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

        return dict(row) if row else None


def complete_task(task_id):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                "UPDATE tasks SET done = 1 WHERE id = ?",
                (task_id,),
            )
            return cursor.rowcount > 0


def delete_task(task_id):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,),
            )
            return cursor.rowcount > 0


def search_tasks(keyword):
    with closing(get_connection()) as connection:
        rows = connection.execute(
            """
            SELECT * FROM tasks
            WHERE title LIKE ?
            ORDER BY id DESC
            """,
            (f"%{keyword}%",),
        ).fetchall()

        return [dict(row) for row in rows]


def get_pending_tasks():
    with closing(get_connection()) as connection:
        rows = connection.execute(
            """
            SELECT * FROM tasks
            WHERE done = 0
            ORDER BY id DESC
            """
        ).fetchall()

        return [dict(row) for row in rows]


def list_tasks(limit=10, offset=0):
    with closing(get_connection()) as connection:
        rows = connection.execute(
            """
            SELECT * FROM tasks
            ORDER BY id DESC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()

        return [dict(row) for row in rows]
