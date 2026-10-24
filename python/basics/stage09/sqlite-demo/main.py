
from database import (
    create_table,
    add_task,
    get_tasks,
    get_task,
    complete_task,
    delete_task,
    search_tasks,
    get_pending_tasks,
    list_tasks,
)


def main():
    create_table()
    print("===== SQLite 数据库练习 =====")

    # 插入数据
    id1 = add_task("学习SQLite", "high")
    id2 = add_task("学习FastAPI", "medium")
    id3 = add_task("学习Python SQL", "high")

    print("\n1. 新增的任务 ID：")
    print(id1, id2, id3)

    # 查询全部
    print("\n2. 查询所有任务：")
    for task in get_tasks():
        print(task)

    # 根据 ID 查询
    print("\n3. 按 ID 查询：")
    print(get_task(id1))

    # 修改
    print("\n4. 完成一条任务：")
    print("修改成功：", complete_task(id1))
    print(get_task(id1))

    # WHERE + LIKE
    print("\n5. 搜索 Python：")
    for task in search_tasks("Python"):
        print(task)

    # WHERE done = 0
    print("\n6. 未完成任务：")
    for task in get_pending_tasks():
        print(task)

    # ORDER BY + LIMIT + OFFSET
    print("\n7. 分页查询：")
    for task in list_tasks(limit=2, offset=0):
        print(task)

    # 删除
    print("\n8. 删除任务：")
    print("删除成功：", delete_task(id2))

    print("\n9. 最终全部任务：")
    for task in get_tasks():
        print(task)


if __name__ == "__main__":
    main()
