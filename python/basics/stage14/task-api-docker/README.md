# Task API Docker — Python Stage 14

基于 FastAPI、SQLAlchemy、PostgreSQL、uv 和 Docker Compose 的容器化任务管理后端。

## 技术栈

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL 16
- Psycopg
- uv
- Docker
- Docker Compose

## 项目结构

```text
task-api-docker/
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── schemas/
│   ├── db/
│   └── core/
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .env.example
├── pyproject.toml
└── uv.lock
```

## 环境准备

需要本机安装并运行 Docker Engine 和 Docker Compose。

复制 `.env.example` 为 `.env`，配置本地数据库用户、密码和数据库名。

`.env` 不应提交 Git。

## 启动服务

```bash
docker compose up --build
```

或后台运行：

```bash
docker compose up -d --build
```

## API 文档

http://127.0.0.1:8000/docs

## 查看服务

```bash
docker compose ps
```

## 查看日志

```bash
docker compose logs -f backend
```

## PostgreSQL 查询

```bash
docker compose exec db psql -U agent_user -d agent_app
```

## 停止并删除容器

```bash
docker compose down
```

默认保留 named volume。

不要随意使用 `docker compose down -v`，它可能删除数据库数据。

## 数据持久化

PostgreSQL 使用 `postgres_data` named volume 保存数据。

容器删除并重新创建后，数据库数据可以继续保留。

## 功能

- Task CRUD
- 任务搜索
- 优先级筛选
- PATCH 完成任务
- PostgreSQL 持久化
- Docker Compose 多容器管理
- 数据库健康检查

## 后续计划

- Docker 多阶段构建
- GitHub Actions
- 数据库迁移
- 部署与环境管理
- AI Agent 服务容器化