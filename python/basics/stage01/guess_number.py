#要求最多猜三次，猜错提示过大或过小。

answer = 7
success = False

print("===== 猜数字游戏 =====")
print("你有 3 次猜数字的机会")

for attempt in range(3):
    guess = int(input("请输入你猜的数字："))

    if guess == answer:
        print("恭喜猜对！")
        success = True
        break
    elif guess > answer:
        print("太大了")
    else:
        print("太小了")

    print(f"还剩 {2 - attempt} 次机会")

if not success:
    print(f"游戏结束，正确答案是 {answer}")
