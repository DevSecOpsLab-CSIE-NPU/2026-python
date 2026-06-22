import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solver import filter_unique_divisible


def test_basic_case():
    nums = [8, 3, 2, 4, 2, 6, 7]
    d = 2
    assert filter_unique_divisible(nums, d) == [8, 2, 4, 6]


def test_no_divisible():
    nums = [1, 3, 5, 7]
    d = 2
    assert filter_unique_divisible(nums, d) == []


def test_all_duplicates():
    nums = [2, 2, 2, 2]
    d = 2
    assert filter_unique_divisible(nums, d) == [2]


def test_zero_divisor_raises():
    nums = [0, 1, 2]
    with pytest.raises(ValueError):
        filter_unique_divisible(nums, 0)
