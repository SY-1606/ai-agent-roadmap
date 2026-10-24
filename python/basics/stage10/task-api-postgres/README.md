# Task API with PostgreSQL — Stage 10

使用 FastAPI、PostgreSQL、SQLAlchemy 2.x ORM 和 Pydantic 构建任务管理 API。

## 技术栈

- Python 3.12+
- uv
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy ORM
- Psycopg 3
- Pydantic
- python-dotenv

## 项目结构

```text
task-api-postgres/
├── main.py         # FastAPI 路由
├── database.py     # Engine 与 Session
├── models.py       # SQLAlchemy ORM Model
├── schemas.py      # Pydantic Schema
├── test_db.py      # ORM CRUD 练习
├── .env.example    # 环境变量示例
├── pyproject.toml
└── uv.lock
```

## 本地配置

确保 PostgreSQL 已启动，并已经创建数据库角色 `agent_user` 和数据库 `agent_app`。

复制 `.env.example` 为 `.env`，填写本地实际数据库连接参数。

不要将 `.env` 提交到 Git。

## 安装依赖

```bash
uv sync
```

## ORM 练习

```bash
uv run python test_db.py
```

## 启动 API

```bash
uv run uvicorn main:app --reload
```

访问：

http://127.0.0.1:8000/docs

## API

| 方法 | 路径 | 作用 |
|---|---|---|
| GET | /tasks | 查询、筛选和分页 |
| GET | /tasks/search | 搜索标题 |
| GET | /tasks/{task_id} | 查询指定任务 |
| POST | /tasks | 新增任务 |
| PUT | /tasks/{task_id} | 更新任务 |
| DELETE | /tasks/{task_id} | 删除任务 |

## 数据持久化

任务保存在 PostgreSQL 数据库的 `tasks` 表中。

正常重启 FastAPI 后，数据库中的数据不会消失。

## 项目局限

这是教学性质的同步数据库 API，尚未实现身份认证、角色权限、数据库迁移和完整自动化测试。

下一阶段可以继续学习 Alembic、事务管理、pytest 和更规范的 Service 层。