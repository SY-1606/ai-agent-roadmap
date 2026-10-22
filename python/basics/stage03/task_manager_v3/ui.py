
def show_menu():
    print("\n===== Task Manager V0.3 =====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("5. 搜索任务")
    print("6. 退出")


def show_tasks(tasks):
    if not tasks:
        print("暂无任务")
        return

    for index, task in enumerate(tasks, start=1):
        status = "已完成" if task["done"] else "未完成"
        print(
            f"{index}. {task['title']} "
            f"| {task['priority']} | {status}"
        )
