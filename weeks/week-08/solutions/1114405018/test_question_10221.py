import math
import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10221(unittest.TestCase):
    """題目 10221（Satellites）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10221.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10221.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10221.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 先嘗試直接匯入，若被測程式有封裝成函式就可直接測
        try:
            spec = importlib.util.spec_from_file_location("target_10221", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases 格式：[(s, a, unit), ...]，unit 為 deg 或 min
        lines = []
        for s, angle, unit in cases:
            lines.append(f"{s} {angle} {unit}")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _reference_case(s, angle, unit):
        # 地球半徑固定 6440 公里，先算軌道半徑 r，再求弧長與弦長
        radius = 6440 + s
        if unit == "deg":
            theta = math.radians(angle)
        else:
            theta = math.radians(angle / 60.0)

        arc = radius * theta
        chord = 2 * radius * math.sin(theta / 2.0)
        return arc, chord

    @staticmethod
    def _parse_output(text):
        # 每行兩個浮點數：弧長與弦長
        lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
        if not lines:
            raise AssertionError("輸出為空，預期應輸出至少一行答案")

        result = []
        for line in lines:
            parts = line.split()
            if len(parts) != 2:
                raise AssertionError(f"輸出格式錯誤：{line}")
            result.append((float(parts[0]), float(parts[1])))
        return result

    def _run_target(self, cases):
        input_data = self._build_input(cases)
        module = self.target_module

        # 優先測試常見函式名稱；若沒有，就改走標準輸入輸出模式
        if module is not None:
            for fn_name in ("solve", "satellites", "solve_case"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(cases)
                    except TypeError:
                        result = fn(input_data)

                    if isinstance(result, str):
                        return self._parse_output(result)
                    if result is not None:
                        return result

            if hasattr(module, "main"):
                fn = getattr(module, "main")
                try:
                    result = fn()
                except TypeError:
                    result = fn(input_data)

                if isinstance(result, str):
                    return self._parse_output(result)
                if result is not None:
                    return result

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def assertAnswersAlmostEqual(self, got, expected):
        # 逐行比對兩個浮點數，容許小數誤差到小數點後 6 位
        self.assertEqual(len(got), len(expected))
        for (g_arc, g_chord), (e_arc, e_chord) in zip(got, expected):
            self.assertAlmostEqual(g_arc, e_arc, places=6)
            self.assertAlmostEqual(g_chord, e_chord, places=6)

    def test_sample_case(self):
        # 題目範例，確認 deg / min 兩種單位都能處理
        cases = [
            (500, 30, "deg"),
            (700, 60, "min"),
            (200, 45, "deg"),
        ]
        expected = [self._reference_case(*case) for case in cases]
        got = self._run_target(cases)
        self.assertAnswersAlmostEqual(got, expected)

    def test_zero_angle(self):
        # 角度為 0 時，弧長與弦長都應為 0
        cases = [
            (0, 0, "deg"),
        ]
        expected = [self._reference_case(*case) for case in cases]
        got = self._run_target(cases)
        self.assertAnswersAlmostEqual(got, expected)

    def test_degree_and_minute_mix(self):
        # 混合 deg 與 min，檢查單位轉換有沒有寫錯
        cases = [
            (100, 90, "deg"),
            (250, 120, "min"),
            (600, 1, "deg"),
        ]
        expected = [self._reference_case(*case) for case in cases]
        got = self._run_target(cases)
        self.assertAnswersAlmostEqual(got, expected)

    def test_randomized_against_reference(self):
        # 小範圍隨機對拍：用參考公式直接比對，抓出角度轉換或三角函數錯誤
        random.seed(10221)
        units = ["deg", "min"]

        for _ in range(80):
            case_count = random.randint(1, 5)
            cases = []
            for _case in range(case_count):
                s = random.randint(0, 2000)
                angle = random.randint(0, 360)
                unit = random.choice(units)
                cases.append((s, angle, unit))

            expected = [self._reference_case(*case) for case in cases]
            got = self._run_target(cases)
            self.assertAnswersAlmostEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)