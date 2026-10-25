def test_create_task_success(client):
    # Arrange
    payload = {
        "title": "学习pytest",
        "priority": "high",
    }

    # Act
    response = client.post(
        "/tasks",
        json=payload,
    )

    # Assert
    assert response.status_code == 201

    data = response.json()

    assert data["id"] > 0
    assert data["title"] == "学习pytest"
    assert data["priority"] == "high"
    assert data["done"] is False


def test_get_tasks_empty(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_missing_title(client):
    response = client.post(
        "/tasks",
        json={
            "priority": "high",
        },
    )

    assert response.status_code == 422


def test_create_task_invalid_priority(client):
    response = client.post(
        "/tasks",
        json={
            "title": "测试任务",
            "priority": "urgent",
        },
    )

    # Stage 11 使用 Literal 类型校验，
    # 因此非法 priority 会由 Pydantic 返回 422
    assert response.status_code == 422


def test_create_task_empty_title(client):
    response = client.post(
        "/tasks",
        json={
            "title": "",
            "priority": "high",
        },
    )

    assert response.status_code == 422


def test_create_task_spaces_title(client):
    response = client.post(
        "/tasks",
        json={
            "title": "   ",
            "priority": "high",
        },
    )

    # Pydantic 允许空格字符串，
    # Service 进一步校验并返回业务错误
    assert response.status_code == 400
    assert response.json()["detail"] == "任务标题不能为空"


def test_get_missing_task(client):
    response = client.get("/tasks/999999999")

    assert response.status_code == 404

    assert response.json() == {"detail": "任务不存在"}


def test_filter_tasks_by_priority(client):
    client.post(
        "/tasks",
        json={
            "title": "高优先级任务",
            "priority": "high",
        },
    )

    client.post(
        "/tasks",
        json={
            "title": "低优先级任务",
            "priority": "low",
        },
    )

    response = client.get(
        "/tasks",
        params={"priority": "high"},
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 1
    assert tasks[0]["priority"] == "high"


def test_search_tasks(client):
    client.post(
        "/tasks",
        json={
            "title": "学习Python",
            "priority": "high",
        },
    )

    client.post(
        "/tasks",
        json={
            "title": "学习数据库",
            "priority": "medium",
        },
    )

    response = client.get(
        "/tasks/search",
        params={"keyword": "Python"},
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "学习Python"


def test_complete_task(client):
    created = client.post(
        "/tasks",
        json={
            "title": "待完成任务",
            "priority": "medium",
        },
    )

    task_id = created.json()["id"]

    response = client.patch(f"/tasks/{task_id}/complete")

    assert response.status_code == 200
    assert response.json()["done"] is True


def test_task_crud_flow(client):
    # 1. Create
    create_response = client.post(
        "/tasks",
        json={
            "title": "CRUD测试",
            "priority": "medium",
        },
    )

    assert create_response.status_code == 201

    task = create_response.json()
    task_id = task["id"]

    # 2. Read
    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 200
    assert get_response.json()["title"] == "CRUD测试"

    # 3. Update
    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "CRUD测试修改",
            "priority": "high",
            "done": True,
        },
    )

    assert update_response.status_code == 200

    updated = update_response.json()

    assert updated["title"] == "CRUD测试修改"
    assert updated["priority"] == "high"
    assert updated["done"] is True

    # 4. Delete
    delete_response = client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 200

    # 5. Verify deleted
    missing_response = client.get(f"/tasks/{task_id}")

    assert missing_response.status_code == 404
