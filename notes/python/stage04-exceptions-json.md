# Python 第四关：异常处理、文件读写、JSON 与数据持久化

## 1. 学习目标

掌握 Python 的异常处理、文本文件读写和 JSON 数据存储，让程序在输入错误时不轻易崩溃，并在重启后恢复数据。

主要知识点：

- `try / except / else / finally`
- `raise`
- `with open()`
- 文件模式 `r / w / a / x`
- `json.dump / json.load`
- `json.dumps / json.loads`
- `pathlib.Path`
- 输入校验 Validation
- 数据持久化 Persistence

## 2. 异常处理

异常（Exception）是程序执行过程中发生的异常情况。

例如：

```python
number = int("abc")
```

会抛出 `ValueError`。

使用 `try / except`：

```python
try:
    age = int(input("请输入年龄："))
except ValueError:
    print("年龄必须是整数")
else:
    print(f"年龄：{age}")
finally:
    print("处理结束")
```

- `try`：尝试执行代码
- `except`：捕获指定异常
- `else`：没有异常时执行
- `finally`：退出这个处理结构时通常都会执行，包括发生异常时

### 常见异常

| 异常 | 原因 |
|---|---|
| ValueError | 数值或格式不合法 |
| TypeError | 类型不匹配 |
| IndexError | 列表下标越界 |
| KeyError | 字典键不存在 |
| FileNotFoundError | 文件不存在 |
| ZeroDivisionError | 除数为零 |
| json.JSONDecodeError | JSON 格式不合法 |

推荐明确捕获预期异常，避免无条件使用 `except: pass`。

## 3. 主动抛出异常 raise

```python
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能小于 0")
    return age
```

使用：

```python
try:
    check_age(-1)
except ValueError as e:
    print(e)
```

`as e` 可以取得异常对象。

## 4. 安全整数输入

```python
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")
```

循环直到得到合法整数。

## 5. 文件读写

文件打开模式：

| 模式 | 作用 |
|---|---|
| r | 读取 |
| w | 写入并覆盖原文件 |
| a | 在末尾追加 |
| x | 创建新文件，已存在则报错 |

建议使用 `with open()`，自动关闭文件。

### 写入

```python
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("你好，Python")
```

### 读取

```python
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

### 追加

```python
with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("\n第二行")
```

### 逐行读取

```python
with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

注意：`w` 会清空原文件内容，应避免误覆盖重要文件。

## 6. JSON 基础

JSON 全称 JavaScript Object Notation，是一种常用的数据交换格式。

示例：

```json
{
  "name": "Tom",
  "age": 20,
  "active": true,
  "skills": ["Python", "Git"]
}
```

Python 与 JSON 存在对应关系：

| Python | JSON |
|---|---|
| dict | object |
| list | array |
| True | true |
| False | false |
| None | null |

JSON 不等于 Python 字典，但二者可以相互转换。

## 7. 四个 JSON 函数

| 函数 | 作用 |
|---|---|
| json.dumps() | Python 对象转 JSON 字符串 |
| json.loads() | JSON 字符串转 Python 对象 |
| json.dump() | 将 Python 对象写入 JSON 文件 |
| json.load() | 从 JSON 文件读取 Python 对象 |

记忆方法：带 `s` 的主要处理字符串。

### 字符串转换

```python
import json

user = {"name": "小明", "age": 20}

text = json.dumps(user, ensure_ascii=False, indent=2)

print(text)

restored = json.loads(text)
```

### 文件写入

```python
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=2)
```

### 文件读取

```python
with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)
```

`ensure_ascii=False` 可以让中文直接保存为可读字符；`indent=2` 控制缩进。

## 8. pathlib.Path

使用 `Path` 管理文件路径：

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "tasks.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
```

`__file__` 是当前 Python 文件的位置。

这样从不同工作目录运行时，也能稳定找到项目自己的数据文件。

## 9. 数据持久化

数据持久化（Persistence）是指程序退出后，数据依然可以保留并恢复。

任务管理器工作流程：

1. 程序启动，读取 JSON。
2. 将任务加载到列表。
3. 用户添加、删除或完成任务。
4. 将修改保存到 JSON。
5. 下次启动时重新读取。

JSON 文件适用于本地小项目。多人并发访问、复杂查询等场景通常更适合数据库。

## 10. 输入校验

```python
def validate_priority(priority):
    allowed = {"high", "medium", "low"}
    return priority in allowed
```

不能直接相信用户输入。

错误的输入应得到明确提示，而不是悄悄保存成无效数据。

## 11. Agent 与 JSON

Agent 消息可以保存为：

```json
[
  {
    "role": "user",
    "content": "你好"
  },
  {
    "role": "assistant",
    "content": "你好，有什么可以帮助你？"
  }
]
```

程序重启后读取文件，就能恢复历史消息。

这属于最基础的 Conversation Memory（会话记忆），不是完整的长期 Agent Memory 系统。

## 12. 安全注意事项

- 不要把 API Key 写入公开仓库。
- `.env` 文件应加入 `.gitignore`。
- 真实聊天记录可能包含个人信息，不应随意公开。
- JSON 文件内容可能损坏，读取时要处理相关异常。
- 不要在 JSON 解析失败时直接覆盖原文件；先报告错误并保留原始数据。

## 13. 本关项目

- [ ] 异常处理练习
- [ ] 文本文件读写
- [ ] JSON 序列化练习
- [ ] Task Manager JSON 持久化
- [ ] Chat Memory V0.1
- [ ] JSON 学生成绩系统
- [ ] 读取 JSON 配置文件
- [ ] 测试所有项目
- [ ] Pull Request 合并 main

## 14. 自测

**Q1：ValueError 与 FileNotFoundError 有什么区别？**

前者常表示值或转换格式不合法，后者表示要读取的文件不存在。

**Q2：为什么推荐 with open？**

因为代码块结束时会自动关闭文件。

**Q3：w 与 a 有什么区别？**

w 覆盖，a 追加。

**Q4：json.load 与 json.loads 有什么区别？**

load 从文件对象读取，loads 解析 JSON 字符串。

**Q5：什么是持久化？**

程序结束后，数据仍可以保留并在之后恢复。

**Q6：为什么 JSON 文件不适合复杂的多用户后端系统？**

文件本身缺乏数据库提供的事务、并发控制和复杂查询等能力。

## 15. 验收标准

能正确处理非法输入，独立读写文本和 JSON 文件，完成 Task Manager 数据持久化，并使 Chat Memory 在程序重启后恢复历史消息。