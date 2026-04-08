import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10062(unittest.TestCase):
    """題目 10062（Tell me the frequencies!）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10062.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10062.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10062.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 盡量用 import 測函式；若失敗則退回 subprocess 測腳本輸入輸出
        try:
            spec = importlib.util.spec_from_file_location("target_10062", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _reference_solve(counts):
        # 參考解：由後往前插入。
        # counts[i] 代表第 i+2 個位置（1-based: 位置 i+2）前面比它小的數量。
        n = len(counts) + 1
        ans = [1]
        for value in range(2, n + 1):
            c = counts[value - 2]
            # 長度為 value-1，合法 c 範圍為 [0, value-1]
            idx = value - 1 - c
            ans.insert(idx, value)
        return ans

    @staticmethod
    def _build_input(counts):
        n = len(counts) + 1
        lines = [str(n)]
        lines.extend(str(x) for x in counts)
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text, n):
        # 允許空白分隔（換行或空格皆可）
        nums = [int(x) for x in text.split()]
        if len(nums) != n:
            raise AssertionError(f"輸出數量錯誤，預期 {n} 個，實際 {len(nums)} 個")
        return nums

    def _run_target(self, counts):
        n = len(counts) + 1
        input_data = self._build_input(counts)
        m = self.target_module

        # 優先找常見函式名稱
        if m is not None:
            for fn_name in ("reconstruct", "solve", "solve_case"):
                if hasattr(m, fn_name):
                    fn = getattr(m, fn_name)
                    try:
                        result = fn(counts)
                        if isinstance(result, str):
                            return self._parse_output(result, n)
                        return [int(x) for x in result]
                    except TypeError:
                        # solve(input_text) 型別
                        result = fn(input_data)
                        if isinstance(result, str):
                            return self._parse_output(result, n)
                        return [int(x) for x in result]

        # 腳本模式：直接餵 stdin，讀 stdout
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout.strip(), n)

    @staticmethod
    def _counts_from_permutation(perm):
        # 由排列反推 counts，作為隨機測資生成器
        counts = []
        for i in range(1, len(perm)):
            x = perm[i]
            c = sum(1 for j in range(i) if perm[j] < x)
            counts.append(c)
        return counts

    def test_minimum_n2(self):
        # N=2 的最小案例
        counts = [0]
        expected = [1, 2]
        got = self._run_target(counts)
        self.assertEqual(got, expected)

    def test_ordered_case(self):
        # counts = [1,2,3,4] 依參考解重建結果
        counts = [1, 2, 3, 4]
        expected = [5, 4, 3, 2, 1]
        got = self._run_target(counts)
        self.assertEqual(got, expected)

    def test_reverse_case(self):
        # counts 全為 0 時，依參考解重建為遞增
        counts = [0, 0, 0, 0]
        expected = [1, 2, 3, 4, 5]
        got = self._run_target(counts)
        self.assertEqual(got, expected)

    def test_handcrafted_case(self):
        # 手作中型案例，避免只通過極端值
        counts = [0, 1, 1, 3, 2]
        expected = self._reference_solve(counts)
        got = self._run_target(counts)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：先隨機排列，再反推 counts，最後比對重建結果
        random.seed(10062)
        for _ in range(80):
            n = random.randint(2, 120)
            perm = list(range(1, n + 1))
            random.shuffle(perm)
            counts = self._counts_from_permutation(perm)

            expected = self._reference_solve(counts)
            got = self._run_target(counts)

            self.assertEqual(got, expected, msg=f"failed n={n}, counts_head={counts[:8]}")
            # 額外驗證輸出確實是 1..n 的排列
            self.assertEqual(sorted(got), list(range(1, n + 1)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
