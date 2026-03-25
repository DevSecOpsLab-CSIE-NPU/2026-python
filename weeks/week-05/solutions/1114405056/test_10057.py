from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 用檔案路徑載入，讓標準版與 easy 版都能以同一份測試驗證。
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


STANDARD_MODULE = load_module("10057.py", "solution_10057")
EASY_MODULE = load_module("10057-easy.py", "solution_10057_easy")
HAND_MODULE = load_module("10057-hand.py", "solution_10057_hand")


def test_odd_and_even_cases() -> None:
    # 同時驗證奇數與偶數長度資料的中位數規則。
    input_data = "5\n1 2 3 4 5\n6\n1 1 1 2 3 3\n10\n1 2 3 4 5 6 7 8 9 10\n"
    expected = "3 1 1\n1 4 2\n5 2 2"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected


def test_all_same_numbers() -> None:
    # 所有數字都一樣時，最佳答案只有那個值本身。
    input_data = "4\n7 7 7 7\n"
    expected = "7 4 1"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected