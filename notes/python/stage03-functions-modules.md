# Python 第三关：函数、作用域、模块与代码组织

## 1. 学习目标

把以前从上到下编写的代码拆分成函数和模块。

重点掌握：

- 函数定义与调用
- 参数和返回值
- 作用域
- 类型提示
- 模块与 import
- `__name__ == "__main__"`
- `*args`、`**kwargs`
- 函数作为对象
- 多文件项目组织

## 2. 函数基础

使用 `def`（define，定义）创建函数。

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Tom"))
```

定义函数时，函数体不会立即运行；调用函数时才执行。

## 3. 形参与实参

```python
def add(a, b):
    return a + b

result = add(3, 5)
```

- `a`、`b`：形参（Parameter）
- `3`、`5`：实参（Argument）

## 4. print 与 return 的区别

```python
def add1(a, b):
    print(a + b)

def add2(a, b):
    return a + b
```

- `print()`：将内容显示在终端
- `return`：把结果返回给调用者，并结束当前函数
- 没有显式返回值的函数通常返回 `None`

实际业务函数优先返回数据，让主程序决定如何显示。

## 5. 参数类型

### 位置参数

```python
introduce("Tom", 20)
```

### 关键字参数

```python
introduce(age=20, name="Tom")
```

### 默认参数

```python
def greet(name, language="zh"):
    if language == "zh":
        return f"你好，{name}"
    return f"Hello, {name}"
```

### 避免可变默认参数

不推荐：

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

推荐：

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

原因：默认参数在函数定义时求值，可变对象可能被多次调用共享。

## 6. 类型提示 Type Hint

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int`：希望参数是整数
- `-> int`：希望返回整数

类型提示主要用于阅读、编辑器提示、静态类型检查，不会自动进行运行时类型验证。

## 7. 作用域 Scope

```python
app_name = "AgentApp"

def show_name():
    message = "Hello"
    print(app_name)
```

- 局部变量 Local Variable：函数内部定义的变量
- 全局变量 Global Variable：模块级变量

变量查找顺序通常使用 LEGB 规则：

Local → Enclosing → Global → Built-in

应尽量通过参数和返回值传递数据，减少对可修改全局变量的依赖。

## 8. 模块 Module

一个 `.py` 文件可以作为 Python 模块。

例如：

```python
# calculator.py
def add(a, b):
    return a + b
```

另一个文件：

```python
import calculator

print(calculator.add(3, 5))
```

还可以：

```python
from calculator import add
```

或：

```python
import calculator as calc
```

## 9. 主程序入口

标准结构：

```python
def main():
    print("程序运行")

if __name__ == "__main__":
    main()
```

当前文件直接运行时，`__name__` 是 `"__main__"`。

当前模块被导入时，`__name__` 通常是模块名，因此不会执行这个条件块中的 `main()`。

## 10. 不定长参数

### *args

```python
def add_all(*args):
    return sum(args)
```

将多个额外位置参数收集为 tuple。

### **kwargs

```python
def show_info(**kwargs):
    print(kwargs)
```

将多个额外关键字参数收集为 dict。

## 11. 函数对象

函数可以存储在变量和字典中：

```python
def search(query):
    return f"搜索：{query}"

tools = {
    "search": search
}

tool = tools["search"]
print(tool("Python"))
```

关键区别：

- `search`：函数对象本身
- `search()`：调用函数

这是以后学习 Agent Tool Calling（工具调用）的基础。

## 12. 工程化原则

1. 一个函数尽量只负责一件明确的事情。
2. 函数名采用动词加名词，例如 `add_task()`。
3. 业务逻辑和输入输出分开。
4. 重复代码提取为公共函数。
5. 主程序负责组合各个模块。
6. 使用 docstring 说明函数的用途。

## 13. 本关项目

- [ ] 函数基础练习
- [ ] 计算器模块
- [ ] 学生管理模块
- [ ] Task Manager 多文件重构
- [ ] 模拟 Agent Tool Calling
- [ ] 独立运行并测试
- [ ] 创建 Pull Request 并合并

## 14. 自测

**Q1：print 与 return 有什么区别？**

print 负责显示，return 负责向调用者返回结果。

**Q2：函数没写 return 会返回什么？**

`None`。

**Q3：什么是模块？**

可供导入使用的 Python 文件。

**Q4：`if __name__ == "__main__":` 有什么作用？**

只在当前文件作为主程序直接运行时，执行对应代码块。

**Q5：`*args` 和 `**kwargs` 的区别？**

前者收集额外位置参数形成 tuple，后者收集额外关键字参数形成 dict。

**Q6：字典中存函数有什么用？**

可以根据字符串名称查找到函数，再执行它，例如模拟 Agent 工具调度。

## 15. 验收标准

能够独立定义函数、传入参数、返回结果、导入自定义模块，并把任务管理器拆成多个文件。重点掌握 return、模块拆分和函数对象。