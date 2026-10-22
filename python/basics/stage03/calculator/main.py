
import calculator


def main():
    a = float(input("第一个数："))
    b = float(input("第二个数："))

    print("加法：", calculator.add(a, b))
    print("减法：", calculator.subtract(a, b))
    print("乘法：", calculator.multiply(a, b))

    result = calculator.divide(a, b)

    if result is None:
        print("除法：除数不能为零")
    else:
        print("除法：", result)


if __name__ == "__main__":
    main()
