import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util
import math


class TestQuestion10170(unittest.TestCase):
    """題目 10170（The Hotel with Infinite Rooms）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10170.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10170.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10170.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先嘗試 import；若失敗則退回 subprocess 腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10170", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # 題目是多筆輸入直到 EOF，每行一組 S D
        lines = [f"{s} {d}" for s, d in cases]
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        # 輸出每行一個答案，這裡容許空白分隔
        parts = text.strip().split()
        if not parts:
            return []
        return [int(x) for x in parts]

    @staticmethod
    def _reference_answer(s, d):
        """參考解（數學版）。

        設 total(n) = 1+2+...+n。
        從 S 人團開始，住到 n 人團為止的總天數：
            total(n) - total(S-1)
        需找到最小 n 使上述值 >= D。
        """
        need = d + s * (s - 1) // 2

        # 求最小 n 使 n(n+1)/2 >= need
        # 先用 isqrt 給一個下界，再往上微調
        n = (math.isqrt(1 + 8 * need) - 1) // 2
        while n * (n + 1) // 2 < need:
            n += 1
        return n

    def _run_target(self, cases):
        input_data = self._build_input(cases)
        m = self.target_module

        if m is not None:
            # 常見函式名稱嘗試順序
            for fn_name in ("solve", "solve_case", "hotel_group", "answer"):
                if hasattr(m, fn_name):
                    fn = getattr(m, fn_name)

                    # 1) 嘗試 solve(text) 形式
                    try:
                        result = fn(input_data)
                        if isinstance(result, str):
                            return self._parse_output(result)
                        if isinstance(result, list):
                            return [int(x) for x in result]
                    except TypeError:
                        pass

                    # 2) 嘗試 solve(s, d) 單筆形式，逐筆呼叫
                    try:
                        out = [int(fn(s, d)) for s, d in cases]
                        return out
                    except TypeError:
                        pass

                    # 3) 嘗試 solve((s,d)) 或 solve([s,d]) 形式
                    try:
                        out = []
                        for s, d in cases:
                            v = fn((s, d))
                            out.append(int(v))
                        return out
                    except Exception:
                        pass

        # 腳本模式：直接餵 stdin
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_sample_like_case(self):
        # 常見敘述案例：S=4，D=10 時應落在 6 人團
        cases = [(4, 10)]
        expected = [6]
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_single_day(self):
        # 第一天一定是起始團 S 人
        cases = [(1, 1), (7, 1), (10000, 1)]
        expected = [1, 7, 10000]
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_multiple_lines(self):
        # 多筆輸入（直到 EOF）應逐行對應輸出
        cases = [(3, 1), (3, 3), (3, 4), (3, 7)]
        expected = [3, 3, 4, 4]
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_large_values(self):
        # 大數值測試，確保不會因為整數溢位或效率問題失敗
        cases = [
            (1, 10**12),
            (9999, 10**14),
            (10000, 10**14 - 7),
        ]
        expected = [self._reference_answer(s, d) for s, d in cases]
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：與數學參考解比對
        random.seed(10170)
        cases = []
        for _ in range(120):
            s = random.randint(1, 10000)
            d = random.randint(1, 10**12)
            cases.append((s, d))

        expected = [self._reference_answer(s, d) for s, d in cases]
        got = self._run_target(cases)
        self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
