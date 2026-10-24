# Python 第十关：PostgreSQL + SQLAlchemy ORM

## 1. 学习目标

掌握 PostgreSQL 数据库服务器和 SQLAlchemy 2.x ORM 的基本使用方法，并与 FastAPI 结合，建立支持持久化的 Task CRUD API。

重点：

- PostgreSQL 与 SQLite 的区别
- PostgreSQL 用户、数据库、psql
- Psycopg 数据库驱动
- SQLAlchemy ORM
- Engine、Connection Pool、Session
- DeclarativeBase、Mapped、mapped_column
- ORM INSERT、SELECT、UPDATE、DELETE
- FastAPI Depends(get_db)
- SQLAlchemy Model 与 Pydantic Schema
- .env 和 DATABASE_URL
- Transaction、commit、rollback
- 数据库迁移与 Alembic

## 2. SQLite 与 PostgreSQL

SQLite 是嵌入式数据库，一般直接操作本地数据库文件。

PostgreSQL 是独立的数据库服务器，可以同时管理多个数据库并服务多个客户端。

```text
SQLite:
Python -> tasks.db

PostgreSQL:
Python -> 数据库连接 -> PostgreSQL Server -> agent_app -> tasks
```

PostgreSQL 更适合需要数据库服务器、多用户访问和完善事务管理的后端应用。

## 3. PostgreSQL 用户

Linux 用户和 PostgreSQL 数据库角色是不同的概念。

例如：

- zbh：Linux 用户
- postgres：常见的数据库管理角色
- agent_user：我们为学习项目创建的数据库角色

数据库角色用于管理登录和访问权限。

## 4. 安装 PostgreSQL

Ubuntu 中可以使用：

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

检查客户端：

```bash
psql --version
```

检查数据库服务：

```bash
sudo service postgresql status
```

需要时启动：

```bash
sudo service postgresql start
```

## 5. psql

psql 是 PostgreSQL 命令行客户端。

```bash
sudo -u postgres psql
```

常用元命令：

| 命令 | 作用 |
|---|---|
| \l | 查看数据库 |
| \dt | 查看当前数据库中的表 |
| \d tasks | 查看 tasks 表结构 |
| \q | 退出 |

这些反斜杠命令是 psql 元命令，不是 SQL。

## 6. 数据库与角色

本项目使用：

```text
数据库角色：agent_user
数据库名称：agent_app
```

数据库连接常用信息：

- Host：localhost
- Port：5432
- User：agent_user
- Database：agent_app

数据库密码应由自己设置，并放入本地 .env 文件，不能提交 GitHub。

## 7. Psycopg

Psycopg 是 Python PostgreSQL 驱动。

```text
Python / SQLAlchemy
        ↓
Psycopg
        ↓
PostgreSQL
```

项目通过 uv 安装：

```bash
uv add "psycopg[binary]"
```

方括号中的 binary 是安装附加选项的一部分。

## 8. SQLAlchemy

SQLAlchemy 是 Python 数据库工具库，包含：

- Core：SQL 表达式、数据库连接等能力
- ORM：对象关系映射

ORM 全称 Object-Relational Mapping。

它能够把数据库中的行映射为 Python 对象。

例如：

```python
task = Task(title="学习ORM")
```

保存后对应数据库的一条 tasks 记录。

## 9. Engine

```python
engine = create_engine(DATABASE_URL)
```

Engine 是数据库连接的基础设施对象。

它负责连接管理，通常使用连接池。

Engine 本身不能简单理解为一条固定的数据库连接。

## 10. Connection Pool

Connection Pool，即连接池。

数据库连接建立有一定成本，因此连接池可以复用连接，减少重复创建连接的开销。

## 11. Session

Session 是 ORM 操作数据库的核心工作单元。

可以通过它：

- 查询 ORM 对象
- 添加新对象
- 修改对象
- 删除对象
- 管理事务

Engine 主要负责数据库连接基础设施，Session 主要负责一组 ORM 数据操作。

## 12. sessionmaker

```python
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)
```

sessionmaker 用于创建 Session 工厂。

使用：

```python
db = SessionLocal()
```

获得一个 Session 对象。

## 13. ORM Model

现代 SQLAlchemy 2.x 常使用 DeclarativeBase。

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

定义 Task：

```python
class Task(Base):
    __tablename__ = "tasks"
```

表示 Task 类与数据库中的 tasks 表对应。

## 14. Mapped 和 mapped_column

```python
id: Mapped[int] = mapped_column(
    primary_key=True
)
```

Mapped 表示 ORM 映射属性及 Python 类型。

mapped_column 进一步定义数据库列和约束。

例如：

```python
title: Mapped[str] = mapped_column(
    String(200)
)
```

通常对应数据库的 VARCHAR(200) 类型列。

## 15. 创建数据库表

```python
Base.metadata.create_all(bind=engine)
```

SQLAlchemy 根据已定义的模型创建尚不存在的表。

这适合教学和小项目初始化。

已有表结构的修改应当学习数据库迁移工具，而不是依赖 create_all 自动修改已有列。

## 16. ORM INSERT

```python
task = Task(
    title="学习SQLAlchemy",
    priority="high"
)

db.add(task)
db.commit()
db.refresh(task)
```

- Task(...)：创建 Python ORM 对象
- db.add(...)：将对象加入 Session
- db.commit()：提交事务
- db.refresh(...)：从数据库刷新对象属性

## 17. ORM SELECT

```python
from sqlalchemy import select

statement = select(Task)
tasks = db.scalars(statement).all()
```

select(Task) 构造查询表达式。

db.scalars(...) 执行查询并取得标量结果，这里就是 Task 对象。

主键查询：

```python
task = db.get(Task, 1)
```

如果找不到，通常返回 None。

## 18. ORM UPDATE

```python
task = db.get(Task, 1)

if task is not None:
    task.done = True
    db.commit()
```

SQLAlchemy 会追踪对象属性的变化，并在 flush / commit 过程中生成相应 SQL。

## 19. ORM DELETE

```python
task = db.get(Task, 1)

if task is not None:
    db.delete(task)
    db.commit()
```

ORM 最终仍通过数据库 SQL 操作完成删除。

## 20. FastAPI Depends

FastAPI 的 Depends 用于依赖注入（Dependency Injection）。

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

接口：

```python
def get_tasks(db: Session = Depends(get_db)):
    ...
```

FastAPI 会通过 get_db 为接口提供 Session，并在请求处理结束后完成清理。

## 21. ORM Model 与 Pydantic Schema

SQLAlchemy ORM Model：

```python
class Task(Base):
    ...
```

用于数据库表映射。

Pydantic Schema：

```python
class TaskCreate(BaseModel):
    title: str
```

用于 HTTP 请求或响应的数据定义和校验。

这两类模型职责不同。

## 22. from_attributes

```python
class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool

    model_config = {
        "from_attributes": True
    }
```

让 Pydantic 能够从 ORM 对象属性读取响应字段。

## 23. DATABASE_URL

SQLAlchemy PostgreSQL 连接地址一般形如：

```text
postgresql+psycopg://用户名:密码@localhost:5432/数据库名
```

其中：

- postgresql：数据库类型
- psycopg：驱动
- localhost：数据库服务器地址
- 5432：端口
- 最后的路径：数据库名称

密码如果含有特殊字符，需要进行正确的 URL 编码，或者通过 SQLAlchemy URL 对象组装。

## 24. .env

`.env` 是常见的本地环境变量配置文件。

例如：

```dotenv
DATABASE_URL=postgresql+psycopg://...
```

可以通过 python-dotenv 读取：

```python
from dotenv import load_dotenv

load_dotenv()
```

再通过：

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

获取配置。

.env 不应提交 GitHub。

## 25. 事务 Transaction

事务用于把相关数据库操作作为一个整体管理。

例如转账：

```text
账户 A 扣除 100
账户 B 增加 100
```

这两项应当同时成功或同时失败。

- commit：提交事务
- rollback：回滚尚未提交的事务

## 26. ACID

事务的重要特性：

| 缩写 | 英文 | 中文 |
|---|---|---|
| A | Atomicity | 原子性 |
| C | Consistency | 一致性 |
| I | Isolation | 隔离性 |
| D | Durability | 持久性 |

## 27. 数据库迁移 Migration

create_all 可以创建不存在的表，但不能代替已有表的版本化结构调整。

未来需要使用 Alembic 等迁移工具管理新增列、约束和表结构变化。

## 28. 本关项目结构

```text
task-api-postgres/
├── database.py
├── models.py
├── schemas.py
├── main.py
├── test_db.py
├── .env.example
├── pyproject.toml
└── uv.lock
```

职责：

- database.py：连接、Engine、Session
- models.py：SQLAlchemy ORM 模型
- schemas.py：Pydantic 请求和响应模型
- main.py：FastAPI 路由
- test_db.py：ORM 操作演示

## 29. 与 Agent 开发的关系

未来 AI Agent 后端可能会存储：

- 用户
- 会话
- 消息
- 文档
- 工具调用
- 任务
- Agent 执行记录

Web API、ORM 和 PostgreSQL 是建立这类持久化后端的常见方案。

## 30. 本关验收标准

- [ ] 安装 PostgreSQL
- [ ] 创建数据库角色与数据库
- [ ] 使用 psql 成功连接
- [ ] 使用 uv 安装依赖
- [ ] 配置 DATABASE_URL
- [ ] 创建 Engine 和 Session
- [ ] 定义 ORM Task 模型
- [ ] create_all 建表成功
- [ ] ORM INSERT、SELECT、UPDATE、DELETE
- [ ] FastAPI Depends(get_db)
- [ ] Pydantic Schema 校验
- [ ] PostgreSQL Task CRUD API
- [ ] 任务筛选和搜索
- [ ] 服务器重启后任务仍在
- [ ] GitHub PR 合并 main

## 31. 核心结论

完整后端数据流：

浏览器 → HTTP → FastAPI → Pydantic → SQLAlchemy Session → ORM / SQL → Psycopg → PostgreSQL。

这是后续实现 AI Agent 后端、用户会话和聊天记录持久化的基础。