
def add_student(students, name, score):
    """添加学生，返回新学生记录。"""
    student = {"name": name, "score": score}
    students.append(student)
    return student


def find_student(students, name):
    """按姓名查找学生。"""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def get_average(students):
    """计算平均成绩；空列表返回 None。"""
    if not students:
        return None

    total = sum(student["score"] for student in students)
    return total / len(students)


def get_top_student(students):
    """返回最高分学生；空列表返回 None。"""
    if not students:
        return None

    return max(students, key=lambda student: student["score"])
