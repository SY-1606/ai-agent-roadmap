#功能：输入姓名和成绩，输出成绩等级。

#要求高的条件放在前面

name = input("请输入姓名：")
score = float(input("请输入成绩："))

if score < 0 or score > 100:
    print("成绩输入错误")
elif score >= 90:
    print(f"{name} 的成绩等级是：优秀")
elif score >= 80:
    print(f"{name} 的成绩等级是：良好")
elif score >= 60:
    print(f"{name} 的成绩等级是：及格")
else:
    print(f"{name} 的成绩等级是：不及格")
