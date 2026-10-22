
def add(a: float, b: float) -> float:
    """返回两个数的和。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """返回两个数的差。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """返回两个数的积。"""
    return a * b


def divide(a: float, b: float) -> float | None:
    """除数为零时返回 None。"""
    if b == 0:
        return None
    return a / b
