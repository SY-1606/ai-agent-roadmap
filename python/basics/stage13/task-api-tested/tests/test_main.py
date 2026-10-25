def test_root_success(client):
    # Arrange：无需额外数据

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Task API is running"
    assert "Router" in data["architecture"]
    assert "Service" in data["architecture"]
    assert "Repository" in data["architecture"]
