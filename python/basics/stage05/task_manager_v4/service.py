
from models import Task


def add_task(tasks, title, priority="medium"):
    task = Task(title=title, priority=priority)
    tasks.append(task)
    return task


def complete_task(tasks, number):
    index = number - 1

    if not 0 <= index < len(tasks):
        return False

    tasks[index].complete()
    return True


def delete_task(tasks, number):
    index = number - 1

    if not 0 <= index < len(tasks):
        return None

    return tasks.pop(index)


def search_tasks(tasks, keyword):
    keyword = keyword.strip().lower()

    return [
        task
        for task in tasks
        if keyword in task.title.lower()
    ]
