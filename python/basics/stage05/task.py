
class Task:
    def __init__(self, title, priority="medium"):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

    def show(self):
        status = "已完成" if self.done else "未完成"

        print(
            f"{self.title} | "
            f"{self.priority} | "
            f"{status}"
        )


def main():
    task1 = Task("学习Python", "high")
    task2 = Task("学习FastAPI")

    tasks = [task1, task2]

    task1.complete()

    for task in tasks:
        task.show()


if __name__ == "__main__":
    main()
