import os
import random
import subprocess
import sys
import unittest
from itertools import product
from pathlib import Path
import importlib.util


class TestQuestion10071(unittest.TestCase):
    """題目 10071 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10071.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10071.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10071.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先用 import 測函式，失敗時退回 subprocess 測標準輸入輸出
        try:
            spec = importlib.util.spec_from_file_location("target_10071", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(nums):
        lines = [str(len(nums))]
        lines.extend(str(x) for x in nums)
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        data = text.strip().split()
        if not data:
            raise AssertionError("輸出為空，預期應輸出一個整數答案")
        return int(data[0])

    @staticmethod
    def _reference_count(nums):
        # 參考解（小資料精確）：枚舉 (a,b,c,d,e)，若總和在 S 中即對應唯一 f。
        values = list(nums)
        sset = set(values)
        total = 0
        for a, b, c, d, e in product(values, repeat=5):
            if (a + b + c + d + e) in sset:
                total += 1
        return total

    def _run_target(self, nums):
        input_data = self._build_input(nums)
        m = self.target_module

        # 優先找常見函式名稱
        if m is not None:
            for fn_name in ("count_tuples", "count_sextuples", "solve", "solve_case"):
                if hasattr(m, fn_name):
                    fn = getattr(m, fn_name)
                    try:
                        result = fn(nums)
                    except TypeError:
                        result = fn(input_data)

                    if isinstance(result, str):
                        return self._parse_output(result)
                    return int(result)

        # 腳本模式
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_single_zero(self):
        # S={0} 時僅有 (0,0,0,0,0,0) 一組
        nums = [0]
        expected = 1
        got = self._run_target(nums)
        self.assertEqual(got, expected)

    def test_single_nonzero(self):
        # S={5} 時 5+5+5+5+5=25，不可能等於 f=5
        nums = [5]
        expected = 0
        got = self._run_target(nums)
        self.assertEqual(got, expected)

    def test_two_values_0_1(self):
        # S={0,1}：5 個變數和為 0 或 1 時可成立
        nums = [0, 1]
        expected = 6
        got = self._run_target(nums)
        self.assertEqual(got, expected)

    def test_negative_positive_mix(self):
        # 含負數、零、正數的混合案例
        nums = [-1, 0, 1]
        expected = self._reference_count(nums)
        got = self._run_target(nums)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：小 N 精確比對參考解
        random.seed(10071)
        universe = list(range(-6, 7))

        for _ in range(80):
            n = random.randint(1, 7)
            nums = random.sample(universe, n)

            expected = self._reference_count(nums)
            got = self._run_target(nums)

            self.assertEqual(got, expected, msg=f"failed nums={nums}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
