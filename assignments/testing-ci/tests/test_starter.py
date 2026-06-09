import pytest

from starter_module import sum_list, divide


def test_sum_list_empty():
    assert sum_list([]) == 0


def test_sum_list_values():
    assert sum_list([1, 2, 3]) == 6


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
