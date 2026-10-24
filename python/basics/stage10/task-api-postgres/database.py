
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE_DIR = Path(__file__).resolve().parent

# 读取项目目录中的 .env 文件
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "未配置 DATABASE_URL，请检查 .env 文件"
    )


# Engine 管理数据库连接基础设施
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)


# Session 工厂
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_db():
    """为每次 FastAPI 请求提供数据库 Session。"""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
