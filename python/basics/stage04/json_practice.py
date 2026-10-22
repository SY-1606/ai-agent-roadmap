
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "user.json"


def main():
    user = {
        "name": "小明",
        "age": 20,
        "is_student": True,
        "skills": ["Python", "Git", "FastAPI"],
    }

    # Python 对象 -> JSON 字符串
    json_text = json.dumps(
        user,
        ensure_ascii=False,
        indent=2,
    )
    print("===== JSON 字符串 =====")
    print(json_text)

    # JSON 字符串 -> Python 对象
    restored = json.loads(json_text)
    print("恢复的姓名：", restored["name"])

    # Python 对象 -> JSON 文件
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            user,
            file,
            ensure_ascii=False,
            indent=2,
        )

    # JSON 文件 -> Python 对象
    with DATA_FILE.open("r", encoding="utf-8") as file:
        loaded_user = json.load(file)

    print("===== 从文件读取 =====")
    print(loaded_user)


if __name__ == "__main__":
    main()
