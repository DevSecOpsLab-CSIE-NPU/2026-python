from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 直接從檔案路徑載入，避免檔名格式影響 import。
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


STANDARD_MODULE = load_module("10055.py", "solution_10055")
EASY_MODULE = load_module("10055-easy.py", "solution_10055_easy")
HAND_MODULE = load_module("10055-hand.py", "solution_10055_hand")


def test_multiple_pairs() -> None:
    # 連續多組 EOF 輸入時，應逐行輸出差值。
    input_data = "10 12\n10 14\n100 200\n"
    expected = "2\n4\n100"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected


def test_large_difference() -> None:
    # Python 整數沒有固定長度限制，應可正確處理大數差值。
    input_data = "0 4294967295\n"
    expected = "4294967295"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected