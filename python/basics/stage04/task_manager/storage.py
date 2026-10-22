
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "tasks.json"


def load_tasks():
    """读取任务；文件不存在时返回空列表。"""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

    except (json.JSONDecodeError, UnicodeError) as e:
        raise ValueError(f"任务数据文件格式错误：{e}") from e

    if not isinstance(tasks, list):
        raise ValueError("任务数据必须是列表")

    for task in tasks:
        if (
            not isinstance(task, dict)
            or not isinstance(task.get("title"), str)
            or not isinstance(task.get("done"), bool)
            or task.get("priority") not in
            ("high", "medium", "low")
        ):
            raise ValueError("任务数据结构不合法")

    return tasks


def save_tasks(tasks):
    """将任务列表保存到 JSON 文件。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=2,
        )
