from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 用路徑載入檔案，讓測試可以同時驗證正式版與 easy 版。
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


STANDARD_MODULE = load_module("10050.py", "solution_10050")
EASY_MODULE = load_module("10050-easy.py", "solution_10050_easy")
HAND_MODULE = load_module("10050-hand.py", "solution_10050_hand")


def test_sample_cases() -> None:
    # 這是 Hartals 最常見的範例，第二組要正確排除週末。
    input_data = "2\n14\n3\n3\n4\n8\n100\n4\n12\n15\n25\n40\n"
    expected = "5\n15"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected


def test_overlapping_strikes() -> None:
    # 不同政黨撞在同一天時，損失天數只能算一次。
    input_data = "1\n15\n2\n2\n3\n"
    expected = "8"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected