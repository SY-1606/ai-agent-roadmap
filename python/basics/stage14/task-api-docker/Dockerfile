
# 1. 使用 Python 3.12 精简镜像
FROM python:3.12-slim

# 2. 设置容器内工作目录
WORKDIR /app

# 3. 让 Python 日志及时输出
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. 安装 uv
RUN pip install --no-cache-dir uv

# 5. 先复制依赖管理文件
COPY pyproject.toml uv.lock ./

# 6. 安装运行依赖
RUN uv sync --frozen --no-dev --no-install-project

# 7. 再复制应用代码
COPY app ./app

# 8. 声明应用使用的端口
EXPOSE 8000

# 9. 启动 FastAPI
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
