"""UVA/ZeroJudge 10062（本題敘述為乳牛排序）單元測試。

使用方式：
1) 將你的解答程式放在同一資料夾（預設會自動嘗試多個常見檔名）。
2) 執行：python -m unittest test_10062.py -v

可選：
- 若你的檔名不同，可設定環境變數 SOLUTION_FILE 指定路徑。
"""

import importlib.util
import io
import os
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from typing import List


# 會依序嘗試這些常見檔名
CANDIDATE_FILES = [
    "solution.py",
    "main.py",
    "10062.py",
    "uva10062.py",
    "uva_10062.py",
    "question_10062.py",
    "QUESTION-10062.py",
]


def _normalize_output(text: str) -> str:
    """將輸出標準化：去除前後空白、統一換行。"""
    lines = [line.rstrip() for line in text.strip().splitlines()]
    return "\n".join(lines).strip()


def _build_input_from_permutation(perm: List[int]) -> str:
    """由正確排列產生題目輸入（第 2..N 行的計數資料）。"""
    n = len(perm)
    counts = []
    for i in range(1, n):
        # a[i] = 在第 i 個位置前面，編號比目前牛小的數量
        smaller_before = sum(1 for x in perm[:i] if x < perm[i])
        counts.append(smaller_before)
    return str(n) + "\n" + "\n".join(map(str, counts)) + "\n"


def _reference_decode(input_data: str) -> List[int]:
    """參考解碼器：由題目輸入重建最終排列（作為測試 oracle）。"""
    nums = [int(x) for x in input_data.strip().split()]
    n = nums[0]
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = nums[i - 1]

    available = list(range(1, n + 1))
    ans = [0] * (n + 1)

    # 由後往前還原：第 i 位置要選擇剩餘數字中的第 (a[i] + 1) 小
    for i in range(n, 0, -1):
        idx = a[i]
        ans[i] = available.pop(idx)

    return ans[1:]


class StudentRunner:
    """負責找到學生程式並提供統一執行介面。"""

    def __init__(self) -> None:
        self.test_dir = Path(__file__).resolve().parent
        self.solution_file = self._find_solution_file()

    def _find_solution_file(self) -> Path:
        env_path = os.environ.get("SOLUTION_FILE")
        if env_path:
            p = Path(env_path).expanduser().resolve()
            if p.exists() and p.suffix == ".py":
                return p
            raise FileNotFoundError(f"SOLUTION_FILE 不存在或非 Python 檔：{p}")

        for name in CANDIDATE_FILES:
            p = self.test_dir / name
            if p.exists():
                return p

        raise FileNotFoundError(
            "找不到解答程式。請將解答放在同資料夾，或用 SOLUTION_FILE 指定路徑。"
        )

    def run(self, input_data: str) -> str:
        """優先嘗試呼叫 solve(input_str)，否則退回 subprocess 執行檔案。"""
        module = self._try_load_module(self.solution_file)
        if module is not None and hasattr(module, "solve") and callable(module.solve):
            result = module.solve(input_data)
            if not isinstance(result, str):
                result = str(result)
            return _normalize_output(result)

        # 若沒有 solve，改用子行程模擬線上評測輸入輸出
        proc = subprocess.run(
            [sys.executable, str(self.solution_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                "解答程式執行失敗。\n"
                f"returncode={proc.returncode}\n"
                f"stderr=\n{proc.stderr}"
            )
        return _normalize_output(proc.stdout)

    @staticmethod
    def _try_load_module(path: Path):
        try:
            spec = importlib.util.spec_from_file_location("student_solution", path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            # 匯入失敗時，改走 subprocess 路徑以兼容腳本型解法
            return None


class TestUVA10062(unittest.TestCase):
    """針對題意（重建排列）設計的測試。"""

    @classmethod
    def setUpClass(cls):
        cls.runner = StudentRunner()

    def assert_solution(self, input_data: str, expected_perm: List[int]):
        expected = "\n".join(map(str, expected_perm))
        output = self.runner.run(input_data)
        self.assertEqual(output, expected)

    def test_n2_case_a0(self):
        # N=2，第二個位置 a[2]=0，排列應為 [2,1]
        input_data = "2\n0\n"
        self.assert_solution(input_data, [2, 1])

    def test_n2_case_a1(self):
        # N=2，第二個位置 a[2]=1，排列應為 [1,2]
        input_data = "2\n1\n"
        self.assert_solution(input_data, [1, 2])

    def test_fixed_case_1(self):
        perm = [2, 1, 4, 3]
        input_data = _build_input_from_permutation(perm)
        self.assert_solution(input_data, perm)

    def test_fixed_case_2(self):
        perm = [3, 1, 4, 2, 5]
        input_data = _build_input_from_permutation(perm)
        self.assert_solution(input_data, perm)

    def test_reference_generated_cases(self):
        # 多組小型案例：先由排列產生輸入，再比對輸出是否回復原排列
        cases = [
            [1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1],
            [4, 1, 6, 2, 5, 3],
            [2, 5, 1, 4, 6, 3],
            [3, 6, 2, 1, 5, 4],
        ]
        for perm in cases:
            with self.subTest(perm=perm):
                input_data = _build_input_from_permutation(perm)
                expected = _reference_decode(input_data)
                self.assert_solution(input_data, expected)

    def test_output_token_count(self):
        # 額外檢查：輸出應該恰好有 N 個整數
        perm = [5, 2, 1, 4, 3]
        input_data = _build_input_from_permutation(perm)
        out = self.runner.run(input_data)
        tokens = out.split()
        self.assertEqual(len(tokens), len(perm))
        for t in tokens:
            int(t)


if __name__ == "__main__":
    unittest.main(verbosity=2)
