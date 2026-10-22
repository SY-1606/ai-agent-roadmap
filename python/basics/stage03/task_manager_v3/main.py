
from task_service import (
    add_task,
    complete_task,
    delete_task,
    search_tasks,
)
from ui import show_menu, show_tasks


def read_number(prompt):
    text = input(prompt).strip()

    if not text.isdigit():
        return None

    return int(text)


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("请选择：").strip()

        if choice == "1":
            title = input("任务名称：").strip()
            priority = input(
                "优先级(high/medium/low)："
            ).strip().lower()

            if priority not in ("high", "medium", "low"):
                priority = "medium"

            task = add_task(tasks, title, priority)

            if task is None:
                print("任务名称不能为空")
            else:
                print("任务添加成功")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("完成哪个任务：")

            if number is None:
                print("请输入有效编号")
            elif complete_task(tasks, number):
                print("任务已完成")
            else:
                print("任务编号不存在")

        elif choice == "4":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("删除哪个任务：")

            if number is None:
                print("请输入有效编号")
                continue

            removed = delete_task(tasks, number)

            if removed is None:
                print("任务编号不存在")
            else:
                print(f"已删除：{removed['title']}")

        elif choice == "5":
            keyword = input("搜索关键词：").strip()

            if not keyword:
                print("搜索关键词不能为空")
                continue

            results = search_tasks(tasks, keyword)
            show_tasks(results)

        elif choice == "6":
            print("退出任务管理器")
            break

        else:
            print("无效选项")


if __name__ == "__main__":
    main()
