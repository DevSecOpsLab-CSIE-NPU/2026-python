"""
針對 `solution_10922-easy.py` 的 pytest 測試。

因為檔名含有 `-`，不能直接用一般 import，這裡改用 importlib 依路徑載入。
"""

import importlib.util
from pathlib import Path


def load_easy_module():
    """從目前資料夾載入簡易版模組。"""
    folder = Path(__file__).resolve().parent
    path = folder / 'solution_10922-easy.py'
    spec = importlib.util.spec_from_file_location('solution_10922_easy', str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_easy_version():
    # 取得函式
    mod = load_easy_module()
    f = mod.nine_degree_easy

    # 不是 9 的倍數
    assert f('123') is None
    assert f('10') is None

    # 基本案例
    assert f('9') == 1
    assert f('18') == 2
    assert f('99') == 3

    # 長數字
    assert f('999999999') == 3

    # 前導零
    assert f('009') == 1
    assert f('018') == 2
