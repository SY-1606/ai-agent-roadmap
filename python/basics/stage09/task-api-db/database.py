
import sqlite3
from contextlib import closing
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "tasks.db"


def get_connection():
    connection = sqlite3.connect(
        DATABASE_FILE,
        timeout=10,
    )

    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    priority TEXT NOT NULL
                        DEFAULT 'medium'
                        CHECK (
                            priority IN ('high', 'medium', 'low')
                        ),
                    done INTEGER NOT NULL
                        DEFAULT 0
                        CHECK (done IN (0, 1))
                )
            """)


def list_tasks(done=None, limit=20, offset=0):
    sql = "SELECT * FROM tasks"
    params = []

    if done is not None:
        sql += " WHERE done = ?"
        params.append(int(done))

    sql += " ORDER BY id DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    with closing(get_connection()) as connection:
        rows = connection.execute(
            sql, params
        ).fetchall()

        return [dict(row) for row in rows]


def find_task(task_id):
    with closing(get_connection()) as connection:
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

        return dict(row) if row else None


def insert_task(title, priority="medium"):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                INSERT INTO tasks (title, priority, done)
                VALUES (?, ?, 0)
                """,
                (title, priority),
            )
            task_id = cursor.lastrowid

    return find_task(task_id)


def update_task(task_id, title, priority, done):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                UPDATE tasks
                SET title = ?, priority = ?, done = ?
                WHERE id = ?
                """,
                (title, priority, int(done), task_id),
            )

            updated = cursor.rowcount > 0

    if not updated:
        return None

    return find_task(task_id)


def mark_task_done(task_id):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                UPDATE tasks
                SET done = 1
                WHERE id = ?
                """,
                (task_id,),
            )

            return cursor.rowcount > 0


def remove_task(task_id):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,),
            )

            return cursor.rowcount > 0
