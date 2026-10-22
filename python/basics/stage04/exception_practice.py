
def read_int(prompt):
    """反复读取输入，直到获得整数。"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")


def safe_divide(a, b):
    """执行除法，处理除数为零的问题。"""
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能小于0")
    return age


def main():
    age = read_int("请输入年龄：")

    try:
        check_age(age)
    except ValueError as e:
        print(f"输入错误：{e}")
    else:
        print(f"你的年龄是：{age}")
    finally:
        print("年龄检查结束")

    try:
        a = float(input("请输入a："))
        b = float(input("请输入b："))
        print(f"计算结果：{safe_divide(a, b)}")

    except ValueError:
        print("请输入合法数字")

    except ZeroDivisionError as e:
        print(f"计算错误：{e}")


if __name__ == "__main__":
    main()
