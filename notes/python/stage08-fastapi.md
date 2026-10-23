# Python 第八关：FastAPI 从零搭建后端 API

## 1. 学习目标

学会用 FastAPI 编写 Web 后端，理解 HTTP 请求如何映射到 Python 函数，并实现 Task CRUD API。

重点掌握：

- FastAPI 与 Uvicorn
- ASGI
- `app = FastAPI()`
- 路由与装饰器
- GET / POST / PUT / DELETE
- Path Parameter 和 Query Parameter
- Pydantic BaseModel
- HTTPException
- HTTP 状态码
- Swagger UI /docs
- Task CRUD API

## 2. FastAPI 是什么？

FastAPI 是 Python Web 框架（Web Framework）。

它可以帮助我们处理：

- HTTP 请求解析
- 路由匹配
- 数据校验
- JSON 响应
- API 文档生成
- 错误响应

基本代码：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
```

## 3. Uvicorn 是什么？

Uvicorn 是 ASGI Server，即支持 ASGI 接口的 Web 服务器。

主要负责：

1. 监听网络端口
2. 接收 HTTP 请求
3. 将请求交给 FastAPI 应用
4. 把应用产生的响应返回客户端

FastAPI 负责 Web 应用逻辑，Uvicorn 负责运行并对外提供网络服务。

## 4. 什么是 ASGI？

ASGI 全称 Asynchronous Server Gateway Interface。

它是 Python Web 服务器和应用之间的接口规范。

当前阶段只需要理解：

```text
浏览器
  ↓ HTTP Request
Uvicorn
  ↓ ASGI
FastAPI
  ↓ 路由匹配
Python 函数
  ↓ 返回数据
FastAPI
  ↓ HTTP Response
Uvicorn
  ↓
浏览器
```

## 5. 创建应用对象

```python
from fastapi import FastAPI

app = FastAPI()
```

- `FastAPI` 是类
- `FastAPI()` 创建实例
- `app` 是 Web 应用对象

这是第五关 OOP 知识的实际应用。

## 6. 路由 Route

```python
@app.get("/")
def root():
    return {"message": "Hello"}
```

其中：

- `@app.get("/")`：注册 GET `/` 路由
- `def root()`：定义处理请求的函数
- `return`：返回 Python 数据

路由就是 HTTP 方法、路径和处理函数之间的映射。

例如：

```text
GET /          -> root()
GET /tasks     -> get_tasks()
POST /tasks    -> create_task()
```

## 7. 装饰器 Decorator

`@app.get("/")` 是装饰器语法。

它会将下方函数注册为指定 HTTP 请求的处理函数。

这个函数本身仍然是普通 Python 函数，只是由 FastAPI 在收到对应请求时调用。

## 8. 启动服务器

```bash
uv run uvicorn main:app --reload
```

拆解：

- `uv run`：在项目环境中运行
- `uvicorn`：启动 ASGI 服务器
- `main:app`：从 main 模块中导入 app 对象
- `--reload`：开发时文件修改后自动重载

默认常用地址：

```text
http://127.0.0.1:8000/
```

## 9. JSON 响应

```python
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
```

FastAPI 可以将可序列化的 Python 字典转换为 JSON 响应。

Python：

```python
{"done": False}
```

JSON：

```json
{"done": false}
```

## 10. Path Parameter 路径参数

```python
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}
```

访问：

```text
GET /tasks/5
```

返回：

```json
{"task_id": 5}
```

FastAPI 利用类型提示将参数解析为整数。

如果访问 `/tasks/abc`，参数校验通常会失败并返回 422。

## 11. Query Parameter 查询参数

```python
@app.get("/tasks")
def get_tasks(done: bool | None = None):
    return {"done": done}
```

访问：

```text
/tasks?done=true
```

`done` 会被解析为布尔值 `True`。

`bool | None` 表示参数可以是布尔值，也可以是 None。

`= None` 表示该参数不是必填项。

## 12. Pydantic BaseModel

Pydantic 用于定义数据结构并进行校验。

```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: str = "medium"
```

这里：

- `TaskCreate` 是类
- `BaseModel` 是它继承的父类
- `title` 是必填字段
- `priority` 有默认值

FastAPI 可以利用模型解析请求体。

## 13. POST 请求

```python
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    return {
        "title": task.title,
        "priority": task.priority
    }
```

客户端发送：

```json
{
  "title": "学习FastAPI",
  "priority": "high"
}
```

FastAPI 会解析 JSON、进行模型校验，再将模型对象传给函数。

## 14. Path、Query、Body 的判断

| 定义方式 | FastAPI 主要理解为 |
|---|---|
| 路径中的 `{task_id}` | Path Parameter |
| 不在路径中的简单参数 | Query Parameter |
| Pydantic BaseModel 参数 | Request Body |

这条规则是本关重点。

## 15. HTTPException

如果任务不存在，应返回 404。

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="任务不存在"
)
```

响应通常为：

```json
{
  "detail": "任务不存在"
}
```

HTTP 状态码为 404。

## 16. CRUD API

CRUD 表示 Create、Read、Update、Delete。

常见接口：

```text
GET    /tasks
GET    /tasks/{task_id}
POST   /tasks
PUT    /tasks/{task_id}
DELETE /tasks/{task_id}
```

- GET：读取任务
- POST：创建任务
- PUT：替换或更新任务
- DELETE：删除任务

## 17. Swagger UI 和 OpenAPI

FastAPI 默认提供交互式 API 文档：

```text
http://127.0.0.1:8000/docs
```

可以：

- 查看全部 API
- 阅读参数说明
- 输入请求体
- 发送 GET、POST、PUT、DELETE
- 查看状态码和响应结果

另一个文档地址：

```text
http://127.0.0.1:8000/redoc
```

Swagger UI 是 API 文档的交互式界面，OpenAPI 是描述 API 结构的规范。

## 18. 服务器和数据存储

本关 Task API 使用 Python 列表保存任务。

因此：

- 服务器重启后数据可能重置
- 不支持可靠的多进程共享
- 不适合作为生产环境数据库

本关重点是路由、请求校验、响应与 CRUD，不引入数据库。

## 19. def 和 async def

FastAPI 支持同步和异步处理函数。

```python
def get_tasks():
    ...
```

以及：

```python
async def get_tasks():
    ...
```

当前阶段先使用普通的 `def`。

后续学习异步请求和数据库时再深入 async / await。

## 20. 常见错误

### ModuleNotFoundError

确认安装并使用了项目的虚拟环境。

```bash
uv add fastapi uvicorn
```

### 端口被占用

可以使用其他端口：

```bash
uv run uvicorn main:app --reload --port 8001
```

### POST 无法通过浏览器地址栏测试

浏览器地址栏通常发送 GET 请求。

POST、PUT、DELETE 推荐使用 `/docs`。

### 422 校验错误

常见原因：

- 缺少必填字段
- 参数类型不符合要求
- 数据不满足模型约束

### 404

请求的接口路径或资源不存在。

## 21. 与 AI Agent 的关系

未来 Agent 后端可能提供：

```text
POST /chat
POST /documents
GET  /conversations
```

例如：

```json
{
  "message": "帮我总结这篇论文"
}
```

后端接收 JSON，调用 Agent 逻辑，然后返回结果。

这和当前 Task CRUD API 使用的是相同的 HTTP 请求—处理—响应模式。

## 22. 本关验收

- [ ] 创建 uv FastAPI 项目
- [ ] 安装 FastAPI 和 Uvicorn
- [ ] 浏览器访问 GET /
- [ ] 完成 GET /profile
- [ ] 完成 GET /add
- [ ] 完成路径参数练习
- [ ] 完成 POST /users
- [ ] 完成 Task CRUD API
- [ ] 正确返回 404
- [ ] 体验 422 校验错误
- [ ] 使用 /docs 测试接口
- [ ] 创建 PR 合并 main

## 23. 自测题

**Q1：FastAPI 和 Uvicorn 有什么区别？**

FastAPI 是 Web 框架，Uvicorn 是运行 ASGI 应用的服务器。

**Q2：app = FastAPI() 是什么？**

创建一个 FastAPI 应用对象。

**Q3：@app.get("/tasks") 是什么意思？**

将下方函数注册为处理 GET /tasks 的路由函数。

**Q4：main:app 是什么意思？**

从 main 模块中导入名为 app 的应用对象。

**Q5：为什么返回字典能得到 JSON？**

FastAPI 会将可序列化数据转换成 JSON HTTP 响应。

**Q6：Path Parameter 和 Query Parameter 有什么区别？**

前者来自 URL 路径，后者通常来自 URL 问号后的查询字符串。

**Q7：BaseModel 的作用？**

定义并校验数据结构。

**Q8：HTTPException 有什么用？**

通过抛出异常生成指定状态码的 HTTP 错误响应。

**Q9：/docs 是什么？**

FastAPI 自动提供的交互式 API 文档页面。

**Q10：为什么当前数据不能长期保存？**

因为使用内存列表，服务器重启后不会自动持久化。

## 24. 结论

理解完整链路：

HTTP Request → Uvicorn → FastAPI 路由 → 参数校验 → Python 函数 → JSON Response。

这是后面编写 AI Agent 后端接口的基础。