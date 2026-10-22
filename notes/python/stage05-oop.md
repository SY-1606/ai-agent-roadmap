# Python 第五关：面向对象 OOP

## 1. 学习目标

掌握面向对象编程（Object-Oriented Programming，OOP）的核心概念，学会使用类组织数据和行为，并通过 `dataclass` 将对象和 JSON 持久化连接起来。

## 2. 类和对象

类（Class）是创建对象的模板，对象（Object）是根据类创建的具体实例。

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

`Student` 是类，`student1` 和 `student2` 是两个不同的对象。

## 3. __init__ 与 self

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

student = Student("Tom", 20, 88)
```

- `__init__()`：新对象创建过程中自动调用的初始化方法。
- `self`：当前对象本身，调用实例方法时通常由 Python 自动传入。
- `self.name`：对象自己的属性。
- `name`：初始化方法接收到的参数。

`self.name = name` 表示把参数 `name` 保存为当前对象的 `name` 属性。

## 4. 属性和方法

属性（Attribute）保存数据；方法（Method）定义对象的行为。

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        self.score = new_score

    def is_passed(self):
        return self.score >= 60
```

调用：

```python
student = Student("Tom", 88)

student.update_score(95)
print(student.score)
print(student.is_passed())
```

注意：字典使用 `student["name"]`，对象使用 `student.name`。

## 5. 实例属性与类属性

```python
class Student:
    school = "HIT"

    def __init__(self, name):
        self.name = name
```

- `school`：类属性，通常由多个实例共享。
- `self.name`：实例属性，每个对象独立保存。

## 6. 封装 Encapsulation

封装是把相关的数据和操作放进类中，对外提供清晰的使用方式。

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True
```

调用者只需要：

```python
task.complete()
```

不需要直接管理方法内部实现。

以下划线开头的属性，例如 `self._balance`，通常表示内部使用的属性。这是一种约定，不是绝对的访问限制。

## 7. 继承 Inheritance

子类可以继承父类的方法。

```python
class Animal:
    def speak(self):
        return "动物发声"

class Dog(Animal):
    def speak(self):
        return "汪汪"
```

子类重新实现同名方法，称为方法重写（Override）。

## 8. super()

```python
class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
```

`super()` 可以按照方法解析顺序访问父类等上层类的方法。初学时可以先理解为调用父类的初始化逻辑。

## 9. dataclass

当类主要用于保存数据时，可以使用 `@dataclass` 减少重复代码。

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    priority: str = "medium"
    done: bool = False

    def complete(self):
        self.done = True
```

`@dataclass` 会自动生成 `__init__()`、`__repr__()` 等常用方法。

这里的 `@` 是装饰器（Decorator）语法。

## 10. 对象与 JSON

Python 的 JSON 模块不能直接序列化普通自定义对象。

对于 dataclass，可以使用 `asdict()`：

```python
from dataclasses import asdict

task = Task("学习Python", "high")

data = asdict(task)
```

把字典重新变成对象：

```python
restored = Task(**data)
```

`**data` 会把字典展开为关键字参数。

整体流程：

Task 对象 → dict → JSON 文件 → dict → Task 对象

## 11. 什么时候使用类？

当程序只有简单的输入、计算和输出时，函数通常足够。

当某个事物具有自己的属性、可变化的状态，以及多个相关操作时，可以考虑定义类。

例如任务有：

- title：标题
- priority：优先级
- done：完成状态
- complete()：标记完成的方法

这种情况适合使用 Task 类。

## 12. 常见错误

**忘记 self：**

实例方法应通常写为：

```python
def show_info(self):
    ...
```

**属性未保存到 self：**

错误：

```python
name = name
```

正确：

```python
self.name = name
```

**对象和字典混淆：**

字典使用 `task["title"]`，Task 对象使用 `task.title`。

**忘记创建对象：**

定义 `class Student` 不会自动创建学生实例，需要调用 `Student(...)`。

## 13. 与 AI Agent 开发的关系

未来会遇到：

```python
agent = Agent(...)
agent.run(...)
```

其中 Agent 是类，agent 是对象，run 是方法。

OOP 同样广泛应用于 API SDK、ORM 数据模型、后端服务和有状态的 Agent 系统。

## 14. 本关任务

- [ ] Student 类
- [ ] Task 类
- [ ] Book 类
- [ ] BankAccount 类
- [ ] 继承与 super 练习
- [ ] dataclass 与 asdict 练习
- [ ] Task Manager V0.4
- [ ] JSON 持久化测试
- [ ] 创建 PR 并合并 main

## 15. 自测

**Q1：class 和 object 有什么区别？**

类是模板，对象是根据类创建的实例。

**Q2：self 是什么？**

当前对象本身。

**Q3：__init__ 的作用？**

初始化新创建的对象。

**Q4：属性和方法有什么区别？**

属性保存对象的数据，方法定义对象的行为。

**Q5：继承有什么作用？**

让子类复用父类的属性和方法，并允许扩展或重写。

**Q6：dataclass 的作用？**

自动生成数据类的常用方法，减少样板代码。

**Q7：Task(**data) 是什么意思？**

将字典展开为关键字参数，调用 Task 类创建对象。

## 16. 验收标准

能够独立写出 Student 和 Task 类，理解实例属性、方法与 self，完成 Task Manager 的对象化重构，并实现 JSON 保存与恢复。