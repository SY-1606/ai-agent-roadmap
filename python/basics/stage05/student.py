
class Student:
    school = "HIT"

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"成绩：{self.score}")

    def update_score(self, new_score):
        if not 0 <= new_score <= 100:
            raise ValueError("成绩必须在0到100之间")

        self.score = new_score

    def is_passed(self):
        return self.score >= 60


def main():
    student1 = Student("Tom", 20, 88)
    student2 = Student("Alice", 21, 95)

    student1.show_info()
    student1.update_score(96)

    print("修改后成绩：", student1.score)
    print("是否及格：", student1.is_passed())

    print("\n第二个学生：")
    student2.show_info()

    print("学校：", Student.school)


if __name__ == "__main__":
    main()
