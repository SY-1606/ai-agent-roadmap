
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FILE_PATH = DATA_DIR / "hello.txt"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # w：覆盖写入
    with FILE_PATH.open("w", encoding="utf-8") as file:
        file.write("第一行：学习 Python 文件操作\n")

    # a：追加
    with FILE_PATH.open("a", encoding="utf-8") as file:
        file.write("第二行：学习 with open\n")
        file.write("第三行：学习 JSON\n")

    # r：读取整个文件
    with FILE_PATH.open("r", encoding="utf-8") as file:
        content = file.read()

    print("===== 文件内容 =====")
    print(content)

    # 逐行读取
    print("===== 逐行读取 =====")

    with FILE_PATH.open("r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")

    print(f"文件位置：{FILE_PATH}")


if __name__ == "__main__":
    main()
