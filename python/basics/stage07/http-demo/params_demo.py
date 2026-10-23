
import requests


def main():
    url = "https://httpbin.org/get"

    params = {
        "course": "python",
        "week": 7,
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        print("实际请求 URL：", response.url)
        print("服务器收到的参数：", data["args"])

        print("course：", data["args"]["course"])
        print("week：", data["args"]["week"])

    except requests.RequestException as e:
        print(f"请求失败：{e}")

    except ValueError as e:
        print(f"JSON 解析失败：{e}")


if __name__ == "__main__":
    main()
