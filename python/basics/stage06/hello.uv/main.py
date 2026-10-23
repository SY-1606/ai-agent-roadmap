
import requests


def main():
    print("===== Python uv 项目练习 =====")

    print(f"Requests 版本：{requests.__version__}")

    url = "https://example.com"

    try:
        response = requests.get(url, timeout=10)

        print(f"请求地址：{url}")
        print(f"HTTP 状态码：{response.status_code}")

        response.raise_for_status()

        print("HTTP 请求成功")

    except requests.exceptions.Timeout:
        print("请求超时")

    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络或代理")

    except requests.exceptions.HTTPError as e:
        print(f"服务器返回错误：{e}")

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误：{e}")


if __name__ == "__main__":
    main()
