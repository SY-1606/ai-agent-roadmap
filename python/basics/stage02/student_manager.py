
# Python Stage 02 - Student Manager
# 要求的四项功能：列出学生、计算平均分、查找最高分、搜索指定学生。

students = [
    {"name": "Tom", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 76}
]

print("===== 学生成绩管理 =====")

# 显示全部学生
print("\n所有学生：")
for index, student in enumerate(students, start=1):
    print(f"{index}. {student['name']} - {student['score']}分")

# 计算平均分
total = 0

for student in students:
    total += student["score"]

average = total / len(students)

print(f"\n平均分：{average:.2f}")

# 查找最高分
top_student = students[0]

for student in students:
    if student["score"] > top_student["score"]:
        top_student = student

print(
    f"最高分：{top_student['name']} "
    f"- {top_student['score']}分"
)

# 搜索学生
keyword = input("\n请输入要搜索的学生姓名：").strip()

found = False

for student in students:
    if student["name"].lower() == keyword.lower():
        print(f"找到学生：{student}")
        found = True
        break

if not found:
    print("没有找到该学生")
