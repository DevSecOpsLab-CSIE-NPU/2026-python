"""
UVA 10055 單元測試程式

用途：
1. 驗證解答程式是否正確處理「反轉」與「區間查詢」
2. 驗證輸入輸出格式是否正確

執行方式（在本檔所在資料夾）：
python -m unittest -v test_question_10055.py

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
    "10055.py",
    "uva10055.py",
    "question_10055.py",
    "solution_10055.py",
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
        if p.name != Path(__file__).name and "10055" in p.stem
    )
    if keyword_matches:
        return keyword_matches[0]

    raise FileNotFoundError(
        "找不到可測試的解答程式。請將解答放在同資料夾，或設定 SOLUTION_FILE 環境變數。"
    )


def expected_answers(n: int, operations: list[tuple[int, int, int]]) -> list[int]:
    """使用直接模擬計算所有查詢的正確答案。"""
    # 0 代表增函數、1 代表減函數；初始全部是增函數。
    state = [0] * (n + 1)
    out: list[int] = []

    for op in operations:
        if op[0] == 1:
            _, i, _ = op
            state[i] ^= 1
        else:
            _, l, r = op
            # 區間內減函數數量為奇數 => 複合後為減函數（輸出 1）
            out.append(sum(state[l : r + 1]) % 2)

    return out


class TestUVA10055(unittest.TestCase):
    """針對 UVA 10055 的整體行為測試。"""

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
        try:
            return [int(line) for line in lines]
        except ValueError as exc:
            self.fail(f"輸出包含非整數內容：{lines}\n原始錯誤：{exc}")

    def test_basic_toggle_and_query(self) -> None:
        """基本反轉與查詢流程。"""
        input_data = "\n".join([
            "5 7",
            "2 1 5",
            "1 3",
            "2 1 5",
            "1 1",
            "2 1 3",
            "1 3",
            "2 2 5",
        ]) + "\n"

        # 手算：
        # 初始全增 -> [1,5] 為增 => 0
        # flip 3 之後 [1,5] 有 1 個減 => 1
        # flip 1 之後 [1,3] 有 2 個減 => 0
        # flip 3 還原後 [2,5] 有 0 個減 => 0
        expected = [0, 1, 0, 0]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_single_point_queries(self) -> None:
        """單點查詢可直接檢查該函數當前狀態。"""
        input_data = "\n".join([
            "4 6",
            "2 2 2",
            "1 2",
            "2 2 2",
            "1 2",
            "2 2 2",
            "2 1 1",
        ]) + "\n"

        # f2: 增 -> 減 -> 增
        expected = [0, 1, 0, 0]
        actual = self.run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_randomized_cases(self) -> None:
        """隨機案例：用直接模擬比對答案。"""
        random.seed(10055)

        n = 60
        q = 220
        ops: list[tuple[int, int, int]] = []

        for _ in range(q):
            if random.random() < 0.45:
                i = random.randint(1, n)
                ops.append((1, i, 0))
            else:
                l = random.randint(1, n)
                r = random.randint(l, n)
                ops.append((2, l, r))

        lines = [f"{n} {q}"]
        for op, a, b in ops:
            if op == 1:
                lines.append(f"1 {a}")
            else:
                lines.append(f"2 {a} {b}")

        input_data = "\n".join(lines) + "\n"
        expected = expected_answers(n, ops)
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
