"""
UVA 10041 單元測試程式

用途：
1. 驗證解答程式是否正確計算最小總距離
2. 驗證多組輸入輸出的格式是否正確

執行方式（在本檔所在資料夾）：
python -m unittest -v test_question_10041.py

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
    "10041.py",
    "uva10041.py",
    "question_10041.py",
    "solution_10041.py",
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
        if p.name != Path(__file__).name and "10041" in p.stem
    )
    if keyword_matches:
        return keyword_matches[0]

    raise FileNotFoundError(
        "找不到可測試的解答程式。請將解答放在同資料夾，或設定 SOLUTION_FILE 環境變數。"
    )


def expected_min_total_distance(addresses: list[int]) -> int:
    """利用中位數性質計算理論最小總距離。"""
    ordered = sorted(addresses)
    median = ordered[len(addresses) // 2]
    return sum(abs(x - median) for x in ordered)


class TestUVA10041(unittest.TestCase):
    """針對 UVA 10041 的整體行為測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = find_solution_script()

    def run_solution(self, input_data: str) -> list[int]:
        """以 subprocess 執行解答程式，回傳每行輸出的整數。"""
        completed = subprocess.run(
            [sys.executable, str(self.solution)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=str(BASE_DIR),
            timeout=5,
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
        try:
            return [int(line) for line in lines]
        except ValueError as exc:
            self.fail(f"輸出包含非整數內容：{lines}\n原始錯誤：{exc}")

    def test_basic_cases(self) -> None:
        """基本案例：偶數與奇數筆數。"""
        input_data = "\n".join([
            "2",
            "2 2 4",
            "3 2 4 6",
        ]) + "\n"
        expected = [2, 4]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_with_duplicate_addresses(self) -> None:
        """重複門牌案例：題目允許相同地址。"""
        input_data = "\n".join([
            "1",
            "5 10 10 10 20 20",
        ]) + "\n"
        expected = [20]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_unsorted_even_count(self) -> None:
        """未排序且偶數筆數：檢查是否正確處理中位數區間。"""
        input_data = "\n".join([
            "1",
            "4 1 2 100 101",
        ]) + "\n"
        expected = [198]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_randomized_cases(self) -> None:
        """隨機案例：用理論值比對，提高覆蓋率。"""
        random.seed(10041)

        test_cases: list[list[int]] = []
        for _ in range(30):
            r = random.randint(1, 15)
            addresses = [random.randint(1, 200) for _ in range(r)]
            test_cases.append(addresses)

        lines = [str(len(test_cases))]
        for addresses in test_cases:
            parts = [str(len(addresses))] + [str(x) for x in addresses]
            lines.append(" ".join(parts))

        input_data = "\n".join(lines) + "\n"
        expected = [expected_min_total_distance(a) for a in test_cases]
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
