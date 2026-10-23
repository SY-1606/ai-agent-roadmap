# FastAPI Demo — Python Stage 08

使用 Python、FastAPI、Uvicorn 和 Pydantic 实现一个内存版 Task CRUD API。

## 环境

- Python 3.12+
- uv
- FastAPI
- Uvicorn
- Pydantic（FastAPI 依赖）

## 安装依赖

进入项目目录执行：

```bash
uv sync
```

## 启动

```bash
uv run uvicorn main:app --reload
```

默认地址：

- 根路径：http://127.0.0.1:8000/
- Swagger UI：http://127.0.0.1:8000/docs
- ReDoc：http://127.0.0.1:8000/redoc

## 基础接口

| Method | Path | 功能 |
|---|---|---|
| GET | / | Hello API |
| GET | /hello | Hello World |
| GET | /profile | 个人信息示例 |
| GET | /add?a=3&b=5 | 加法 |
| GET | /users/{user_id} | 用户路径参数 |
| POST | /users | 创建用户示例 |

## Task CRUD API

| Method | Path | 功能 |
|---|---|---|
| GET | /tasks | 查询任务列表 |
| GET | /tasks/{task_id} | 查询指定任务 |
| POST | /tasks | 创建任务 |
| PUT | /tasks/{task_id} | 更新任务 |
| DELETE | /tasks/{task_id} | 删除任务 |

## 创建任务示例

POST /tasks

```json
{
  "title": "学习FastAPI",
  "priority": "high"
}
```

成功时返回 HTTP 201。

## 更新任务示例

PUT /tasks/1

```json
{
  "title": "学习数据库",
  "priority": "medium",
  "done": true
}
```

## 错误处理

- 404：指定任务不存在
- 422：请求参数或请求体校验失败

## 数据说明

任务存储在 Python 内存列表中，服务器重启后会恢复初始任务，不具备持久化能力。

本项目仅用于学习 FastAPI 路由、Pydantic 校验和 HTTP CRUD。

## 后续计划

学习数据库、持久化存储、项目分层、自动测试，以及 AI Agent API。