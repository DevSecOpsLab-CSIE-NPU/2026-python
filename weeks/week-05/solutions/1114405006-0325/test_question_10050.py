"""
UVA 10050 單元測試程式

用途：
1. 驗證解答程式是否正確計算罷會造成的工作天損失
2. 驗證多組輸入輸出的格式是否正確

執行方式（在本檔所在資料夾）：
python -m unittest -v test_question_10050.py

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
    "10050.py",
    "uva10050.py",
    "question_10050.py",
    "solution_10050.py",
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
        if p.name != Path(__file__).name and "10050" in p.stem
    )
    if keyword_matches:
        return keyword_matches[0]

    raise FileNotFoundError(
        "找不到可測試的解答程式。請將解答放在同資料夾，或設定 SOLUTION_FILE 環境變數。"
    )


def expected_lost_days(n: int, hartals: list[int]) -> int:
    """依題意計算 N 天內的罷會損失工作天數。"""
    lost = set()

    # Day 1 是星期日，因此：
    # day % 7 == 6 為星期五，day % 7 == 0 為星期六。
    for h in hartals:
        day = h
        while day <= n:
            if day % 7 not in (6, 0):
                lost.add(day)
            day += h

    return len(lost)


class TestUVA10050(unittest.TestCase):
    """針對 UVA 10050 的整體行為測試。"""

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

    def test_statement_example(self) -> None:
        """題目敘述案例：N=14, h=[3,4,8]，答案應為 5。"""
        input_data = "\n".join([
            "1",
            "14",
            "3",
            "3",
            "4",
            "8",
        ]) + "\n"
        expected = [5]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_overlap_and_weekend(self) -> None:
        """重疊與假日排除：同一天被多政黨命中也只算一次，週五週六不算。"""
        input_data = "\n".join([
            "1",
            "30",
            "3",
            "2",
            "3",
            "4",
        ]) + "\n"
        expected = [expected_lost_days(30, [2, 3, 4])]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_single_week_no_loss(self) -> None:
        """僅命中假日時，損失應為 0。"""
        input_data = "\n".join([
            "1",
            "14",
            "1",
            "7",
        ]) + "\n"
        # h=7 會落在 day 7,14,...（星期六），都不計入。
        expected = [0]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_randomized_cases(self) -> None:
        """隨機案例：用理論值比對，提高覆蓋率。"""
        random.seed(10050)

        cases: list[tuple[int, list[int]]] = []
        for _ in range(25):
            n = random.randint(7, 200)
            p = random.randint(1, 8)

            # 題目保證 hi 不會是 7 的倍數。
            hs: list[int] = []
            while len(hs) < p:
                h = random.randint(1, 30)
                if h % 7 != 0:
                    hs.append(h)

            cases.append((n, hs))

        lines = [str(len(cases))]
        for n, hs in cases:
            lines.append(str(n))
            lines.append(str(len(hs)))
            lines.extend(str(h) for h in hs)

        input_data = "\n".join(lines) + "\n"
        expected = [expected_lost_days(n, hs) for n, hs in cases]
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
