import os
import subprocess
import sys
import unittest
from pathlib import Path


# ============================================================
# 這份是「好記版」測試：
# 1) 先找到解答程式
# 2) 丟入測資執行
# 3) 比對輸出是否和預期一致
# ============================================================


def find_target_script() -> Path:
    """找 10189 的解答檔。

    優先順序：
    1. 環境變數 TARGET_10189
    2. 與本測試檔同資料夾中的常見檔名
    3. 若都找不到就跳過測試（避免整包直接失敗）
    """
    custom_path = os.environ.get("TARGET_10189")
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    folder = Path(__file__).resolve().parent
    names = [
        "QUESTION-10189-手打.py",
        "QUESTION-10189.py",
        "question_10189.py",
        "uva10189.py",
        "10189.py",
        "solution_10189.py",
    ]

    for name in names:
        p = folder / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10189 解答檔，請放同資料夾或設定 TARGET_10189")


def run_program(input_text: str) -> str:
    """執行目標程式，回傳標準輸出文字。"""
    script = find_target_script()
    result = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def normalize_for_compare(text: str) -> str:
    """標準化輸出，避免因尾端空白造成誤判。

    注意：
    - 我們只去掉每行「右側空白」
    - 會保留主要行結構，仍可檢查格式
    """
    lines = text.strip().splitlines()
    lines = [line.rstrip() for line in lines]
    return "\n".join(lines)


class Test10189Easy(unittest.TestCase):
    """UVA 10189（Minesweeper）好記版測試。"""

    def test_official_sample(self):
        # 題目範例：最重要，通常先確保這筆會過。
        input_text = (
            "4 4\n"
            "*...\n"
            "....\n"
            ".*..\n"
            "....\n"
            "3 5\n"
            "**...\n"
            ".....\n"
            ".*...\n"
            "0 0\n"
        )
        expected = (
            "Field #1:\n"
            "*100\n"
            "2210\n"
            "1*10\n"
            "1110\n"
            "\n"
            "Field #2:\n"
            "**100\n"
            "33200\n"
            "1*100\n"
        )

        actual = run_program(input_text)
        self.assertEqual(normalize_for_compare(actual), normalize_for_compare(expected))

    def test_one_cell_dot(self):
        # 1x1 且是空白格，答案應該是 0。
        input_text = "1 1\n.\n0 0\n"
        expected = "Field #1:\n0\n"
        actual = run_program(input_text)
        self.assertEqual(normalize_for_compare(actual), normalize_for_compare(expected))

    def test_one_cell_mine(self):
        # 1x1 且是地雷，答案就維持 *。
        input_text = "1 1\n*\n0 0\n"
        expected = "Field #1:\n*\n"
        actual = run_program(input_text)
        self.assertEqual(normalize_for_compare(actual), normalize_for_compare(expected))


if __name__ == "__main__":
    unittest.main()
