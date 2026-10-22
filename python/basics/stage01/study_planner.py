#CLI 学习计划生成器  CLI（Command Line Interface）即命令行界面。
#优先处理用户输入的异常情况，确保程序的健壮性。

print("===== AI 学习计划生成器 =====")

name = input("请输入姓名：")
hours = float(input("每天可以学习多少小时："))

print("请选择学习方向：")
print("1. Python 基础")
print("2. 后端开发")
print("3. Agent 开发")

choice = input("请输入编号：")

if hours < 0 or hours > 24:
    print("学习时间输入错误")
elif choice != "1" and choice != "2" and choice != "3":
    print("学习方向选择错误")
else:
    print(f"\n{name}，你的学习建议如下：")

    if hours < 1:
        print("每天先保证 30~60 分钟连续学习")
    elif hours < 2:
        print("每天学习知识 1 小时，练习代码 30 分钟")
    else:
        print("每天学习知识 1 小时，项目实操 1 小时")

    if choice == "1":
        print("重点：Python 语法、函数、数据结构")
    elif choice == "2":
        print("重点：HTTP、FastAPI、数据库")
    else:
        print("重点：LLM、RAG、Tool Calling")
