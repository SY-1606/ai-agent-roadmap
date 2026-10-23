# Python 第六关：第三方库、虚拟环境与 uv 项目管理

## 1. 学习目标

掌握 Python 项目的依赖管理、虚拟环境和 uv 工作流程。

重点：

- Python 标准库与第三方库
- module、package、library
- pip 与 PyPI
- dependency 依赖
- Python 虚拟环境 venv
- uv init、uv add、uv run、uv sync、uv lock
- pyproject.toml 和 uv.lock
- VS Code Python 解释器
- GitHub 项目文件管理

## 2. 标准库与第三方库

Python 标准库（Standard Library）是 Python 自带的功能。

```python
import json
import pathlib
import math
import random
```

这些通常不需要另外安装。

第三方库（Third-party Library）由其他开发者维护，需要单独安装。

例如：

```python
import requests
from fastapi import FastAPI
```

没有安装对应包时，可能出现 ModuleNotFoundError。

## 3. module、package、library

| 术语 | 中文 | 基本含义 |
|---|---|---|
| Module | 模块 | 通常是一个 `.py` 文件或可导入模块 |
| Package | 包 | 用于组织相关模块 |
| Library | 库 | 提供可复用功能的代码集合 |

## 4. PyPI 与 pip

PyPI（Python Package Index）是 Python 软件包索引。

pip 是常用的 Python 包管理工具。

```bash
python3 -m pip --version
```

安装第三方库：

```bash
python -m pip install requests
```

使用 `python -m pip` 可以明确使用当前 Python 解释器对应的 pip。

注意：应在合适的虚拟环境内安装，不建议使用 sudo pip 修改 Ubuntu 系统 Python。

## 5. 依赖 Dependency

依赖指程序运行需要的软件包。

例如：

```python
import requests
```

Requests 就是项目的依赖。

依赖分为：

- Direct Dependency：直接依赖，项目主动声明使用
- Transitive Dependency：间接依赖，由其他包引入

## 6. Python 虚拟环境

虚拟环境（Virtual Environment）用于隔离不同项目所使用的 Python 包。

例如：

```text
project-a/
└── .venv/

project-b/
└── .venv/
```

不同项目可以使用不同版本的依赖。

使用 Python 自带的 venv 创建：

```bash
python3 -m venv .venv
```

WSL Ubuntu 中激活：

```bash
source .venv/bin/activate
```

查看解释器：

```bash
which python
python --version
```

退出虚拟环境：

```bash
deactivate
```

`.venv` 不等于虚拟机，也不等于 WSL。

## 7. uv 是什么？

uv 是一个使用 Rust 实现的 Python 包和项目管理工具。

它可以管理：

- Python 版本
- 虚拟环境
- 项目依赖
- 依赖锁文件
- 项目运行

主要命令：

| 命令 | 功能 |
|---|---|
| `uv init` | 初始化项目 |
| `uv add` | 添加依赖 |
| `uv remove` | 移除依赖 |
| `uv run` | 在项目环境内执行程序 |
| `uv lock` | 解析并更新锁文件 |
| `uv sync` | 同步虚拟环境 |
| `uv tree` | 查看依赖关系 |
| `uv --version` | 查看 uv 版本 |

## 8. 使用 uv 初始化项目

```bash
uv init --app --no-package --vcs none hello-uv
```

创建一个应用型 Python 项目，并避免额外创建 Git 仓库。

进入项目：

```bash
cd hello-uv
```

查看生成的文件：

```bash
ls -la
```

uv 不同版本的项目模板可能略有差异。

## 9. pyproject.toml

这是 Python 项目的核心配置文件。

示例：

```toml
[project]
name = "hello-uv"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32"
]
```

其中：

- name：项目名称
- version：项目版本
- requires-python：Python 版本要求
- dependencies：项目依赖

实际版本范围由 uv 根据已解析的依赖填写，不需要手动照抄示例。

## 10. uv.lock

`uv.lock` 是依赖锁文件（Lock File）。

它记录依赖解析后的具体版本及相关信息，便于项目在不同设备上复现环境。

区别：

- `pyproject.toml`：声明项目需要什么
- `uv.lock`：记录依赖最终锁定的结果

通常两个文件都应提交 Git。

## 11. 添加和移除依赖

添加 Requests：

```bash
uv add requests
```

这会更新项目依赖记录，并进行依赖解析和环境同步。

移除：

```bash
uv remove requests
```

## 12. 使用 uv run

```bash
uv run python main.py
```

uv 会使用项目对应的环境执行程序，并在需要时同步依赖。

因此不必每次手动激活 `.venv`。

## 13. uv sync

```bash
uv sync
```

将项目虚拟环境与依赖配置、锁文件同步。

典型场景：

```text
从 GitHub 克隆项目
        ↓
项目内包含 pyproject.toml、uv.lock
        ↓
运行 uv sync
        ↓
创建虚拟环境、安装依赖
        ↓
使用 uv run 执行程序
```

## 14. uv.lock 与依赖可复现

例如某个依赖声明为：

```text
requests>=2.32
```

允许不同兼容版本。

锁文件则记录解析得到的确切版本，使不同环境更容易使用一致的依赖集合。

## 15. VS Code Python 解释器

如果代码能运行，但 VS Code 提示 import 不存在，需要确认 Python Interpreter（解释器）。

使用：

`Ctrl + Shift + P`

搜索：

`Python: Select Interpreter`

选择当前项目 `.venv/bin/python`。

## 16. .venv 和 .env

| 文件或目录 | 作用 |
|---|---|
| `.venv/` | Python 虚拟环境 |
| `.env` | 通常存储环境变量配置 |
| `pyproject.toml` | 项目配置及依赖声明 |
| `uv.lock` | 依赖锁文件 |
| `.python-version` | 项目选用的 Python 版本 |

`.venv` 和包含密钥的 `.env` 不应提交到公开 GitHub 仓库。

## 17. GitHub 版本管理

推荐提交：

- Python 源代码
- README.md
- pyproject.toml
- uv.lock
- .python-version
- .gitignore

推荐忽略：

- .venv/
- __pycache__/
- .env
- 临时文件与个人密钥

## 18. Requests 基础

Requests 是一个常用的 HTTP 客户端库。

```python
import requests

response = requests.get(
    "https://example.com",
    timeout=10
)

print(response.status_code)
```

这里：

- requests.get()：发送 HTTP GET 请求
- response：响应对象
- response.status_code：HTTP 状态码
- response.text：响应文本
- response.json()：尝试将响应内容解析为 JSON

网络请求可能因为代理、证书、超时等原因失败。

## 19. 本关常见问题

**Q1：为什么 import requests 失败？**

可能没有安装 Requests，或者使用了错误的 Python 环境。

**Q2：为什么 uv init 没有生成 main.py？**

不同版本和初始化选项可能生成不同项目布局，应该检查实际生成的目录。

**Q3：.venv 要上传 GitHub 吗？**

不需要，它属于可重建的运行环境。

**Q4：pip 和 uv 有什么区别？**

pip 主要用于包安装管理，uv 还提供项目初始化、锁文件、环境同步和运行等工作流。

**Q5：为什么需要 uv.lock？**

为了记录依赖解析结果，提高项目环境的可复现性。

**Q6：为什么不能把 API Key 写进仓库？**

公开仓库中的密钥可能泄漏并被他人滥用。

## 20. 本关验收清单

- [ ] 能解释标准库和第三方库
- [ ] 能解释 pip 和虚拟环境
- [ ] uv 初始化项目成功
- [ ] 使用 uv 添加 Requests
- [ ] 使用 uv run 运行程序
- [ ] 能查看 pyproject.toml
- [ ] 理解 uv.lock
- [ ] 会使用 uv sync
- [ ] 能正确选择 VS Code 解释器
- [ ] 提交项目代码和依赖文件
- [ ] PR 合并到 main

## 21. 本关总结

完整的 Python 项目管理流程：

创建项目 → 创建虚拟环境 → 添加依赖 → 记录依赖 → 锁定版本 → 执行代码 → GitHub 版本管理。

推荐统一使用 WSL2 Ubuntu + Python 3.12 + uv，避免多个工具混用造成混乱。