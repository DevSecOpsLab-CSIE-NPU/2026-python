"""
針對 `solution_10929-easy.py` 的 pytest 測試檔。

因為檔名含有 `-`，無法直接用一般 import，這裡改用 importlib 依檔案路徑載入。
"""

import importlib.util
from pathlib import Path


def load_easy_module():
    """從目前資料夾載入 easy 版模組。"""
    folder = Path(__file__).resolve().parent
    path = folder / 'solution_10929-easy.py'
    spec = importlib.util.spec_from_file_location('solution_10929_easy', str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_easy_version():
    # 取得函式
    mod = load_easy_module()
    f = mod.is_multiple_of_11_easy

    # 可被 11 整除
    assert f('11') is True
    assert f('121') is True
    assert f('1001') is True

    # 不可被 11 整除
    assert f('1') is False
    assert f('123') is False
    assert f('101') is False

    # 大位數輸入，確認是字串處理
    assert f('1' * 999 + '2') is False

    # 前導零
    assert f('0011') is True
    assert f('0101') is False
