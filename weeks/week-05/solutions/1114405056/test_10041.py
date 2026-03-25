from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 以檔案路徑載入題解，避免檔名含數字或連字號時不好直接 import。
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


STANDARD_MODULE = load_module("10041.py", "solution_10041")
EASY_MODULE = load_module("10041-easy.py", "solution_10041_easy")
HAND_MODULE = load_module("10041-hand.py", "solution_10041_hand")


def test_sample_cases() -> None:
    # 驗證常見範例：中位數位置能得到最小總距離。
    input_data = "2\n2 2 4\n3 2 4 6\n"
    expected = "2\n4"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected


def test_duplicate_addresses() -> None:
    # 親戚地址可重複，程式應正確處理。
    input_data = "1\n5 1 1 2 10 10\n"
    expected = "18"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected