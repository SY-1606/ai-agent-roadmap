
def validate_priority(priority):
    return priority in {"high", "medium", "low"}


def create_task(title, priority="medium"):
    if not title.strip():
        raise ValueError("任务名称不能为空")

    if not validate_priority(priority):
        raise ValueError("优先级不合法")

    return {
        "title": title.strip(),
        "priority": priority,
        "done": False,
    }


def add_task(tasks, title, priority="medium"):
    task = create_task(title, priority)
    tasks.append(task)
    return task


def complete_task(tasks, number):
    index = number - 1

    if not 0 <= index < len(tasks):
        return False

    tasks[index]["done"] = True
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
        if keyword in task["title"].lower()
    ]
