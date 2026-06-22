import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solver import filter_unique_divisible


def test_red_light_next_requirement():
    # 這個測試目前會失敗，作為紅燈測試示例。
    nums = [8, 3, 2, 4, 2, 6, 7]
    d = 2
    assert filter_unique_divisible(nums, d) == [2, 4, 6]
