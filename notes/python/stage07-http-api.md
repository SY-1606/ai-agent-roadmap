# Python 第七关：HTTP、客户端与服务器、URL 和 API

## 1. 学习目标

掌握 Web 后端开发所必需的 HTTP 基础知识，并能够使用 Python Requests 发送 HTTP 请求。

重点：

- Client / Server
- HTTP / HTTPS
- URL、IP、DNS、Port
- Request / Response
- GET、POST、PUT、PATCH、DELETE
- HTTP Status Code
- Headers / Body
- Path Parameter / Query Parameter
- JSON API、REST API
- Requests 实战

## 2. 客户端与服务器

Client（客户端）是主动发起请求的一方。

例如：

- 浏览器
- 手机 App
- 前端网页
- Python Requests 程序

Server（服务器）负责接收和处理请求，并返回响应。

基本过程：

```text
客户端 Client
    |
    | HTTP Request
    v
服务器 Server
    |
    | 处理请求
    |
    | HTTP Response
    v
客户端 Client
```

## 3. HTTP 是什么？

HTTP 全称 HyperText Transfer Protocol，超文本传输协议。

它是一套客户端和服务器交换请求、响应的通信规则。

HTTPS 是通过 TLS 保护通信的 HTTP，能够提供传输加密及相关安全保证。

## 4. URL 的组成

例如：

```text
https://api.example.com:443/tasks?id=10
```

| 部分 | 含义 |
|---|---|
| https | 协议 |
| api.example.com | 域名 |
| 443 | 端口 |
| /tasks | 路径 |
| ?id=10 | 查询参数 |

### IP 地址

用于在网络中标识网络接口等通信目标。

### DNS

Domain Name System，域名系统。

常用于将域名解析为 IP 地址。

### Port

端口用来区分一台设备上的不同网络服务。

常见端口：

- 80：HTTP 默认端口
- 443：HTTPS 默认端口
- 22：SSH 常见端口
- 8000：FastAPI 常用开发端口
- 5432：PostgreSQL 默认端口

### localhost

`localhost` 通常表示当前机器自身，`127.0.0.1` 是 IPv4 回环地址。

例如：

```text
http://127.0.0.1:8000
```

用于访问本机 8000 端口上的 HTTP 服务。

## 5. HTTP Request

请求一般包含：

- Method：请求方法
- URL：资源地址
- Headers：请求头
- Body：请求体（如果有）

例如：

```http
POST /tasks HTTP/1.1
Host: example.com
Content-Type: application/json

{"title": "学习HTTP"}
```

## 6. HTTP Method

| Method | 常见用途 |
|---|---|
| GET | 获取资源 |
| POST | 创建或提交资源 |
| PUT | 创建或整体替换目标资源 |
| PATCH | 局部修改资源 |
| DELETE | 删除资源 |

注意：这些是常见设计约定，实际操作含义取决于 API 文档。

## 7. CRUD

CRUD 是四类基本数据操作：

- Create：创建
- Read：读取
- Update：更新
- Delete：删除

REST 风格 API 常用对应关系：

```text
GET    /tasks       获取所有任务
POST   /tasks       创建任务
GET    /tasks/1     获取编号1的任务
PUT    /tasks/1     替换任务
PATCH  /tasks/1     修改任务部分字段
DELETE /tasks/1     删除任务
```

URL 表示资源，HTTP Method 表示操作意图。

## 8. API

API 全称 Application Programming Interface，应用程序编程接口。

API 是一个程序提供给另一个程序使用的功能入口。

Web API 常通过 HTTP 传输数据，JSON 是常见的数据格式。

例如：

```json
{
  "id": 1,
  "title": "学习HTTP",
  "done": false
}
```

## 9. Path Parameter

例如：

```text
GET /tasks/10
```

`10` 通常是目标任务的 ID。

FastAPI 中可能定义：

```python
@app.get("/tasks/{task_id}")
```

## 10. Query Parameter

例如：

```text
GET /tasks?done=true&priority=high
```

问号后面是查询参数，可用于搜索、筛选、排序和分页。

使用 Requests：

```python
params = {
    "done": "true",
    "priority": "high"
}

requests.get(url, params=params, timeout=10)
```

## 11. Request Body

请求体携带提交给服务器的数据。

例如：

```json
{
  "title": "学习FastAPI",
  "priority": "high"
}
```

Requests 提交 JSON：

```python
requests.post(
    url,
    json={"title": "学习FastAPI"},
    timeout=10
)
```

`params=` 通常构造 URL 查询参数，`json=` 通常生成 JSON 请求体。

## 12. HTTP Headers

Headers 用于传递附加信息。

常见：

```http
Content-Type: application/json
```

表示请求体的数据类型。

```http
Authorization: Bearer TOKEN
```

通常用于携带访问凭证。

真实 API Key 或 Token 不应该直接写进公开仓库。

## 13. HTTP Response

响应通常包含：

- Status Code：状态码
- Headers：响应头
- Body：响应体

例如：

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"message": "success"}
```

## 14. 常用 HTTP 状态码

| 状态码 | 含义 |
|---|---|
| 200 | 请求成功 |
| 201 | 资源已创建 |
| 204 | 成功，但没有响应体 |
| 400 | 请求有问题 |
| 401 | 缺少有效的身份认证 |
| 403 | 禁止访问 |
| 404 | 资源不存在 |
| 422 | 请求内容无法按要求处理，常见于校验失败 |
| 500 | 服务器内部错误 |

记忆：

- 2xx：成功
- 4xx：客户端请求方面的问题
- 5xx：服务器处理方面的问题

## 15. Requests 基础

Requests 是 Python 常用 HTTP 客户端库。

GET 示例：

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

print(response.status_code)
```

### Response 对象

```python
response.status_code
```

HTTP 响应状态码。

```python
response.text
```

返回的文本内容。

```python
response.json()
```

尝试把响应体解析为 Python 对象。

注意：`response.json()` 并不保证成功，响应不是合法 JSON 时可能抛出异常。

## 16. 网络异常处理

```python
try:
    response = requests.get(
        "https://httpbin.org/get",
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

except requests.RequestException as e:
    print(f"请求失败：{e}")
except ValueError as e:
    print(f"JSON 解析失败：{e}")
```

- timeout：限制网络等待时间
- raise_for_status()：对 4xx、5xx 等错误状态抛出异常
- RequestException：Requests 的常见网络请求异常基类

## 17. HTTP 无状态

HTTP 是无状态协议，意味着单个请求本身不要求服务器自动记住此前请求的上下文。

Web 应用可以使用 Cookie、Session、Token 等机制维护用户登录等状态。

## 18. REST API

REST 是一种以资源为核心组织 Web API 的架构风格。

入门阶段先掌握：

```text
GET    /tasks
POST   /tasks
GET    /tasks/1
PUT    /tasks/1
DELETE /tasks/1
```

同一路径配合不同 HTTP 方法，可以表示不同操作。

## 19. Endpoint 和 Route

Endpoint：一个可访问的 API 操作入口。

Route：请求路径、方法与处理程序之间的路由关系。

FastAPI 示例：

```python
@app.get("/tasks")
def get_tasks():
    return tasks
```

当客户端请求 `GET /tasks`，FastAPI 会调用对应的处理函数。

## 20. CLI 与 Web 后端关系

此前 Task Manager 使用：

```python
title = input("任务名称：")
add_task(tasks, title)
print("添加成功")
```

未来 Web 后端则可以：

```text
POST /tasks
    ↓
解析请求体
    ↓
验证 title
    ↓
调用 add_task(...)
    ↓
返回 JSON
```

已有业务逻辑仍有机会被复用。

## 21. 第七关项目

- [ ] GET 请求
- [ ] JSON 响应解析
- [ ] 查询参数
- [ ] POST JSON
- [ ] API 客户端函数封装
- [ ] 网络异常处理
- [ ] uv 项目运行
- [ ] GitHub PR 合并

## 22. 自测题

**Q1：Client 和 Server 区别？**

Client 发起请求，Server 接收请求并返回响应。

**Q2：HTTP 与 HTTPS 区别？**

HTTPS 为 HTTP 通信提供 TLS 安全保护。

**Q3：GET 和 POST 的常见区别？**

GET 通常获取数据；POST 通常提交或创建数据。

**Q4：Path Parameter 和 Query Parameter 有什么区别？**

路径参数通常用来确定具体资源；查询参数通常用于筛选、搜索和分页。

**Q5：params 和 json 的区别？**

params 用于构建 URL 查询参数，json 用于生成 JSON 请求体。

**Q6：response.json() 返回什么？**

尝试将 JSON 响应解析为 Python 对象，可能是 dict、list 等。

**Q7：404 和 500 有什么区别？**

404 表示目标资源未找到；500 表示服务器内部错误。

**Q8：为什么网络请求要设置 timeout？**

防止程序因网络问题长时间等待。

## 23. 验收标准

能够独立使用 Requests 发送 GET 和 POST 请求，理解状态码、请求头、请求体、查询参数，以及 JSON 响应，并能处理常见网络异常，为 FastAPI 开发做好准备。