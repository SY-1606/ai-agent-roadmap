from pathlib import Path

import pytest
from dotenv import dotenv_values
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.task import Task  # noqa: F401

PROJECT_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture
def test_engine():
    """为每条测试建立一个干净的专用测试库表。"""

    config = dotenv_values(PROJECT_DIR / ".env.test")

    test_url = config.get("TEST_DATABASE_URL")

    if not test_url:
        pytest.fail("缺少 TEST_DATABASE_URL，请检查 .env.test")

    parsed_url = make_url(test_url)

    # 安全限制：只允许操作专用测试数据库
    if (
        parsed_url.get_backend_name() != "postgresql"
        or parsed_url.database != "agent_app_test"
        or parsed_url.host not in ("localhost", "127.0.0.1")
    ):
        pytest.fail("拒绝执行：测试数据库必须是 PostgreSQL agent_app_test")

    engine = create_engine(
        test_url,
        pool_pre_ping=True,
    )

    # 测试库专用：测试开始前清空并重建表
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        yield engine

    finally:
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def client(test_engine):
    """使用专用测试数据库，不运行开发环境 lifespan。"""

    def override_get_db():
        with Session(test_engine) as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db

    try:
        test_client = TestClient(app)
        yield test_client

    finally:
        app.dependency_overrides.clear()
