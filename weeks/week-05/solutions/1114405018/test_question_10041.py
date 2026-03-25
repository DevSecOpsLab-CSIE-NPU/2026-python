import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestUVA10041(unittest.TestCase):
    """UVA 10041 (Vito's Family) 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 允許用環境變數指定被測試檔案；未指定時預設測同資料夾下的 solution.py
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "solution.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 solution.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 若是可匯入的 Python 模組，嘗試動態載入
        try:
            spec = importlib.util.spec_from_file_location("target_solution", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            # 若載入失敗，稍後改走 subprocess 執行腳本模式
            return None

    @staticmethod
    def _brute_force_min_sum(addresses):
        # 參考解：枚舉所有可能住址，計算最小總距離（用於驗證）
        best = None
        for x in addresses:
            total = sum(abs(x - a) for a in addresses)
            if best is None or total < best:
                best = total
        return best if best is not None else 0

    def _run_target_single_case(self, addresses):
        # 優先測函式 API，找不到再改測整支腳本輸入輸出
        m = self.target_module

        if m is not None and hasattr(m, "min_total_distance"):
            result = m.min_total_distance(addresses)
            return int(result)

        if m is not None and hasattr(m, "solve"):
            input_data = f"1\n{len(addresses)} {' '.join(map(str, addresses))}\n"
            output = str(m.solve(input_data)).strip()
            return int(output)

        input_data = f"1\n{len(addresses)} {' '.join(map(str, addresses))}\n"
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        output = completed.stdout.strip().splitlines()
        self.assertTrue(output, "腳本沒有輸出任何內容")
        return int(output[-1].strip())

    def test_basic_case(self):
        # 經典範例：選中位數可得最小總距離
        addresses = [2, 4, 6]
        expected = 4
        got = self._run_target_single_case(addresses)
        self.assertEqual(got, expected)

    def test_with_duplicates(self):
        # 題目允許重複門牌號碼
        addresses = [10, 10, 10, 20, 30]
        expected = self._brute_force_min_sum(addresses)
        got = self._run_target_single_case(addresses)
        self.assertEqual(got, expected)

    def test_even_number_of_relatives(self):
        # 偶數筆資料時，中位區間任一點都能得到最小值
        addresses = [1, 2, 100, 101]
        expected = self._brute_force_min_sum(addresses)
        got = self._run_target_single_case(addresses)
        self.assertEqual(got, expected)

    def test_single_relative(self):
        # 只有一位親戚時，最小總距離應為 0
        addresses = [12345]
        expected = 0
        got = self._run_target_single_case(addresses)
        self.assertEqual(got, expected)

    def test_randomized_against_bruteforce(self):
        # 隨機小測資對拍，避免只通過固定範例
        random.seed(10041)
        for _ in range(60):
            n = random.randint(1, 15)
            addresses = [random.randint(1, 200) for _ in range(n)]
            expected = self._brute_force_min_sum(addresses)
            got = self._run_target_single_case(addresses)
            self.assertEqual(got, expected, msg=f"failed addresses={addresses}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
