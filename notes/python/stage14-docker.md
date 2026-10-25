# Python 第十四关：Docker 与 FastAPI + PostgreSQL 容器化

## 1. 学习目标

掌握 Docker 基础概念及常见命令，学会使用 Dockerfile 构建 FastAPI 镜像，使用 Docker Compose 同时运行 FastAPI 和 PostgreSQL，并使用 Volume 持久化数据库数据。

重点掌握：

- Docker、Image、Container
- Dockerfile
- FROM、WORKDIR、COPY、RUN、CMD
- Build Context、Layer Cache
- docker build、docker run
- Port Mapping
- 127.0.0.1 与 0.0.0.0
- Docker Compose
- Container Network 与 Service Name
- Environment Variables
- Named Volume 与 Bind Mount
- Healthcheck
- docker compose up/down/ps/logs
- .dockerignore
- FastAPI + PostgreSQL 容器化

## 2. Docker 是什么？

Docker 是用于构建、运行和管理容器的技术平台。

容器能把应用程序、依赖和运行环境组织到相对隔离的环境中，提高跨机器部署的一致性。

Docker 并不意味着宿主机环境完全没有影响，CPU 架构、内核、网络等因素仍然需要考虑。

## 3. Container 与 Virtual Machine

Virtual Machine（虚拟机）通常运行独立的客户操作系统和内核。

Linux 容器通常共享运行它的 Linux 内核，同时隔离进程、文件系统和网络环境。

所以容器通常比完整虚拟机更轻量。

在 Windows 的 Docker Desktop + WSL2 场景中，Linux 容器实际上运行在 Docker 提供的 Linux 环境中。

## 4. Image 与 Container

Image（镜像）是创建容器的模板。

Container（容器）是镜像的运行实例。

可以粗略类比：

```text
Class → Object
Image → Container
```

同一个镜像可以启动多个容器。

## 5. Dockerfile

Dockerfile 描述镜像的构建步骤。

常用指令：

| 指令 | 作用 |
|---|---|
| FROM | 指定基础镜像 |
| WORKDIR | 设置工作目录 |
| COPY | 复制构建上下文中的文件 |
| RUN | 构建镜像时执行命令 |
| CMD | 设置容器启动时的默认命令 |

## 6. FROM

```dockerfile
FROM python:3.12-slim
```

从 Python 3.12 的精简基础镜像开始构建。

slim 表示相对精简。

## 7. WORKDIR

```dockerfile
WORKDIR /app
```

设置后续指令的默认工作目录为容器中的 /app。

## 8. COPY

```dockerfile
COPY app ./app
```

把本地 app 目录复制到镜像中的 /app/app。

注意 Docker COPY 的源路径受 Build Context 限制。

## 9. RUN 与 CMD

```dockerfile
RUN uv sync --frozen --no-dev
```

RUN 在镜像构建时执行。

```dockerfile
CMD ["uvicorn", "app.main:app"]
```

CMD 定义容器启动时的默认命令。

不要把构建阶段和启动阶段混淆。

## 10. docker build

```bash
docker build -t task-api .
```

- build：构建镜像
- -t：为镜像设置名称或标签
- task-api：镜像名称
- .：当前目录是构建上下文

## 11. Build Context

Build Context（构建上下文）是 Docker 构建时可使用的文件集合。

例如：

```bash
docker build .
```

最后的点表示当前目录。

.dockerignore 可以排除不希望进入构建上下文的文件。

## 12. Layer Cache

Docker 镜像构建有层缓存机制。

通常建议先复制依赖配置并安装依赖，再复制经常修改的源代码：

```dockerfile
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY app ./app
```

这样修改 Python 业务代码时，依赖安装层可能复用缓存。

## 13. .dockerignore

用于排除不需要发送到 Docker 构建上下文的文件。

例如：

```text
.git
.venv
.env
.env.*
__pycache__
.pytest_cache
.ruff_cache
```

.gitignore 与 .dockerignore 的用途不同：

- .gitignore：控制 Git 未追踪文件的忽略
- .dockerignore：控制 Docker 构建上下文

## 14. docker run

```bash
docker run task-api
```

根据镜像创建并启动容器。

例如：

```bash
docker run -p 8000:8000 task-api
```

-p 代表发布端口。

8000:8000 分别代表：

```text
宿主机端口 : 容器端口
```

## 15. 0.0.0.0

在 Docker 容器里启动 Uvicorn 时，通常使用：

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

0.0.0.0 表示监听所有可用网络接口。

127.0.0.1 只监听本机回环接口。

如果容器中的服务只监听 127.0.0.1，即使配置了 Docker 端口映射，也可能无法从宿主机正常访问。

## 16. Docker Compose

Docker Compose 使用配置文件统一管理多个容器服务。

本关有：

```text
backend：FastAPI
db：PostgreSQL
```

启动：

```bash
docker compose up
```

后台运行：

```bash
docker compose up -d
```

## 17. compose.yaml

Compose 配置文件描述服务镜像、构建方式、网络、端口、环境变量和数据卷。

例如：

```yaml
services:
  db:
    image: postgres:16
  backend:
    build: .
```

表示管理 db 和 backend 两个服务。

## 18. Service Name

Docker Compose 默认会为同一项目的服务提供内部网络和 DNS 名称。

例如 backend 可以通过：

```text
db:5432
```

连接 PostgreSQL。

注意，容器内部的 localhost 是当前容器自己，不是另一个数据库容器。

## 19. Environment Variables

应用可以从环境变量读取数据库连接配置。

例如：

```python
os.getenv("DATABASE_URL")
```

Compose 可以使用 .env 进行变量替换，并通过 environment 将配置传入容器。

实际密钥不应直接写进 Dockerfile 或提交到公开仓库。

## 20. Named Volume

Volume（数据卷）用于保存需要长期存在的数据。

PostgreSQL 16 的常见数据目录：

```text
/var/lib/postgresql/data
```

通过 named volume 挂载：

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

数据库容器重建时，数据仍可保存在 Volume 中。

## 21. Bind Mount

Bind Mount 将宿主机具体目录挂载到容器内。

例如开发时：

```yaml
volumes:
  - ./app:/app/app
```

适合让容器直接读取本地修改的代码。

Named Volume 常用于数据库数据。

## 22. Healthcheck

Healthcheck 是健康检查。

PostgreSQL 可以使用：

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
```

用于判断数据库是否准备好接受连接。

## 23. depends_on

```yaml
depends_on:
  db:
    condition: service_healthy
```

使 backend 在 db 达到健康状态后再启动。

比只声明启动顺序更适合数据库初始化场景。

## 24. Compose 常用命令

```bash
docker compose up --build
```

构建并启动服务。

```bash
docker compose up -d
```

后台启动。

```bash
docker compose ps
```

查看服务。

```bash
docker compose logs backend
```

查看后端日志。

```bash
docker compose logs -f backend
```

持续跟踪日志。

```bash
docker compose down
```

停止并删除 Compose 创建的服务容器和网络，默认保留 named volume。

## 25. 危险命令

```bash
docker compose down -v
```

-v 会一并删除 Compose 管理的 named volume 等数据卷，可能造成数据库数据丢失。

当前练习不要执行。

## 26. docker exec

```bash
docker compose exec backend sh
```

在运行中的 backend 容器里打开 Shell。

可用于检查文件、运行命令和排查环境问题。

不要依赖进入容器手动修改代码作为正常开发方式。

## 27. Docker Logs

容器应用一般将日志写入 stdout / stderr。

可以通过：

```bash
docker compose logs backend
```

查看日志。

不要把数据库密码、API Key 等敏感值输出到日志中。

## 28. 生产环境与开发环境

开发时可以使用 Uvicorn --reload。

容器化部署通常不默认启用 --reload。

修改通过 COPY 加入镜像的代码后，需要重新构建镜像。

## 29. 常见问题

**Q1：浏览器无法访问后端？**

检查端口映射、容器运行状态、Uvicorn 监听地址和日志。

**Q2：数据库连接 refused？**

检查数据库容器健康状态和连接地址是否使用 db。

**Q3：数据容器重建后丢失？**

检查 PostgreSQL 数据目录是否正确挂载 Named Volume。

**Q4：修改代码不生效？**

检查是否需要 docker compose up --build。

**Q5：密码被复制到镜像？**

检查 Dockerfile COPY 范围和 .dockerignore。

## 30. 与 Agent 项目的关系

未来 Agent 项目可能同时运行：

- FastAPI backend
- PostgreSQL
- Redis
- 向量数据库
- Worker

Docker Compose 可以统一管理这些本地服务。

当前先实现 backend + db 两个服务，不急于增加其他组件。

## 31. 本关验收

- [ ] Docker Desktop / Docker Engine 正常运行
- [ ] docker run hello-world 成功
- [ ] 理解 Image 和 Container
- [ ] 编写 Dockerfile
- [ ] 编写 .dockerignore
- [ ] Docker 镜像构建成功
- [ ] 理解端口映射
- [ ] 编写 compose.yaml
- [ ] backend 和 db 均正常启动
- [ ] PostgreSQL Healthcheck 正常
- [ ] Swagger UI 可以访问
- [ ] Task CRUD 正常
- [ ] 停止并重建容器后数据仍然存在
- [ ] 不提交 .env 和敏感信息
- [ ] 完成 GitHub PR

## 32. 核心总结

Docker Image 是模板，Container 是实例。

Dockerfile 负责构建镜像，Compose 负责管理多个服务。

最终目标：

```text
docker compose up --build
→ FastAPI + PostgreSQL
→ 浏览器访问 /docs
→ CRUD 正常
→ Volume 持久化
```

这是未来部署 AI 应用和 Agent 后端服务的重要基础。