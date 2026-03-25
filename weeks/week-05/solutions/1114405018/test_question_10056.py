import math
import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestUVA10056(unittest.TestCase):
    """UVA 10056 (What is the Probability ?) 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測同資料夾下的 10056.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10056.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10056.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 若可匯入就優先測函式；失敗再退回腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10056", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _reference_probability(n: int, p: float, i: int) -> float:
        # 參考公式：P(i wins) = p*(1-p)^(i-1) / (1-(1-p)^n)
        # p=0 時永遠不會有人成功，因此機率為 0
        if p == 0.0:
            return 0.0

        q = 1.0 - p
        numerator = p * (q ** (i - 1))
        denominator = 1.0 - (q ** n)
        return numerator / denominator

    @staticmethod
    def _format_input_case(n: int, p: float, i: int) -> str:
        return f"1\n{n} {p} {i}\n"

    def _run_target_single_case(self, n: int, p: float, i: int) -> float:
        # 優先找函式介面，否則用 stdin/stdout 執行整支程式
        m = self.target_module

        if m is not None and hasattr(m, "win_probability"):
            return float(m.win_probability(n, p, i))

        if m is not None and hasattr(m, "solve"):
            output = str(m.solve(self._format_input_case(n, p, i))).strip()
            if not output:
                self.fail("solve 回傳空字串")
            return float(output.splitlines()[0].strip())

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=self._format_input_case(n, p, i),
            text=True,
            capture_output=True,
            check=True,
        )
        out = completed.stdout.strip()
        self.assertTrue(out, "腳本沒有輸出任何內容")
        return float(out.splitlines()[0].strip())

    def assertOutput4dpEqual(self, got: float, expected: float):
        # 題目要求小數點後四位，測試以四位小數結果比對
        expected_4dp = float(f"{expected:.4f}")
        self.assertAlmostEqual(got, expected_4dp, places=4)

    def test_p_zero_should_be_zero(self):
        # 成功機率為 0 時，不論第幾位玩家機率都為 0
        n, p, i = 10, 0.0, 3
        expected = 0.0
        got = self._run_target_single_case(n, p, i)
        self.assertOutput4dpEqual(got, expected)

    def test_p_one_only_first_player_can_win(self):
        # 成功機率為 1 時，只有第一位玩家會贏
        n, p = 7, 1.0

        got_first = self._run_target_single_case(n, p, 1)
        got_other = self._run_target_single_case(n, p, 4)

        self.assertOutput4dpEqual(got_first, 1.0)
        self.assertOutput4dpEqual(got_other, 0.0)

    def test_known_case(self):
        # 一般案例：用參考公式計算後比對
        n, p, i = 3, 0.5, 2
        expected = self._reference_probability(n, p, i)
        got = self._run_target_single_case(n, p, i)
        self.assertOutput4dpEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：檢查多組輸入都與參考公式一致（四位小數）
        random.seed(10056)
        for _ in range(80):
            n = random.randint(1, 80)
            i = random.randint(1, n)

            # 取四位小數機率，降低二進位浮點輸入誤差
            p = random.randint(0, 10000) / 10000.0

            expected = self._reference_probability(n, p, i)
            got = self._run_target_single_case(n, p, i)
            self.assertOutput4dpEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
