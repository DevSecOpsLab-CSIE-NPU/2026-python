import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10268(unittest.TestCase):
    """題目 10268（水球試樓層）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10268.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10268.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10268.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先嘗試匯入，方便測函式；失敗時退回 subprocess
        try:
            spec = importlib.util.spec_from_file_location("target_10268", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases 格式：[(k, n), ...]
        lines = [f"{k} {n}" for k, n in cases]
        lines.append("0 0")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        # 只接受兩種輸出：整數 trial 數，或題目指定的英文句子
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return lines

    @staticmethod
    def _reference_case(k, n):
        # 標準 DP：dp[e] 表示目前試驗次數下，e 顆蛋最多能測出幾層
        if n <= 1:
            return "1"

        dp = [0] * (k + 1)
        for t in range(1, 64):
            for e in range(k, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
            if dp[k] >= n:
                return str(t)
        return "More than 63 trials needed."

    @classmethod
    def _reference_solve_from_text(cls, input_data):
        cases = []
        for line in input_data.splitlines():
            line = line.strip()
            if not line:
                continue
            k, n = map(int, line.split())
            if k == 0:
                break
            cases.append((k, n))

        return [cls._reference_case(k, n) for k, n in cases]

    def _run_target(self, input_data):
        module = self.target_module

        # 優先測試常見函式名稱
        if module is not None:
            for fn_name in ("solve", "solve_text", "run", "main_solve"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(input_data)
                    except TypeError:
                        result = None

                    if isinstance(result, str):
                        return result

        # 腳本模式
        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample_like_cases(self):
        # 幾個直觀案例：一顆蛋就是線性測試
        cases = [(1, 1), (1, 10), (2, 100)]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, expected)

    def test_exact_thresholds(self):
        # 已知門檻：2 顆蛋在 14 次可測到 105 層，13 次只能到 91 層
        cases = [(2, 105), (2, 106), (3, 63)]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, expected)

    def test_more_than_63_message(self):
        # 超過 63 次就要輸出題目指定訊息
        cases = [(1, 9223372036854775807), (2, 9223372036854775807)]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 小範圍隨機對拍：k 與 n 都不大時，用參考 DP 精確比對
        random.seed(10268)

        cases = []
        for _ in range(60):
            k = random.randint(1, 10)
            n = random.randint(1, 500)
            cases.append((k, n))

        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
