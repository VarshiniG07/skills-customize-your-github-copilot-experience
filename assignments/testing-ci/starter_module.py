from typing import List


def sum_list(values: List[int]) -> int:
    """Return the sum of the given list of integers."""
    return sum(values)


def divide(a: int, b: int) -> float:
    """Return a / b. Raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
