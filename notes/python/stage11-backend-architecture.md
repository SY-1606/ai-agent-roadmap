# Python 第十一关：后端项目分层与工程化

## 1. 学习目标

将单文件 FastAPI 项目拆分成职责明确的多个模块，为后续 AI Agent 后端开发建立项目组织基础。

重点掌握：

- Router / APIRouter
- Service / Business Logic
- Repository / Data Access Layer
- SQLAlchemy Model
- Pydantic Schema
- Database / Session
- Config / Settings
- Dependency Injection
- Low Coupling / High Cohesion
- Python Package 和绝对导入

## 2. 为什么需要分层？

初学阶段把接口全部写在 main.py 中没有问题。

但功能增加后，会出现：

- HTTP 路由和数据库逻辑混杂
- 业务规则重复
- 单个文件过长
- 单元测试困难
- 多人协作容易产生修改冲突

分层的核心目标是明确职责、降低维护复杂度。

## 3. Router：HTTP 路由层

Router 负责：

- 接收 HTTP 请求
- 读取请求参数
- 调用 Service
- 转换 HTTP 错误
- 返回 API 响应

FastAPI 中使用：

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)
```

`prefix` 是路由前缀。

例如：

```python
@router.get("")
```

最终路径是：

```text
GET /tasks
```

`tags` 用于 Swagger UI 分组。

在主程序中注册：

```python
app.include_router(router)
```

## 4. Service：业务逻辑层

Service 负责业务规则。

例如：

- 任务标题不能为空
- 优先级只能是 high / medium / low
- 不存在的任务不能更新
- 完成任务时修改完成状态

Service 通常不直接处理 HTTP 状态码。

这样业务代码可以被 HTTP 接口、命令行程序和测试代码复用。

## 5. Repository：数据访问层

Repository 主要负责数据库操作。

例如：

```python
statement = select(Task)
tasks = db.scalars(statement).all()
```

以及：

```python
db.add(task)
db.commit()
```

Repository 不负责 HTTP 响应格式，也不应该生成 JSONResponse。

## 6. Model：数据库模型

SQLAlchemy ORM Model 描述数据库表结构。

```python
class Task(Base):
    __tablename__ = "tasks"
```

例如：

```python
title: Mapped[str] = mapped_column(
    String(200)
)
```

Model 与数据库表和 Python ORM 对象关联。

## 7. Schema：API 数据结构

Pydantic Schema 描述 API 输入输出。

```python
class TaskCreate(BaseModel):
    title: str
    priority: str = "medium"
```

常见模型：

- TaskCreate：创建任务
- TaskUpdate：更新任务
- TaskResponse：返回任务

注意：SQLAlchemy Model 与 Pydantic Schema 不是同一个东西。

## 8. DB：数据库基础设施

db/base.py：

```python
class Base(DeclarativeBase):
    pass
```

db/session.py：

```python
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
```

DB 层负责数据库连接、Engine 和 Session 管理。

## 9. Config：配置管理

core/config.py 统一读取配置：

```python
settings.database_url
settings.app_name
settings.debug
```

避免到处重复调用 os.getenv。

本地密钥使用 .env 文件，不能提交 GitHub。

## 10. Dependency Injection：依赖注入

```python
db: Session = Depends(get_db)
```

表示路由函数需要一个数据库 Session，由 FastAPI 提供。

好处包括：

- 减少重复创建依赖的代码
- 统一管理资源
- 更方便替换测试数据库
- 使依赖关系清晰

## 11. Python Package

包含 Python 模块的目录可以组织成包。

常见项目使用 __init__.py 明确包的结构。

例如：

```python
from app.models.task import Task
```

含义：

- app：顶层包
- models：子包
- task：模块
- Task：其中的类

## 12. 绝对导入与循环导入

推荐优先使用：

```python
from app.services import task_service
```

避免模块间互相导入：

```text
A 导入 B
B 又导入 A
```

这种现象叫 Circular Import（循环导入）。

分层明确有助于降低循环依赖风险。

## 13. 依赖方向

本关主要依赖链：

```text
Router
  ↓
Service
  ↓
Repository
  ↓
Model / Database
```

上层调用下层，尽量避免底层反向依赖高层业务代码。

Schema 为 API 提供数据定义，Config 为数据库等模块提供配置。

## 14. 低耦合与高内聚

Low Coupling（低耦合）：

模块之间减少不必要的紧密依赖。

High Cohesion（高内聚）：

同一个模块内部的代码围绕明确职责组织。

例如 task_repository.py 只负责 Task 数据访问，而不混入发送邮件或调用大模型的代码。

## 15. 业务异常与 HTTP 异常

例如 Service 中：

```python
raise ValueError("任务标题不能为空")
```

Router 可以转换成：

```python
raise HTTPException(
    status_code=400,
    detail="任务标题不能为空"
)
```

这样 Service 不需要依赖 FastAPI。

当业务复杂后，可以考虑专门的 BusinessError 异常类型。

## 16. PATCH 和 PUT

PUT 通常用于完整替换或更新资源。

PATCH 通常用于部分修改资源。

例如：

```text
PATCH /tasks/1/complete
```

可以只修改任务的完成状态。

## 17. 当前项目结构

```text
app/
├── main.py
├── api/
│   └── tasks.py
├── services/
│   └── task_service.py
├── repositories/
│   └── task_repository.py
├── models/
│   └── task.py
├── schemas/
│   └── task.py
├── db/
│   ├── base.py
│   └── session.py
└── core/
    └── config.py
```

每个目录都具有明确职责。

## 18. 创建任务完整数据流

```text
POST /tasks
  ↓
Router 接收请求
  ↓
Pydantic 校验 TaskCreate
  ↓
Service 校验业务规则
  ↓
Repository 创建 Task ORM 对象
  ↓
SQLAlchemy Session
  ↓
PostgreSQL INSERT
  ↓
TaskResponse
  ↓
JSON 响应
```

## 19. 分层不是越多越好

小项目可能只需要 Router 和 Service。

Repository 并不是所有项目都必须有。

当前单独学习 Repository，是为了理解数据访问抽象和更大型项目的组织方式。

## 20. 本关项目任务

- [ ] 创建 app Python 包
- [ ] 配置 APIRouter
- [ ] 独立 Schema
- [ ] 独立 ORM Model
- [ ] 独立数据库 Engine 和 Session
- [ ] 集中管理配置
- [ ] 编写 Repository CRUD
- [ ] 编写 Service 业务逻辑
- [ ] 实现 Router CRUD
- [ ] 实现搜索和优先级筛选
- [ ] 实现 PATCH 完成任务
- [ ] 通过 Swagger UI 测试
- [ ] PR 合并 main

## 21. 自测

**Q1：Router 的职责？**

接收 HTTP 请求，调用业务逻辑，转换并返回 HTTP 响应。

**Q2：Service 的职责？**

实现任务相关的业务规则。

**Q3：Repository 的职责？**

封装数据库访问操作。

**Q4：Model 与 Schema 区别？**

Model 描述 ORM 数据库映射；Schema 描述 API 数据结构及校验。

**Q5：Config 是什么？**

集中管理应用配置。

**Q6：include_router 做什么？**

把一组 APIRouter 路由注册到主 FastAPI 应用。

**Q7：什么是依赖注入？**

函数需要的依赖由外部系统提供，例如由 FastAPI 提供数据库 Session。

**Q8：什么是低耦合？**

减少模块间不必要的紧密依赖。

**Q9：什么是高内聚？**

每个模块集中承担明确职责。

**Q10：为什么业务层不应直接返回 HTTPException？**

因为业务逻辑应尽量独立于 HTTP 框架，便于测试和复用。

## 22. 验收标准

能够独立解释 Router、Service、Repository、Model、Schema、DB 和 Config，并把第十关单文件 Task API 重构成支持 CRUD、搜索、筛选、PATCH 的分层 PostgreSQL 后端。