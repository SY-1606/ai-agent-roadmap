import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_DIR / ".env")


class Settings:
    def __init__(self):
        self.app_name = os.getenv(
            "APP_NAME",
            "Task API Layered",
        )

        self.debug = os.getenv("DEBUG", "false").lower() == "true"

        self.database_url = os.getenv("DATABASE_URL")

        if not self.database_url:
            raise RuntimeError("DATABASE_URL 未配置，请检查项目根目录 .env")


settings = Settings()
