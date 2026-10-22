# Python 第 1 关｜基础语法复习笔记

## 1. 本关目标

写出一个完整的命令行程序：**输入 → 变量与类型转换 → 计算 → 条件判断 → 循环 → 输出**。

- [ ] 理解变量及 `int` / `float` / `str` / `bool` / `None`
- [ ] 会用 `input()`、`print()` 和类型转换
- [ ] 会写 `if` / `elif` / `else`
- [ ] 会写 `for` / `while`、`break` / `continue`
- [ ] 能独立写出最多尝试 3 次的猜数字程序

## 2. 变量、数据类型、输入输出

```python
name = "Tom"                # str：字符串
age = 20                    # int：整数
height = 1.78               # float：浮点数
is_student = True           # bool：布尔值
result = None               # 当前没有值

print(type(age))            # <class 'int'>
print(f"{name} 今年 {age} 岁")  # f-string：将变量写进字符串
```

- `=` 是**赋值**；`==` 是**比较是否相等**。
- 变量名不能以数字开头，推荐 `student_age` 这种 `snake_case`（蛇形命名法）。
- `20` 是数字，而 `"20"` 是字符串；`"10" + "20"` 得到 `"1020"`。
- `input()` **总是返回字符串**。需要算术运算时先转换：

```python
age = int(input("请输入年龄："))
print(age + 1)
```

输入 `abc` 时 `int("abc")` 会抛出 `ValueError`（后续异常处理章节解决）。

## 3. 运算符

| 类别 | 运算符 | 含义 / 示例 |
| --- | --- | --- |
| 算术 | `+ - * /` | 加、减、乘、除；`10 / 2 == 5.0` |
| 算术 | `//` | 向下取整除法：`10 // 3 == 3` |
| 算术 | `%` | 取余：`10 % 3 == 1`；`n % 2 == 0` 判断偶数 |
| 算术 | `**` | 幂：`2 ** 3 == 8` |
| 比较 | `== != > < >= <=` | 比较后得到布尔值 |
| 逻辑 | `and` / `or` / `not` | 并且 / 或者 / 取反 |

> 补充注意：对负数来说，`//` 是**向下取整**，不是简单去掉小数部分，例如 `-10 // 3 == -4`。

## 4. 条件判断与缩进

```python
score = float(input("请输入成绩："))
if score < 0 or score > 100:
    print("成绩输入错误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

- 条件从上到下匹配；先写 `score >= 60` 会让 95 被提前判为“及格”。
- `if`、`elif`、`else` 的行末有冒号 `:`。
- 代码块一般缩进 **4 个空格**。

## 5. 循环及控制

```python
# range(1, 5) 得到 1、2、3、4（包含起点，不包含终点）
for i in range(1, 5):
    print(i)

# 累加器：计算 1 到 100 之和
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

# while：注意更新循环变量，否则可能死循环
count = 1
while count <= 3:
    print(count)
    count += 1
```

- `break`：**结束整个循环**。
- `continue`：**跳过本轮剩余代码，进入下一轮**。
- 嵌套循环：外层每执行一次，内层通常执行一轮，用于九九乘法表等。

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end=" ")
    print()  # 本行结束后换行
```

## 6. 典型易错点和调试

| 错误类型 | 常见原因 | 排查方法 |
| --- | --- | --- |
| `TypeError` | 字符串与整数直接相加 | `print(type(value))`，必要时 `int()` |
| `ValueError` | `int("abc")` 转换失败 | 检查输入是否合法 |
| `IndentationError` | `if` 后没有正确缩进 | 检查代码块的 4 空格缩进 |
| `SyntaxError` | 忘记 `:` 等语法符号 | 看报错行及前一行 |
| 死循环 | `while` 条件一直为真 | 检查变量是否更新、条件能否终止 |

简单调试方法：

```python
value = input("请输入数字：")
print("DEBUG:", value)
print("DEBUG TYPE:", type(value))
```

## 7. 本关实践项目

代码位置：`python/basics/stage01/`。

| 文件名 | 来源讲义任务 | 完成情况 |
| --- | --- | --- |
| `score.py` | 根据 0–100 分判断成绩等级 | [ ] |
| `login.py` | 用户名/密码校验，最多三次 | [ ] |
| `study_planner.py` | 根据学习时间与方向生成建议 | [ ] |
| `guess_number.py` | 猜数字，最多三次并提示大小 | [ ] |
| `multiplication_table.py` | 九九乘法表（嵌套循环） | [ ] |

**独立练习：** 判断奇偶数；三个数求最大值；九九乘法表；猜数字（最多三次）。

## 8. 自测（先答再看）

1. `=` 与 `==` 分别做什么？
2. `input()` 返回什么类型？为什么 `input(...) + 1` 可能报错？
3. `range(1, 5)` 包含哪些数？
4. `break` 与 `continue` 有何不同？
5. `while` 为什么会出现死循环？
6. `10 % 3` 等于多少？

<details>
<summary>点击查看答案</summary>

1. 赋值 / 判断是否相等。
2. `str`；字符串不能直接与整数相加。
3. `1, 2, 3, 4`。
4. 退出整个循环 / 跳过当前轮。
5. 循环条件始终为真，且没有退出途径。
6. `1`。

</details>

## 9. 与 AI Agent 学习的联系

- `if tool_name == "search"`：工具选择的条件判断。
- `for message in messages`：遍历对话消息。
- `total_tokens += usage`：统计 Token 用量。
- `prompt = f"用户问题：{question}"`：拼接 Prompt。

