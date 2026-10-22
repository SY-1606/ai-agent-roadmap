
import json
from dataclasses import asdict
from pathlib import Path

from models import Task


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "tasks.json"


def save_tasks(tasks):
    """将 Task 对象列表保存为 JSON。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    data = [asdict(task) for task in tasks]

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


def load_tasks():
    """从 JSON 恢复 Task 对象列表。"""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, UnicodeError) as e:
        raise ValueError(f"JSON 数据格式错误：{e}") from e

    if not isinstance(data, list):
        raise ValueError("任务数据必须是列表")

    tasks = []

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("任务数据格式不正确")

        try:
            task = Task(**item)
        except (TypeError, ValueError) as e:
            raise ValueError(f"任务记录不合法：{e}") from e

        tasks.append(task)

    return tasks
