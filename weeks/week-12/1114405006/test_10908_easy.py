"""
測試 `solution_10908-easy.py`（檔名包含 '-'，以 importlib 動態載入）

測試內容與 `test_10908.py` 相同，以確保簡易版行為一致。
"""

import importlib.util
from pathlib import Path


def load_mod(path: Path):
    spec = importlib.util.spec_from_file_location("sol10908_easy", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_easy_matches():
    folder = Path(__file__).resolve().parent
    mod = load_mod(folder / "solution_10908-easy.py")
    f = mod.largest_square

    grid = [
        list("abbbaaaaaa"),
        list("abbbaaaaaa"),
        list("abbbaaaaaa"),
        list("aaaaaaaaaa"),
        list("aaaaaaaaaa"),
        list("aaccaaaaaa"),
        list("aaccaaaaaa"),
    ]
    queries = [(1, 2), (2, 4), (4, 6), (5, 2)]
    expected = [3, 1, 5, 1]
    for (r, c), exp in zip(queries, expected):
        assert f(grid, r, c) == exp

    # 邊界檢查
    assert f([["x"]], 0, 0) == 1
    grid2 = [list("aaaa"), list("aaaa"), list("aaaa"), list("aaaa")]
    assert f(grid2, 1, 1) == 3
    assert f([list("abc"), list("def"), list("ghi")], 0, 1) == 1
