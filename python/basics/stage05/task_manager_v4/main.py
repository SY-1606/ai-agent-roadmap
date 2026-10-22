
from service import (
    add_task,
    complete_task,
    delete_task,
    search_tasks,
)
from storage import load_tasks, save_tasks


def show_menu():
    print("\n===== Task Manager V0.4 =====")
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
        print(f"{index}. {task.show()}")


def read_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")


def save_changes(tasks):
    try:
        save_tasks(tasks)
    except OSError as e:
        print(f"保存失败：{e}")
        return False

    return True


def main():
    try:
        tasks = load_tasks()
    except (OSError, ValueError) as e:
        print(f"加载失败：{e}")
        print("请先检查数据文件，程序不会覆盖原数据")
        return

    print(f"已加载 {len(tasks)} 个任务")

    while True:
        show_menu()
        choice = input("请选择：").strip()

        if choice == "1":
            title = input("任务名称：").strip()
            priority = input(
                "优先级(high/medium/low)："
            ).strip().lower()

            if not priority:
                priority = "medium"

            try:
                task = add_task(tasks, title, priority)
            except ValueError as e:
                print(f"添加失败：{e}")
            else:
                if save_changes(tasks):
                    print(f"已添加：{task.title}")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("完成哪个任务：")

            if complete_task(tasks, number):
                if save_changes(tasks):
                    print("任务已完成")
            else:
                print("任务编号不存在")

        elif choice == "4":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("删除哪个任务：")
            removed = delete_task(tasks, number)

            if removed is None:
                print("任务编号不存在")
            else:
                if save_changes(tasks):
                    print(f"已删除：{removed.title}")

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
            print("无效选项，请重新输入")


if __name__ == "__main__":
    main()
