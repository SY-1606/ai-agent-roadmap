
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "messages.json"


def load_messages():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        messages = json.load(file)

    if not isinstance(messages, list):
        raise ValueError("消息数据必须是列表")

    for message in messages:
        if (
            not isinstance(message, dict)
            or message.get("role") not in ("user", "assistant")
            or not isinstance(message.get("content"), str)
        ):
            raise ValueError("消息结构不合法")

    return messages


def save_messages(messages):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            messages,
            file,
            ensure_ascii=False,
            indent=2,
        )


def main():
    try:
        messages = load_messages()
    except (OSError, ValueError, UnicodeError) as e:
        print(f"历史消息加载失败：{e}")
        return

    print("===== Chat Memory V0.1 =====")
    print("输入 exit 退出")

    if messages:
        print("\n===== 历史消息 =====")

        for message in messages:
            print(f"{message['role']}: {message['content']}")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        reply = f"你刚才说的是：{user_input}"

        messages.append({
            "role": "user",
            "content": user_input,
        })

        messages.append({
            "role": "assistant",
            "content": reply,
        })

        try:
            save_messages(messages)
        except OSError as e:
            print(f"消息保存失败：{e}")
        else:
            print("Assistant:", reply)


if __name__ == "__main__":
    main()
