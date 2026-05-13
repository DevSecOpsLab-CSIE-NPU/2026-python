"""
UVA 10931 — Parity 簡易版的 pytest 測試。

這份測試主要確認 easy 版是否和正式版一樣：
- 二進位轉換正確
- 1 的個數計算正確
- 輸出格式正確

因為檔名含有 `-`，所以使用 importlib 透過路徑載入模組。
"""

import importlib.util
from pathlib import Path

import pytest


def load_easy_module():
    """從檔案路徑載入 easy 版模組。"""
    module_path = Path(__file__).resolve().parent / 'solution_10931-easy.py'
    spec = importlib.util.spec_from_file_location('solution_10931_easy', str(module_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


solution = load_easy_module()


@pytest.mark.parametrize(
    'num, expected_binary, expected_ones',
    [
        (1, '1', 1),
        (2, '10', 1),
        (10, '1010', 2),
        (21, '10101', 3),
        (4, '100', 1),
        (8, '1000', 1),
        (31, '11111', 5),
        (100, '1100100', 3),
        (2147483647, bin(2147483647)[2:], bin(2147483647)[2:].count('1')),
    ],
)
def test_parity_easy(num, expected_binary, expected_ones):
    """確認 easy 版能正確回傳二進位字串與 1 的個數。"""
    binary_str, ones = solution.parity_easy(num)
    assert binary_str == expected_binary
    assert ones == expected_ones


def test_output_format_easy():
    """確認輸出格式符合題目要求。"""
    binary_str, ones = solution.parity_easy(21)
    assert f'The parity of {binary_str} is {ones} (mod 2).' == 'The parity of 10101 is 3 (mod 2).'
