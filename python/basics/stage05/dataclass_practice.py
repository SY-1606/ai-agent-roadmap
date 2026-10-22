
from dataclasses import dataclass, asdict
import json


@dataclass
class Book:
    title: str
    author: str
    price: float

    def discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("折扣百分比不合法")

        self.price *= 1 - percent / 100


def main():
    book = Book("Python入门", "Tom", 100)

    print("原对象：", book)

    book.discount(20)
    print("打折后：", book)

    data = asdict(book)
    print("字典：", data)

    text = json.dumps(data, ensure_ascii=False, indent=2)
    print("JSON：", text)

    restored_data = json.loads(text)
    restored_book = Book(**restored_data)

    print("恢复的对象：", restored_book)


if __name__ == "__main__":
    main()
