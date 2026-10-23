
import requests


def main():
    url = "https://httpbin.org/get"

    try:
        response = requests.get(url, timeout=10)

        print("状态码：", response.status_code)
        print("响应类型：", response.headers.get("Content-Type"))

        response.raise_for_status()

        data = response.json()

        print("Python 数据类型：", type(data))
        print("服务器返回 URL：", data["url"])
        print("完整 JSON：", data)

    except requests.RequestException as e:
        print(f"网络请求失败：{e}")

    except ValueError as e:
        print(f"JSON 解析失败：{e}")


if __name__ == "__main__":
    main()
