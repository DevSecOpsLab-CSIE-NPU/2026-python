"""
測試 `solution-easy.py` 的簡易測試。

因檔名含 '-' 不能直接用 import 模組名稱，故使用 importlib 由檔案路徑載入模組。
"""

import importlib.util
from pathlib import Path
import pytest


def load_module_from_path(path: Path):
    spec = importlib.util.spec_from_file_location("solution_easy", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_solution_easy_matches():
    folder = Path(__file__).resolve().parent
    mod = load_module_from_path(folder / "solution-easy.py")
    compute = mod.compute_scores

    # 與原本測試相同的用例
    assert compute(40, 20) == (30, 10)
    with pytest.raises(ValueError):
        compute(20, 40)
    with pytest.raises(ValueError):
        compute(1, 0)
    assert compute(1, 1) == (1, 0)
    assert compute(0, 0) == (0, 0)
    assert compute(5, 3) == (4, 1)
    with pytest.raises(ValueError):
        compute(10, 12)
    with pytest.raises(ValueError):
        compute(2, 3)
