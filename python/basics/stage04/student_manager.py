
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "students.json"


def load_students():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        students = json.load(file)

    if not isinstance(students, list):
        raise ValueError("学生数据必须是列表")

    for student in students:
        if (
            not isinstance(student, dict)
            or not isinstance(student.get("name"), str)
            or not isinstance(student.get("score"), (int, float))
            or isinstance(student.get("score"), bool)
            or not 0 <= student["score"] <= 100
        ):
            raise ValueError("学生数据结构不合法")

    return students


def save_students(students):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            students,
            file,
            ensure_ascii=False,
            indent=2,
        )


def read_score():
    while True:
        try:
            score = float(input("请输入成绩："))
        except ValueError:
            print("请输入数字")
            continue

        if 0 <= score <= 100:
            return score

        print("成绩必须在 0 到 100 之间")


def main():
    try:
        students = load_students()
    except (OSError, ValueError, UnicodeError) as e:
        print(f"学生数据加载失败：{e}")
        return

    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 查看学生")
        print("3. 搜索学生")
        print("4. 删除学生")
        print("5. 退出")

        choice = input("请选择：").strip()

        if choice == "1":
            name = input("学生姓名：").strip()

            if not name:
                print("姓名不能为空")
                continue

            score = read_score()

            students.append({
                "name": name,
                "score": score,
            })

            try:
                save_students(students)
                print("添加成功")
            except OSError as e:
                print(f"保存失败：{e}")

        elif choice == "2":
            if not students:
                print("暂无学生")

            for index, student in enumerate(students, start=1):
                print(
                    f"{index}. {student['name']}: "
                    f"{student['score']}"
                )

        elif choice == "3":
            keyword = input("请输入姓名：").strip().lower()

            results = [
                student
                for student in students
                if keyword in student["name"].lower()
            ]

            if not results:
                print("未找到学生")
            else:
                for student in results:
                    print(student)

        elif choice == "4":
            if not students:
                print("暂无学生")
                continue

            for index, student in enumerate(students, start=1):
                print(f"{index}. {student['name']}")

            try:
                number = int(input("删除学生编号："))
            except ValueError:
                print("请输入整数")
                continue

            index = number - 1

            if 0 <= index < len(students):
                removed = students.pop(index)

                try:
                    save_students(students)
                    print(f"已删除：{removed['name']}")
                except OSError as e:
                    print(f"保存失败：{e}")
            else:
                print("编号不存在")

        elif choice == "5":
            print("程序结束")
            break

        else:
            print("无效选项")


if __name__ == "__main__":
    main()
