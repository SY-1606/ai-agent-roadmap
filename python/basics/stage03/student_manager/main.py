
from student_service import (
    add_student,
    find_student,
    get_average,
    get_top_student,
)


def main():
    students = []

    add_student(students, "Tom", 85)
    add_student(students, "Alice", 92)
    add_student(students, "Bob", 76)

    print("===== 学生列表 =====")
    for student in students:
        print(f"{student['name']}: {student['score']}")

    average = get_average(students)
    print(f"\n平均分：{average:.2f}")

    top = get_top_student(students)
    print(f"最高分：{top['name']} - {top['score']}")

    name = input("\n搜索学生姓名：").strip()
    student = find_student(students, name)

    if student is None:
        print("未找到学生")
    else:
        print("搜索结果：", student)


if __name__ == "__main__":
    main()
