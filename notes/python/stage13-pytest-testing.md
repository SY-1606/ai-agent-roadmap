# Python 第十三关：pytest、接口测试与代码质量

## 1. 学习目标

让分层 FastAPI Task API 具备自动化测试能力。

核心知识点：

- assert 断言
- pytest 测试框架
- Test Case 测试用例
- Unit Test 单元测试
- Integration Test 集成测试
- FastAPI TestClient
- fixture 与 conftest.py
- 测试数据库与 Dependency Override
- pytest.raises
- Mock 模拟对象
- Coverage 测试覆盖率
- Ruff 代码检查与格式化
- Regression Testing 回归测试

## 2. 为什么需要自动化测试？

手动打开 Swagger UI 只能验证当前操作。

自动化测试可以在每次修改代码后快速检查原有功能是否正常。

典型流程：

```text
修改代码
→ pytest
→ 检查通过或失败
→ 修复问题
→ commit
```

## 3. assert

assert 是断言语句。

```python
assert 1 + 1 == 2
```

条件为真时继续执行，条件为假时抛出 AssertionError。

测试通常包含输入、实际结果和预期结果之间的比较。

## 4. pytest

pytest 是常用的 Python 测试框架。

安装为开发依赖：

```bash
uv add --dev pytest
```

运行：

```bash
uv run pytest
```

pytest 默认可以发现符合命名规则的测试文件，例如：

```text
test_calculator.py
test_tasks.py
```

测试函数通常使用：

```python
def test_add():
    ...
```

## 5. 开发依赖

开发依赖是在开发和测试阶段使用的工具。

例如：

- pytest
- ruff
- pytest-cov
- httpx（用于 API 测试）

这些通常不属于应用本身运行所必需的核心依赖。

## 6. Test Case 测试用例

一个测试用例对应一个具体场景。

例如：

```python
def test_add_positive():
    assert 2 + 3 == 5
```

还应该测试：

- 0
- 负数
- 空字符串
- 不存在的资源
- 非法参数
- 边界输入

## 7. Unit Test 单元测试

单独验证一个函数或业务逻辑单元。

例如任务标题校验：

```python
assert validate_title(" Python ") == "Python"
```

单元测试应尽量避免依赖真实数据库、网络和外部服务。

## 8. Integration Test 集成测试

验证多个模块共同工作。

例如：

```text
TestClient
→ FastAPI Router
→ Service
→ Repository
→ PostgreSQL 测试数据库
```

一条 CRUD 测试可以验证：

```text
POST 创建
→ GET 查询
→ PUT 更新
→ DELETE 删除
→ GET 返回 404
```

## 9. FastAPI TestClient

TestClient 可以在 Python 测试中模拟 HTTP 请求。

```python
from fastapi.testclient import TestClient

client = TestClient(app)

response = client.get("/")
```

不需要单独启动 Uvicorn。

接口测试不仅要检查 HTTP 状态码，还要检查 JSON 内容。

## 10. 常见 HTTP 测试

正常情况：

- 200：查询成功
- 201：创建成功

异常情况：

- 400：业务请求错误（取决于项目设计）
- 404：资源不存在
- 422：FastAPI / Pydantic 参数校验失败

不同项目的错误处理约定可能不同，应以实际接口契约为准。

## 11. Fixture

pytest.fixture 用于准备重复使用的测试资源。

```python
import pytest

@pytest.fixture
def sample_task():
    return {
        "title": "学习pytest",
        "priority": "high"
    }
```

使用：

```python
def test_sample_task(sample_task):
    assert sample_task["priority"] == "high"
```

pytest 根据函数参数名找到并执行对应 fixture。

## 12. conftest.py

conftest.py 是 pytest 的特殊配置文件。

可以放共享 fixture，例如：

- 测试数据库
- 数据库 Session
- TestClient
- 测试用户

测试文件通常不需要手动导入其中的 fixture。

## 13. 测试数据库

自动化测试不能随便连接开发数据库或生产数据库。

本关约定：

```text
开发数据库：agent_app
测试数据库：agent_app_test
```

测试数据库中的数据可以重建、清理。

正式数据库的数据不能因运行测试而受到影响。

## 14. 测试隔离

测试之间不应依赖彼此创建的数据。

例如：

```text
test_create_task
```

不应该成为：

```text
test_get_task
```

的先决条件。

每条测试应当能独立运行。

## 15. FastAPI Dependency Override

生产环境接口使用：

```python
db: Session = Depends(get_db)
```

测试时可以：

```python
app.dependency_overrides[get_db] = override_get_db
```

这样无需修改 Router，即可将数据库 Session 替换为测试用 Session。

测试结束后应清理覆盖设置。

## 16. pytest.raises

用于断言某段代码应当抛出异常。

```python
import pytest

with pytest.raises(ValueError):
    raise ValueError("错误")
```

也可以检查异常消息：

```python
with pytest.raises(
    ValueError,
    match="优先级不合法"
):
    ...
```

## 17. Mock

Mock 表示模拟对象或模拟行为。

适合测试：

- LLM API
- 外部搜索服务
- 邮件服务
- 支付服务
- 网络请求

例如以后测试 Agent 时，不应每次都真实调用收费模型。

使用固定的模拟返回值能提高测试速度和稳定性。

## 18. Coverage

Coverage（测试覆盖率）衡量测试执行到了多少代码。

安装：

```bash
uv add --dev pytest-cov
```

运行：

```bash
uv run pytest --cov=app
```

覆盖率越高不一定代表测试越好。测试仍然应该重点覆盖关键业务规则、异常路径和边界情况。

## 19. Regression Testing

Regression 表示回归问题。

例如修改 Service 后，让原本正常的 GET /tasks 失效。

回归测试用于发现这种旧功能被新改动破坏的问题。

## 20. Arrange / Act / Assert

推荐测试组织方式：

1. Arrange：准备数据
2. Act：执行被测试操作
3. Assert：断言结果

例如：

```python
def test_add():
    # Arrange
    a, b = 2, 3

    # Act
    result = a + b

    # Assert
    assert result == 5
```

## 21. Ruff

Ruff 是 Python Linter 和 Formatter。

- Linter：静态检查器
- Formatter：代码格式化工具

安装：

```bash
uv add --dev ruff
```

检查：

```bash
uv run ruff check .
```

格式化：

```bash
uv run ruff format .
```

不修改文件的格式检查：

```bash
uv run ruff format --check .
```

## 22. Flaky Test

Flaky Test 是不稳定测试。

可能表现为：

```text
第一次成功
第二次失败
第三次又成功
```

常见原因：

- 网络波动
- 随机数
- 时间依赖
- 数据库数据未隔离
- 外部 API
- 并发时序

应该尽量消除这些依赖。

## 23. Test-Driven Development

TDD（测试驱动开发）的典型循环：

```text
Red：先写失败测试
→ Green：写代码使测试通过
→ Refactor：重构
```

目前先掌握给已有业务补测试，不强制采用 TDD。

## 24. CI 持续集成

CI 全称 Continuous Integration。

未来可以通过 GitHub Actions 自动运行：

```text
push / PR
→ 安装依赖
→ Ruff
→ pytest
→ 输出结果
```

本关先掌握本地测试，CI 工作流以后单独配置。

## 25. 本关验收

- [ ] 安装 pytest、httpx
- [ ] 编写单元测试
- [ ] 使用 FastAPI TestClient
- [ ] 编写 fixture
- [ ] 使用独立测试数据库
- [ ] 覆盖 FastAPI 的 get_db 依赖
- [ ] 测试 200、201、404、422
- [ ] 测试空标题和非法优先级
- [ ] 完成 CRUD 集成测试
- [ ] 会用 pytest.raises
- [ ] 会运行 pytest-cov
- [ ] 会使用 Ruff
- [ ] GitHub PR 合并 main

## 26. 最重要的结论

真正可维护的后端项目不仅要能运行，还要能够被自动验证。

建议每次提交前形成习惯：

```text
编写代码
→ Ruff 格式化
→ Ruff 检查
→ pytest
→ Git 检查
→ Commit
→ Push
```

自动化测试不是替代全部人工检查，而是降低重复验证的成本并及时发现回归问题。