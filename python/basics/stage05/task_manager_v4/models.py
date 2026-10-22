
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: str = "medium"
    done: bool = False

    def __post_init__(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("任务名称不能为空")

        self.title = self.title.strip()

        if self.priority not in ("high", "medium", "low"):
            raise ValueError("优先级必须是 high/medium/low")

        if not isinstance(self.done, bool):
            raise ValueError("完成状态必须是布尔值")

    def complete(self):
        self.done = True

    def show(self):
        status = "已完成" if self.done else "未完成"
        return f"{self.title} | {self.priority} | {status}"
