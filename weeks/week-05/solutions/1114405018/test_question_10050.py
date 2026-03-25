import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestUVA10050(unittest.TestCase):
    """UVA 10050 (Hartals) 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設尋找 10050.py，與目前資料夾命名一致
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10050.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10050.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 若可作為模組匯入，優先用函式測試
        try:
            spec = importlib.util.spec_from_file_location("target_solution_10050", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            # 匯入失敗時，後續退回腳本執行模式
            return None

    @staticmethod
    def _is_weekend(day: int) -> bool:
        # 題目設定第 1 天是星期天，星期五(6)與星期六(0)是假日
        weekday = day % 7
        return weekday == 6 or weekday == 0

    def _reference_lost_days(self, n: int, hartals):
        # 參考解：逐日模擬並排除假日
        lost = set()
        for h in hartals:
            day = h
            while day <= n:
                if not self._is_weekend(day):
                    lost.add(day)
                day += h
        return len(lost)

    def _run_target_single_case(self, n: int, hartals):
        # 優先找函式 API，找不到就以 stdin/stdout 執行整支程式
        m = self.target_module

        if m is not None and hasattr(m, "count_lost_days"):
            return int(m.count_lost_days(n, hartals))

        if m is not None and hasattr(m, "simulate_hartals"):
            return int(m.simulate_hartals(n, hartals))

        if m is not None and hasattr(m, "solve"):
            lines = ["1", str(n), str(len(hartals))] + [str(x) for x in hartals]
            input_data = "\n".join(lines) + "\n"
            output = str(m.solve(input_data)).strip()
            return int(output)

        lines = ["1", str(n), str(len(hartals))] + [str(x) for x in hartals]
        input_data = "\n".join(lines) + "\n"
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        output_lines = completed.stdout.strip().splitlines()
        self.assertTrue(output_lines, "腳本沒有輸出任何內容")
        return int(output_lines[-1].strip())

    def test_sample_case_1(self):
        # UVA 經典範例一
        n = 14
        hartals = [3, 4, 8]
        expected = 5
        got = self._run_target_single_case(n, hartals)
        self.assertEqual(got, expected)

    def test_sample_case_2(self):
        # UVA 經典範例二
        n = 100
        hartals = [12, 15, 25, 40]
        expected = 15
        got = self._run_target_single_case(n, hartals)
        self.assertEqual(got, expected)

    def test_no_overlap_simple(self):
        # 多個政黨互不重疊時，應正確累加工作天損失
        n = 20
        hartals = [3, 5]
        expected = self._reference_lost_days(n, hartals)
        got = self._run_target_single_case(n, hartals)
        self.assertEqual(got, expected)

    def test_with_heavy_overlap(self):
        # 大量重疊罷會日，不能重複計數
        n = 70
        hartals = [2, 4, 8, 16]
        expected = self._reference_lost_days(n, hartals)
        got = self._run_target_single_case(n, hartals)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：以參考模擬器驗證結果正確性
        random.seed(10050)
        for _ in range(60):
            n = random.randint(7, 300)
            p = random.randint(1, 12)
            hartals = [random.randint(1, 60) for _ in range(p)]
            expected = self._reference_lost_days(n, hartals)
            got = self._run_target_single_case(n, hartals)
            self.assertEqual(got, expected, msg=f"failed n={n}, hartals={hartals}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
