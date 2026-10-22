
# 1. 基本函数与返回值
def get_level(score: float) -> str:
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"


# 2. 默认参数与关键字参数
def greet(name: str, language: str = "zh") -> str:
    if language == "zh":
        return f"你好，{name}"
    return f"Hello, {name}"


# 3. 多个返回值
def calculate(a: float, b: float) -> tuple:
    return a + b, a - b


# 4. 避免可变默认参数
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


# 5. *args
def add_all(*args):
    total = 0
    for number in args:
        total += number
    return total


# 6. **kwargs
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 7. 作用域
def increase(count: int) -> int:
    return count + 1


def main():
    print(get_level(85))
    print(greet("Tom"))
    print(greet("Alice", language="en"))

    total, difference = calculate(10, 3)
    print("和：", total, "差：", difference)

    print(add_item("Python"))
    print(add_item("Git"))

    print(add_all(1, 2, 3, 4))
    show_info(name="Tom", age=20)

    count = 0
    count = increase(count)
    print("count =", count)


if __name__ == "__main__":
    main()
