import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10193(unittest.TestCase):
    """題目 10193（反正切拆分）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10193.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10193.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10193.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 先嘗試直接匯入，若被測程式有封裝成函式就可直接測
        try:
            spec = importlib.util.spec_from_file_location("target_10193", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _parse_output(text):
        data = text.strip().split()
        if not data:
            raise AssertionError("輸出為空，預期應輸出一個整數答案")
        return int(data[0])

    @staticmethod
    def _expected(a):
        # 由 (b-a)(c-a)=a^2+1 直接找最小 b+c
        target = a * a + 1
        best = None
        limit = int(target ** 0.5)

        for d in range(1, limit + 1):
            if target % d != 0:
                continue
            e = target // d
            b = a + d
            c = a + e
            total = b + c
            if best is None or total < best:
                best = total

        return best

    def _run_target(self, a):
        input_data = f"{a}\n"
        module = self.target_module

        # 優先測試常見函式名稱；若沒有，就改走標準輸入輸出模式
        if module is not None:
            for fn_name in ("solve", "answer", "calc", "solve_case"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(a)
                    except TypeError:
                        result = fn(input_data)

                    if isinstance(result, str):
                        return self._parse_output(result)
                    if result is not None:
                        return int(result)

            if hasattr(module, "main"):
                fn = getattr(module, "main")
                try:
                    result = fn()
                except TypeError:
                    result = fn(input_data)

                if isinstance(result, str):
                    return self._parse_output(result)
                if result is not None:
                    return int(result)

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_small_basic_cases(self):
        # 幾個最小且好手算的案例，方便檢查公式與輸出格式
        cases = {
            1: 5,   # (b-a)(c-a)=2 => (1,2) => 2+3=5
            2: 10,  # (b-a)(c-a)=5 => (1,5) => 3+7=10
            3: 13,  # (b-a)(c-a)=10 => (2,5) => 5+8=13
            4: 26,  # (b-a)(c-a)=17 => (1,17) => 5+21=26
        }

        for a, expected in cases.items():
            got = self._run_target(a)
            self.assertEqual(got, expected, msg=f"failed a={a}")

    def test_reference_factorization(self):
        # 直接用參考解驗證一批固定數字，確認被測程式沒有漏掉較小的因數組
        for a in (5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 25, 30):
            expected = self._expected(a)
            got = self._run_target(a)
            self.assertEqual(got, expected, msg=f"failed a={a}")

    def test_randomized_against_reference(self):
        # 小範圍隨機對拍：用參考解直接比對，抓出因數搜尋或最小值判斷錯誤
        random.seed(10193)
        for _ in range(100):
            a = random.randint(1, 60)
            expected = self._expected(a)
            got = self._run_target(a)
            self.assertEqual(got, expected, msg=f"failed a={a}")

    def test_upper_bound_case(self):
        # 題目上限測一下，確認大一點的數字也能處理
        a = 60000
        expected = self._expected(a)
        got = self._run_target(a)
        self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)