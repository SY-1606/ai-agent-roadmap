
class User:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"我是用户：{self.name}"


class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def introduce(self):
        return f"我是管理员：{self.name}，等级：{self.level}"


def main():
    user = User("Tom")
    admin = Admin("Alice", 2)

    print(user.introduce())
    print(admin.introduce())

    print(isinstance(admin, User))


if __name__ == "__main__":
    main()
