
import requests


def main():
    url = "https://httpbin.org/post"

    task = {
        "title": "学习 HTTP",
        "priority": "high",
        "done": False,
    }

    try:
        response = requests.post(
            url,
            json=task,
            timeout=10,
        )

        print("HTTP 状态码：", response.status_code)

        response.raise_for_status()

        data = response.json()

        print("服务器收到的 JSON：")
        print(data["json"])

        print(
            "Content-Type：",
            data["headers"].get("Content-Type"),
        )

    except requests.RequestException as e:
        print(f"POST 请求失败：{e}")

    except ValueError as e:
        print(f"JSON 解析失败：{e}")


if __name__ == "__main__":
    main()
