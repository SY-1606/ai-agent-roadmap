from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.tasks import router as task_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

# 导入 ORM Model，确保注册到 Base.metadata
from app.models.task import Task  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="Python Stage 11 - Layered Task API",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "Task API is running",
        "architecture": [
            "Router",
            "Service",
            "Repository",
        ],
    }
