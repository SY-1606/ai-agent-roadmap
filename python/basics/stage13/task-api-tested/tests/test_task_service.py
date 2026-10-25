import pytest

from app.services.task_service import validate_task


def test_validate_task_success():
    result = validate_task(
        "  学习pytest  ",
        "high",
    )

    assert result == "学习pytest"


def test_validate_task_empty_title():
    with pytest.raises(
        ValueError,
        match="任务标题不能为空",
    ):
        validate_task(
            "",
            "high",
        )


def test_validate_task_only_spaces():
    with pytest.raises(
        ValueError,
        match="任务标题不能为空",
    ):
        validate_task(
            "   ",
            "medium",
        )


def test_validate_task_invalid_priority():
    with pytest.raises(
        ValueError,
        match="优先级不合法",
    ):
        validate_task(
            "学习测试",
            "urgent",
        )


@pytest.mark.parametrize(
    "priority",
    ["high", "medium", "low"],
)
def test_validate_task_allowed_priorities(priority):
    result = validate_task(
        "学习Python",
        priority,
    )

    assert result == "学习Python"
