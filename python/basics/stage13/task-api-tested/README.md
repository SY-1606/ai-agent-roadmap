# Task API Tested — Python Stage 13

为 FastAPI + PostgreSQL 分层任务管理项目添加 pytest 自动化测试、代码覆盖率和 Ruff 代码质量检查。

## 技术栈

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- pytest
- HTTPX / TestClient
- pytest-cov
- Ruff
- uv

## 目录结构

```text
task-api-tested/
├── app/
│   ├── api/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── schemas/
│   ├── db/
│   ├── core/
│   └── main.py
├── tests/
│   ├── conftest.py
│   ├── test_main.py
│   ├── test_tasks_api.py
│   └── test_task_service.py
├── .env.example
├── pyproject.toml
└── uv.lock
```

## 环境准备

准备本地 PostgreSQL：

- 开发数据库：agent_app
- 专用测试数据库：agent_app_test

根据 `.env.example` 创建 `.env` 并填写开发数据库连接。

另创建 `.env.test`，填写测试数据库连接。

测试会删除并重新创建 `agent_app_test` 中的任务表，因此该数据库不得保存需要保留的数据。

## 安装依赖

```bash
uv sync
```

## 启动 API

```bash
uv run uvicorn app.main:app --reload
```

API 文档：

http://127.0.0.1:8000/docs

## 单元测试

```bash
uv run pytest tests/test_task_service.py -v
```

## 接口测试

```bash
uv run pytest tests/test_tasks_api.py -v
```

## 全部测试

```bash
uv run pytest -v
```

## 测试覆盖率

```bash
uv run pytest --cov=app --cov-report=term-missing
```

## Ruff

格式化：

```bash
uv run ruff format .
```

检查：

```bash
uv run ruff check .
```

验证格式：

```bash
uv run ruff format --check .
```

## 测试内容

- 根路径 HTTP 响应
- 创建任务
- 查询任务
- 更新任务
- 删除任务
- 任务搜索
- 优先级筛选
- 标记任务完成
- 不存在资源返回 404
- 缺少字段返回 422
- 非法优先级返回 422
- 空白标题返回业务错误
- Service 层参数校验

## 数据隔离

自动化测试通过 FastAPI Dependency Override 使用独立 PostgreSQL 测试数据库。

测试不得连接生产数据库。

## 后续计划

- 更完善的事务回滚测试 fixture
- Mock 外部服务
- GitHub Actions CI
- 类型检查
- Docker 与部署