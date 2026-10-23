
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal


# 1. 创建 FastAPI 应用对象
app = FastAPI(
    title="Python Stage 08 - FastAPI Demo",
    description="FastAPI 基础与 Task CRUD API",
    version="1.0.0",
)


# 2. 模拟数据库：使用内存列表
tasks = [
    {
        "id": 1,
        "title": "学习HTTP",
        "priority": "medium",
        "done": True,
    },
    {
        "id": 2,
        "title": "学习FastAPI",
        "priority": "high",
        "done": False,
    },
]

# 下一条任务的编号
next_task_id = 3


# 3. Pydantic 数据模型
class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    priority: Literal["high", "medium", "low"] = "medium"


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    priority: Literal["high", "medium", "low"]
    done: bool


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0)


# 4. 公共函数：根据 ID 查找任务
def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )


# =========================
# 第一部分：基础 API
# =========================

# GET /
@app.get("/")
def root():
    return {
        "message": "Hello FastAPI"
    }


# GET /hello
@app.get("/hello")
def hello():
    return {
        "message": "Hello World"
    }


# GET /profile
@app.get("/profile")
def get_profile():
    return {
        "name": "Tom",
        "role": "student",
        "skills": ["Python", "Git"],
    }


# GET /add?a=3&b=5
@app.get("/add")
def add(a: int, b: int):
    return {
        "result": a + b
    }


# GET /users/10
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


# POST /users
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    return {
        "message": "用户创建成功",
        "name": user.name,
        "age": user.age,
    }


# =========================
# 第二部分：Task CRUD API
# =========================

# GET /tasks
# 通过 done 查询参数筛选
@app.get("/tasks")
def get_tasks(done: bool | None = None):
    if done is None:
        return tasks

    return [
        task
        for task in tasks
        if task["done"] == done
    ]


# GET /tasks/{task_id}
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return find_task(task_id)


# POST /tasks
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_task_id

    new_task = {
        "id": next_task_id,
        "title": task.title,
        "priority": task.priority,
        "done": False,
    }

    next_task_id += 1
    tasks.append(new_task)

    return new_task


# PUT /tasks/{task_id}
@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskUpdate):
    task = find_task(task_id)

    task["title"] = data.title
    task["priority"] = data.priority
    task["done"] = data.done

    return task


# DELETE /tasks/{task_id}
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)

    tasks.remove(task)

    return {
        "message": "删除成功",
        "task": task,
    }
