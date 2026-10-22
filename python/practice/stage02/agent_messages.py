
# Python Stage 02 - Agent Messages

messages = []

print("===== Agent Message Simulator =====")
print("输入 exit 退出")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        print("输入不能为空")
        continue

    user_message = {
        "role": "user",
        "content": user_input
    }

    messages.append(user_message)

    reply = f"你刚才说的是：{user_input}"

    assistant_message = {
        "role": "assistant",
        "content": reply
    }

    messages.append(assistant_message)

    print("Assistant:", reply)

print("\n===== 完整消息历史 =====")

for index, message in enumerate(messages, start=1):
    print(
        f"{index}. [{message['role']}] "
        f"{message['content']}"
    )
