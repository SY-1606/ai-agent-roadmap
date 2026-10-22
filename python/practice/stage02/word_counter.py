# Python Stage 02 - Word Counter

text = input("请输入一段英文：").strip().lower()

words = text.split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print("\n单词出现次数：")

for word, count in counts.items():
    print(f"{word}: {count}")
