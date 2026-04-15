import os
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10190(unittest.TestCase):
    """題目 10190 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10190.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10190.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10190.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 先嘗試直接匯入，方便測試已封裝成函式的版本
        try:
            spec = importlib.util.spec_from_file_location("target_10190", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(n, w, t, v, umbrellas):
        # umbrellas 格式：[(x, l, speed), ...]
        lines = [f"{n} {w} {t} {v}"]
        for x, length, speed in umbrellas:
            lines.append(f"{x} {length} {speed}")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        data = text.strip().split()
        if not data:
            raise AssertionError("輸出為空，預期應輸出一個實數答案")
        return float(data[0])

    def _run_target(self, n, w, t, v, umbrellas):
        input_data = self._build_input(n, w, t, v, umbrellas)
        module = self.target_module

        # 優先測試常見函式名稱；若沒有，就改走標準輸入輸出模式
        if module is not None:
            for fn_name in ("solve", "rainfall", "calculate", "solve_case"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(n, w, t, v, umbrellas)
                    except TypeError:
                        try:
                            result = fn(input_data)
                        except TypeError:
                            result = fn()

                    if isinstance(result, str):
                        return self._parse_output(result)
                    if result is not None:
                        return float(result)

            if hasattr(module, "main"):
                fn = getattr(module, "main")
                try:
                    result = fn()
                except TypeError:
                    result = fn(input_data)

                if isinstance(result, str):
                    return self._parse_output(result)
                if result is not None:
                    return float(result)

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_sample_case(self):
        # 題目範例：確認基本計算與格式處理
        n, w, t, v = 2, 4, 3, 10
        umbrellas = [
            (0, 1, 1),
            (3, 1, -1),
        ]
        expected = 65.00
        got = self._run_target(n, w, t, v, umbrellas)
        self.assertAlmostEqual(got, expected, places=2)

    def test_no_umbrella(self):
        # 沒有任何自動傘時，雨量就是整段道路面積乘上時間與雨強
        n, w, t, v = 0, 10, 4, 2
        umbrellas = []
        expected = 80.00
        got = self._run_target(n, w, t, v, umbrellas)
        self.assertAlmostEqual(got, expected, places=2)

    def test_static_umbrella(self):
        # 靜止不動的傘：覆蓋長度固定，答案很好手算
        n, w, t, v = 1, 5, 2, 3
        umbrellas = [
            (1, 2, 0),
        ]
        # 未被遮住的長度 = 5 - 2 = 3，所以總雨量 = 3 * 2 * 3 = 18
        expected = 18.00
        got = self._run_target(n, w, t, v, umbrellas)
        self.assertAlmostEqual(got, expected, places=2)

    def test_moving_without_bounce(self):
        # 會移動但不碰邊界的案例，確認速度方向有被正確處理
        n, w, t, v = 1, 10, 3, 1
        umbrellas = [
            (0, 2, 2),
        ]
        # 遮住長度固定為 2，所以答案 = (10 - 2) * 3 * 1 = 24
        expected = 24.00
        got = self._run_target(n, w, t, v, umbrellas)
        self.assertAlmostEqual(got, expected, places=2)

    def test_overlap_case(self):
        # 兩把傘彼此靠近並產生重疊，這類情況最容易寫錯
        n, w, t, v = 2, 4, 3, 10
        umbrellas = [
            (0, 1, 1),
            (3, 1, -1),
        ]
        # 這組就是範例，已知答案為 65.00
        expected = 65.00
        got = self._run_target(n, w, t, v, umbrellas)
        self.assertAlmostEqual(got, expected, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)