
def create_task(title, priority="medium"):
    """创建一条任务数据。"""
    return {
        "title": title,
        "priority": priority,
        "done": False,
    }


def add_task(tasks, title, priority="medium"):
    """向任务列表添加任务。"""
    if not title.strip():
        return None

    task = create_task(title.strip(), priority)
    tasks.append(task)
    return task


def complete_task(tasks, number):
    """完成指定编号的任务。"""
    index = number - 1

    if not 0 <= index < len(tasks):
        return False

    tasks[index]["done"] = True
    return True


def delete_task(tasks, number):
    """删除指定编号任务。"""
    index = number - 1

    if not 0 <= index < len(tasks):
        return None

    return tasks.pop(index)


def search_tasks(tasks, keyword):
    """根据任务标题搜索。"""
    keyword = keyword.strip().lower()

    results = []

    for task in tasks:
        if keyword in task["title"].lower():
            results.append(task)

    return results
