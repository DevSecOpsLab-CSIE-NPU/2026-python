"""
UVA 10056 單元測試程式

用途：
1. 驗證解答程式是否正確計算第 i 位玩家獲勝機率
2. 驗證多組輸入輸出格式是否正確（每組一行）

執行方式（在本檔所在資料夾）：
python -m unittest -v test_question_10056.py

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
    "10056.py",
    "uva10056.py",
    "question_10056.py",
    "solution_10056.py",
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
        if p.name != Path(__file__).name and "10056" in p.stem
    )
    if keyword_matches:
        return keyword_matches[0]

    raise FileNotFoundError(
        "找不到可測試的解答程式。請將解答放在同資料夾，或設定 SOLUTION_FILE 環境變數。"
    )


def win_probability(n: int, p: float, i: int) -> float:
    """計算第 i 位玩家最終獲勝機率。"""
    if p == 0.0:
        return 0.0

    q = 1.0 - p

    # 第 i 位第一次可能在第 i 手、或下一輪第 i 手、再下一輪...
    # = p*q^(i-1) * (1 + q^n + q^(2n) + ...)
    # = p*q^(i-1) / (1 - q^n)
    return (p * (q ** (i - 1))) / (1.0 - (q ** n))


class TestUVA10056(unittest.TestCase):
    """針對 UVA 10056 的整體行為測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = find_solution_script()

    def run_solution(self, input_data: str) -> list[float]:
        """以 subprocess 執行解答程式，回傳每行輸出的浮點數。"""
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
            return [float(line) for line in lines]
        except ValueError as exc:
            self.fail(f"輸出包含非浮點數內容：{lines}\n原始錯誤：{exc}")

    def assert_probabilities_close(self, actual: list[float], expected: list[float]) -> None:
        """比對機率值（允許四捨五入到小數點後四位的誤差）。"""
        self.assertEqual(len(actual), len(expected), "輸出行數與預期不一致")
        for idx, (a, e) in enumerate(zip(actual, expected), start=1):
            # 題目要求輸出到小數點後四位，允許 5e-5 級別四捨五入誤差。
            self.assertAlmostEqual(a, e, places=4, msg=f"第 {idx} 行機率不正確")

    def test_known_cases(self) -> None:
        """已知案例：包含一般值與 p=0 邊界。"""
        cases = [
            (3, 0.5, 1),
            (3, 0.5, 2),
            (3, 0.5, 3),
            (5, 0.0, 4),
            (4, 1.0, 1),
            (4, 1.0, 3),
        ]

        lines = [str(len(cases))]
        for n, p, i in cases:
            lines.append(f"{n} {p} {i}")

        input_data = "\n".join(lines) + "\n"
        expected = [win_probability(n, p, i) for n, p, i in cases]
        actual = self.run_solution(input_data)

        self.assert_probabilities_close(actual, expected)

    def test_randomized_cases(self) -> None:
        """隨機案例：以理論公式計算期望值進行比對。"""
        random.seed(10056)

        cases: list[tuple[int, float, int]] = []
        for _ in range(40):
            n = random.randint(1, 30)
            i = random.randint(1, n)

            # 避免只測到太極端，讓 p 分布在 [0, 1]。
            p = random.random()
            if random.random() < 0.1:
                p = 0.0
            elif random.random() < 0.1:
                p = 1.0

            cases.append((n, p, i))

        lines = [str(len(cases))]
        for n, p, i in cases:
            lines.append(f"{n} {p:.8f} {i}")

        input_data = "\n".join(lines) + "\n"
        expected = [win_probability(n, p, i) for n, p, i in cases]
        actual = self.run_solution(input_data)

        self.assert_probabilities_close(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
