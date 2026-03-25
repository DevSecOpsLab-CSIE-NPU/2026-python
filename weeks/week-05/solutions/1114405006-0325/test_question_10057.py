"""
UVA 10057 單元測試程式

用途：
1. 驗證解答程式是否正確輸出三個整數：A、人數、可能 A 的個數
2. 驗證 EOF 多組輸入格式

執行方式（在本檔所在資料夾）：
python -m unittest -v test_question_10057.py

可選環境變數：
SOLUTION_FILE=你的解答檔名.py
"""

from __future__ import annotations

import os
import random
import subprocess
import sys
import unittest
from pathlib import Path


# 測試檔所在目錄，預期解答程式也會放在同一層
BASE_DIR = Path(__file__).resolve().parent

# 優先嘗試這些常見檔名
CANDIDATE_FILES = [
    "10057.py",
    "uva10057.py",
    "question_10057.py",
    "solution_10057.py",
    "main.py",
]


def find_solution_script() -> Path:
    """找出要測試的解答程式檔案路徑。"""
    env_file = os.environ.get("SOLUTION_FILE")
    if env_file:
        path = BASE_DIR / env_file
        if path.exists() and path.is_file():
            return path

    for name in CANDIDATE_FILES:
        path = BASE_DIR / name
        if path.exists() and path.is_file():
            return path

    # 若固定檔名都找不到，嘗試用題號關鍵字搜尋
    keyword_matches = sorted(
        p
        for p in BASE_DIR.glob("*.py")
        if p.name != Path(__file__).name and "10057" in p.stem
    )
    if keyword_matches:
        return keyword_matches[0]

    raise FileNotFoundError(
        "找不到可測試的解答程式。請將解答放在同資料夾，或設定 SOLUTION_FILE 環境變數。"
    )


def expected_result(values: list[int]) -> tuple[int, int, int]:
    """計算單一測資的期望輸出 (A, 人數, 可能 A 個數)。"""
    ordered = sorted(values)
    n = len(ordered)

    if n % 2 == 1:
        a = ordered[n // 2]
        cnt = sum(1 for x in ordered if x == a)
        ways = 1
        return a, cnt, ways

    low = ordered[n // 2 - 1]
    high = ordered[n // 2]

    # 偶數個元素時，A 可在 [low, high] 之間任意整數。
    a = low
    cnt = sum(1 for x in ordered if low <= x <= high)
    ways = high - low + 1
    return a, cnt, ways


class TestUVA10057(unittest.TestCase):
    """針對 UVA 10057 的整體行為測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = find_solution_script()

    def run_solution(self, input_data: str) -> list[tuple[int, int, int]]:
        """以 subprocess 執行解答程式，回傳每行三個整數。"""
        completed = subprocess.run(
            [sys.executable, str(self.solution)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=str(BASE_DIR),
            timeout=6,
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=(
                "解答程式執行失敗\n"
                f"return code: {completed.returncode}\n"
                f"stderr:\n{completed.stderr}"
            ),
        )

        lines = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
        parsed: list[tuple[int, int, int]] = []

        for line in lines:
            parts = line.split()
            if len(parts) != 3:
                self.fail(f"每行輸出應有 3 個整數，實際為：{line}")
            try:
                a, b, c = map(int, parts)
            except ValueError as exc:
                self.fail(f"輸出包含非整數內容：{line}\n原始錯誤：{exc}")
            parsed.append((a, b, c))

        return parsed

    def test_small_fixed_cases(self) -> None:
        """固定案例：奇偶長度、重複值、區間多解。"""
        cases = [
            [1, 2, 3, 4],          # 偶數：A 可為 2 或 3
            [1, 1, 1, 1],          # 全相同
            [1, 2, 2, 3, 4],       # 奇數，且中位數重複
            [10, 20],              # 偶數，區間大於 1
            [5],                   # 單一元素
        ]

        lines: list[str] = []
        for arr in cases:
            lines.append(str(len(arr)))
            lines.append(" ".join(map(str, arr)))

        input_data = "\n".join(lines) + "\n"
        expected = [expected_result(arr) for arr in cases]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_randomized_cases(self) -> None:
        """隨機案例：用理論函式比對答案。"""
        random.seed(10057)

        cases: list[list[int]] = []
        for _ in range(35):
            n = random.randint(1, 40)
            arr = [random.randint(0, 120) for _ in range(n)]
            cases.append(arr)

        lines: list[str] = []
        for arr in cases:
            lines.append(str(len(arr)))
            lines.append(" ".join(map(str, arr)))

        input_data = "\n".join(lines) + "\n"
        expected = [expected_result(arr) for arr in cases]
        actual = self.run_solution(input_data)

        self.assertEqual(
            actual,
            expected,
            msg=(
                "隨機測資比對失敗\n"
                f"expected: {expected}\n"
                f"actual:   {actual}"
            ),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
