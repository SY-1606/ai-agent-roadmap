
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.json"


def load_config():
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    try:
        config = load_config()
    except (OSError, json.JSONDecodeError) as e:
        print(f"配置加载失败：{e}")
        return

    print("应用名称：", config.get("app_name"))
    print("调试模式：", config.get("debug"))
    print("最大历史记录：", config.get("max_history"))


if __name__ == "__main__":
    main()
