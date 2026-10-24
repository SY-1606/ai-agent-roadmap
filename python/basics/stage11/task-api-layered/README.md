# Task API Layered — Python Stage 11

基于 FastAPI、PostgreSQL 和 SQLAlchemy ORM 的分层任务管理 API。

## 技术栈

- Python 3.12+
- uv
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x
- Psycopg
- Pydantic
- python-dotenv

## 项目架构

```text
HTTP Request
  ↓
Router
  ↓
Service
  ↓
Repository
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
```

## 目录

```text
app/
├── main.py
├── api/tasks.py
├── models/task.py
├── schemas/task.py
├── services/task_service.py
├── repositories/task_repository.py
├── db/base.py
├── db/session.py
└── core/config.py
```

## 环境准备

1. 启动 PostgreSQL。
2. 准备数据库 `agent_app` 和角色 `agent_user`。
3. 根据 `.env.example` 创建本地 `.env`。
4. 填写正确的 DATABASE_URL。

## 安装依赖

```bash
uv sync
```

## 运行

```bash
uv run uvicorn app.main:app --reload
```

API 文档：

http://127.0.0.1:8000/docs

## Task API

| Method | Path | 功能 |
|---|---|---|
| GET | /tasks | 获取任务及筛选 |
| GET | /tasks/search | 标题搜索 |
| GET | /tasks/{task_id} | 查询单条任务 |
| POST | /tasks | 新增任务 |
| PUT | /tasks/{task_id} | 更新任务 |
| PATCH | /tasks/{task_id}/complete | 标记完成 |
| DELETE | /tasks/{task_id} | 删除任务 |

## 模块职责

- Router：HTTP 请求和响应
- Service：业务校验和处理
- Repository：ORM 数据访问
- Model：数据库表映射
- Schema：API 输入输出
- DB：连接与 Session
- Config：配置读取

## 说明

本项目使用 PostgreSQL 持久化任务数据。

当前为了学习方便，在 Repository 中管理单次数据操作的提交事务，后续涉及多个 Repository 的复杂业务时应进一步优化事务边界。

生产项目还需要数据库迁移、身份认证、完善的自动化测试等能力。