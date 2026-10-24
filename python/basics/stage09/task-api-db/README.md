# Task API with SQLite — Python Stage 09

使用 FastAPI、Uvicorn 和 SQLite 实现任务管理后端。

## 功能

- 创建任务
- 查询任务
- 更新任务
- 完成任务
- 删除任务
- 条件筛选与分页
- SQLite 持久化

## 环境

- Python 3.12+
- uv
- FastAPI
- Uvicorn
- SQLite（Python 标准库 sqlite3）

## 安装

```bash
uv sync
```

## 启动

```bash
uv run uvicorn main:app --reload
```

Swagger UI：

http://127.0.0.1:8000/docs

## 接口

| Method | Path | 说明 |
|---|---|---|
| GET | / | 服务状态 |
| GET | /tasks | 任务列表 |
| GET | /tasks/{task_id} | 获取任务 |
| POST | /tasks | 创建任务 |
| PUT | /tasks/{task_id} | 更新任务 |
| PUT | /tasks/{task_id}/complete | 标记完成 |
| DELETE | /tasks/{task_id} | 删除任务 |

## 数据存储

所有任务保存在本地 `tasks.db` 文件中。

与上一关的内存版 Task API 不同，正常重启服务器后数据能够保留。

这是学习项目，还没有生产级数据库迁移、权限管理和并发优化。