
# Python Stage 02 - Skill Deduplication

text = input("请输入技能，用逗号分隔：")

skills = text.split(",")

unique_skills = []
seen = set()

for skill in skills:
    skill = skill.strip()

    if not skill:
        continue

    key = skill.lower()

    if key not in seen:
        seen.add(key)
        unique_skills.append(skill)

print("\n去重结果：")

for skill in unique_skills:
    print(skill)
