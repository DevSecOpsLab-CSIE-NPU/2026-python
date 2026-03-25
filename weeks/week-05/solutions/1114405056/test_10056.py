from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(file_name: str, module_name: str):
    # 以路徑載入，方便同時測正式版與 easy 版。
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


STANDARD_MODULE = load_module("10056.py", "solution_10056")
EASY_MODULE = load_module("10056-easy.py", "solution_10056_easy")
HAND_MODULE = load_module("10056-hand.py", "solution_10056_hand")


def test_sample_probabilities() -> None:
    # 驗證題目的典型情境與四捨五入到小數點後四位。
    input_data = "3\n2 0.166666 1\n2 0.166666 2\n10 0.5 1\n"
    expected = "0.5455\n0.4545\n0.5005"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected


def test_zero_success_probability() -> None:
    # 如果單次成功機率是 0，答案必定是 0.0000。
    input_data = "1\n5 0.0 3\n"
    expected = "0.0000"

    assert STANDARD_MODULE.solve(input_data) == expected
    assert EASY_MODULE.solve(input_data) == expected
    assert HAND_MODULE.solve(input_data) == expected