
# Python Stage 02 - Task Manager V0.2

tasks = []

while True:
    print("\n===== Task Manager V0.2 =====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 标记任务完成")
    print("5. 搜索任务")
    print("6. 退出")

    choice = input("请选择操作：").strip()

    if choice == "1":
        title = input("任务名称：").strip()

        if not title:
            print("任务名称不能为空")
            continue

        priority = input(
            "优先级(high/medium/low)："
        ).strip().lower()

        if priority not in ["high", "medium", "low"]:
            priority = "medium"

        task = {
            "title": title,
            "done": False,
            "priority": priority
        }

        tasks.append(task)
        print("任务添加成功")

    elif choice == "2":
        if not tasks:
            print("暂无任务")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "已完成" if task["done"] else "未完成"

                print(
                    f"{index}. {task['title']} "
                    f"[{status}] "
                    f"优先级：{task['priority']}"
                )

    elif choice == "3":
        if not tasks:
            print("暂无任务")
            continue

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']}")

        number = input("请输入要删除的任务编号：").strip()

        if not number.isdigit():
            print("请输入正确的整数编号")
            continue

        index = int(number) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"已删除：{removed['title']}")
        else:
            print("任务编号不存在")

    elif choice == "4":
        if not tasks:
            print("暂无任务")
            continue

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']}")

        number = input("请输入要完成的任务编号：").strip()

        if not number.isdigit():
            print("请输入正确的整数编号")
            continue

        index = int(number) - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("任务已标记完成")
        else:
            print("任务编号不存在")

    elif choice == "5":
        keyword = input("搜索关键词：").strip().lower()

        found = False

        for index, task in enumerate(tasks, start=1):
            if keyword in task["title"].lower():
                status = "已完成" if task["done"] else "未完成"

                print(
                    f"{index}. {task['title']} "
                    f"[{status}] "
                    f"优先级：{task['priority']}"
                )

                found = True

        if not found:
            print("未找到匹配的任务")

    elif choice == "6":
        print("退出任务管理器")
        break

    else:
        print("无效选项，请重新输入")
