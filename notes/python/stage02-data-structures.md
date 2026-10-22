# Python 第二关：核心数据结构

## 1. 学习目标

掌握 Python 五种核心数据结构：

- `list`：列表
- `tuple`：元组
- `dict`：字典
- `set`：集合
- `str`：字符串

重点掌握列表与字典嵌套，因为后续 FastAPI、JSON、RAG、Agent 消息处理都会大量使用。

## 2. 数据结构对比

| 类型 | 写法 | 是否可变 | 主要用途 |
|---|---|---|---|
| list | `[1, 2, 3]` | 是 | 保存有序数据 |
| tuple | `(1, 2, 3)` | 否 | 保存固定数据 |
| dict | `{"name": "Tom"}` | 是 | 保存键值对 |
| set | `{1, 2, 3}` | 是 | 去重、集合运算 |
| str | `"Python"` | 否 | 文本处理 |

注意：`set` 不支持通过下标访问。

## 3. list 列表

### 创建与访问

```python
scores = [80, 90, 70]

print(scores[0])   # 第一个
print(scores[-1])  # 最后一个
```

Python 下标从 `0` 开始。

### 增删改查

```python
scores.append(100)
scores.insert(1, 85)
scores[0] = 95
scores.remove(70)
last = scores.pop()
```

- `append(x)`：在末尾添加元素
- `insert(i, x)`：在指定位置插入
- `remove(x)`：删除第一个值为 x 的元素
- `pop(i)`：删除并返回指定位置的元素，默认最后一个

### 遍历列表

```python
names = ["Tom", "Alice"]

for name in names:
    print(name)

for index, name in enumerate(names):
    print(index, name)
```

`enumerate()` 可以同时获取元素下标和值。

### 切片

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

切片通常遵循左闭右开原则，即包含起点，不包含终点。

### 排序

```python
numbers = [5, 2, 8, 1]

numbers.sort()
new_numbers = sorted(numbers)
```

区别：

- `sort()`：直接修改原列表
- `sorted()`：返回新的排序列表

## 4. tuple 元组

```python
point = (10, 20)

x, y = point
```

元组不可变，不能直接修改其元素位置。

`x, y = point` 称为解包（Unpacking）。

注意：元组不可变指不能替换其中的元素；如果元组内部包含列表，该列表仍可以修改。

## 5. dict 字典

字典以键值对（Key-Value）组织数据。

```python
student = {
    "name": "Tom",
    "age": 20,
    "score": 88
}
```

### 访问与修改

```python
print(student["name"])

student["score"] = 95
student["city"] = "Shenzhen"

del student["age"]
```

### get 安全读取

```python
student.get("name")
student.get("age", 0)
```

如果键不存在：

- `student["age"]` 会抛出 `KeyError`
- `student.get("age")` 返回 `None`
- `student.get("age", 0)` 返回默认值 `0`

### 遍历字典

```python
for key, value in student.items():
    print(key, value)
```

### 列表嵌套字典

```python
students = [
    {"name": "Tom", "score": 85},
    {"name": "Alice", "score": 92}
]

print(students[0]["name"])
```

这是本关最重要的数据结构组合。

## 6. set 集合

```python
skills = {"Python", "Git"}

skills.add("FastAPI")
skills.discard("Git")
```

集合特点：

- 元素不重复
- 不支持数字下标访问
- 可以计算交集、并集、差集

```python
a = {"Python", "Git"}
b = {"Python", "FastAPI"}

print(a & b)  # 交集
print(a | b)  # 并集
print(a - b)  # 差集
```

如果需要保留原始顺序，不能只依赖集合去重。

## 7. str 字符串

常用方法：

| 方法 | 作用 |
|---|---|
| `lower()` | 转小写 |
| `upper()` | 转大写 |
| `strip()` | 去除首尾空白 |
| `split()` | 分割字符串 |
| `join()` | 拼接字符串 |
| `replace()` | 替换子字符串 |
| `find()` | 查找子字符串的位置 |

示例：

```python
text = " Python,FastAPI,Agent "

skills = text.strip().split(",")

print(skills)
print(",".join(skills))
```

## 8. 可变对象与引用

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

输出：

```text
[1, 2, 3, 4]
```

原因：`a` 和 `b` 引用同一个列表。

如果需要独立的浅复制：

```python
b = a.copy()
```

注意：浅复制不会递归复制内部嵌套对象。

## 9. 常见错误

| 错误 | 原因 |
|---|---|
| IndexError | 列表下标越界 |
| KeyError | 字典键不存在 |
| TypeError | 操作类型不匹配 |
| AttributeError | 对象没有对应属性或方法 |

常见示例：

```python
numbers = [1, 2, 3]
# numbers[10] 会产生 IndexError

user = {"name": "Tom"}
# user["age"] 会产生 KeyError
```

## 10. 与 AI Agent 的关系

Agent 消息通常采用列表与字典嵌套：

```python
messages = [
    {
        "role": "user",
        "content": "什么是 RAG？"
    },
    {
        "role": "assistant",
        "content": "RAG 是检索增强生成。"
    }
]
```

可以通过：

```python
for message in messages:
    print(message["role"])
    print(message["content"])
```

访问每条消息。

## 11. 第二关项目任务

- [ ] 列表操作练习
- [ ] 字典与嵌套结构练习
- [ ] 学生成绩管理
- [ ] 单词频率统计
- [ ] 技能去重
- [ ] Task Manager V0.2
- [ ] 模拟 Agent 消息系统
- [ ] 所有代码运行成功
- [ ] 使用 Git 分支开发
- [ ] 通过 Pull Request 合并 main

## 12. 自测

**Q1：list 和 tuple 有什么区别？**

list 可修改；tuple 不能替换其元素。

**Q2：`numbers[-1]` 表示什么？**

最后一个元素。

**Q3：`numbers[1:4]` 包含下标 4 吗？**

不包含。

**Q4：为什么推荐使用 `dict.get()`？**

在键不存在时可以返回默认值，避免直接触发 KeyError。

**Q5：`split()` 和 `join()` 的区别？**

split 将字符串拆分成列表，join 将字符串序列拼接成字符串。

**Q6：为什么 Agent 经常使用 list + dict？**

因为一段对话包含多条消息，每条消息又有 role、content 等多个字段。

## 13. 本关验收标准

能够独立创建并遍历列表、字典和集合，理解可变与不可变对象，并能独立实现具备增删改查功能的 CLI 任务管理器。