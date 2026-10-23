
import requests


def get_json(url, params=None):
    """发送 GET 请求并返回解析后的 JSON。"""
    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"GET 请求失败：{e}")

    except ValueError as e:
        print(f"JSON 解析失败：{e}")

    return None


def post_json(url, data):
    """发送 POST JSON 请求并返回解析后的 JSON。"""
    try:
        response = requests.post(
            url,
            json=data,
            timeout=10,
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"POST 请求失败：{e}")

    except ValueError as e:
        print(f"JSON 解析失败：{e}")

    return None


def main():
    print("===== API Client Demo =====")

    get_result = get_json(
        "https://httpbin.org/get",
        params={"course": "python", "stage": 7},
    )

    if get_result is not None:
        print("GET 结果：", get_result.get("args"))

    task = {
        "title": "学习 API",
        "done": False,
    }

    post_result = post_json(
        "https://httpbin.org/post",
        task,
    )

    if post_result is not None:
        print("POST 结果：", post_result.get("json"))


if __name__ == "__main__":
    main()
