
from task_service import (
    add_task,
    complete_task,
    delete_task,
    search_tasks,
)
from storage import load_tasks, save_tasks
from ui import show_menu, show_tasks


def read_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")


def persist(tasks):
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
        print("请检查数据文件，程序不会覆盖原数据。")
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

            try:
                task = add_task(tasks, title, priority)
            except ValueError as e:
                print(f"添加失败：{e}")
            else:
                if persist(tasks):
                    print(f"添加成功：{task['title']}")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("完成哪个任务：")

            if complete_task(tasks, number):
                if persist(tasks):
                    print("任务已完成")
            else:
                print("编号不存在")

        elif choice == "4":
            show_tasks(tasks)

            if not tasks:
                continue

            number = read_number("删除哪个任务：")
            removed = delete_task(tasks, number)

            if removed is None:
                print("编号不存在")
            else:
                if persist(tasks):
                    print(f"已删除：{removed['title']}")

        elif choice == "5":
            keyword = input("搜索关键词：").strip()

            if not keyword:
                print("关键词不能为空")
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
