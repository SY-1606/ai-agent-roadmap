
class Book:
    def __init__(self, title, author, price):
        if price < 0:
            raise ValueError("价格不能为负数")

        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f"书名：{self.title}")
        print(f"作者：{self.author}")
        print(f"价格：{self.price:.2f}")

    def discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("折扣百分比必须在0到100之间")

        self.price *= 1 - percent / 100


def main():
    book = Book("Python入门", "Tom", 100)

    book.show_info()
    book.discount(20)

    print("\n打折后：")
    book.show_info()


if __name__ == "__main__":
    main()
