import os
import subprocess
import sys
import unittest
from pathlib import Path


def _find_solution_script() -> Path:
    """尋找 10189 解答程式位置；可由環境變數覆寫。"""
    custom = os.environ.get("TARGET_10189")
    if custom:
        p = Path(custom)
        if p.exists():
            return p

    base = Path(__file__).resolve().parent
    candidates = [
        "QUESTION-10189-手打.py",
        "QUESTION-10189.py",
        "question_10189.py",
        "uva10189.py",
        "10189.py",
        "solution_10189.py",
    ]
    for name in candidates:
        p = base / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10189 解答程式，請先放入同資料夾或設定 TARGET_10189")


def _run_solution(input_data: str) -> str:
    script = _find_solution_script()
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout


def _normalize(text: str) -> str:
    # 只移除每行行尾空白，保留題目要求的空白行結構。
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


class TestQuestion10189(unittest.TestCase):
    """UVA 10189 Minesweeper 測試。"""

    def test_sample(self):
        input_data = (
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
        actual = _run_solution(input_data)
        self.assertEqual(_normalize(actual), _normalize(expected))

    def test_single_empty_cell(self):
        input_data = "1 1\n.\n0 0\n"
        expected = "Field #1:\n0\n"
        actual = _run_solution(input_data)
        self.assertEqual(_normalize(actual), _normalize(expected))

    def test_single_mine_cell(self):
        input_data = "1 1\n*\n0 0\n"
        expected = "Field #1:\n*\n"
        actual = _run_solution(input_data)
        self.assertEqual(_normalize(actual), _normalize(expected))


if __name__ == "__main__":
    unittest.main()
