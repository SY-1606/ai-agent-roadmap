# HTTP Demo — Python Stage 07

Python HTTP 和 API 基础练习，使用 Requests 发送 GET、POST 请求并解析 JSON 响应。

## 项目内容

| 文件 | 功能 |
|---|---|
| get_demo.py | GET 请求及响应解析 |
| params_demo.py | URL 查询参数 |
| post_demo.py | POST JSON 请求 |
| api_client.py | 可复用 API 客户端函数 |

## 环境

- Python 3.12+
- uv
- Requests

## 初始化

在当前目录执行：

```bash
uv sync
```

## 运行

```bash
uv run python get_demo.py
uv run python params_demo.py
uv run python post_demo.py
uv run python api_client.py
```

## 学习重点

- HTTP Request / Response
- GET / POST
- URL Query Parameters
- JSON Request Body
- Status Code
- Requests 网络异常处理

## 测试服务

本项目使用 `https://httpbin.org` 作为练习接口，运行时需要网络连接。网络访问或服务限制可能影响运行结果。

## 后续计划

将本关的 HTTP 客户端知识应用于 FastAPI 后端开发和 AI Agent API 调用。