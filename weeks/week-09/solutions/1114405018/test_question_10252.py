import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10252(unittest.TestCase):
    """題目 10252（王老師愛兩條線）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10252.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10252.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10252.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先嘗試匯入，方便直接測函式；失敗再退回 subprocess
        try:
            spec = importlib.util.spec_from_file_location("target_10252", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases 格式：[(points), ...]，points 為 [(x, y), ...]
        lines = [str(len(cases))]
        for points in cases:
            lines.append(str(len(points)))
            for x, y in points:
                lines.append(f"{x} {y}")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        # 每組輸出兩個整數：最小距離和 + 最多解的個數
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        result = []
        for line in lines:
            parts = line.split()
            if len(parts) != 2:
                raise AssertionError(f"輸出格式錯誤：{line!r}")
            result.append((int(parts[0]), int(parts[1])))
        return result

    @staticmethod
    def _reference_case(points):
        # L1 距離可分成 x、y 各自找中位數
        xs = sorted(x for x, _ in points)
        ys = sorted(y for _, y in points)
        n = len(points)

        if n % 2 == 1:
            mx = xs[n // 2]
            my = ys[n // 2]
            count = 1
        else:
            lx, rx = xs[n // 2 - 1], xs[n // 2]
            ly, ry = ys[n // 2 - 1], ys[n // 2]
            mx = lx
            my = ly
            count = (rx - lx + 1) * (ry - ly + 1)

        best = sum(abs(x - mx) + abs(y - my) for x, y in points)
        return best, count

    @classmethod
    def _reference_solve_from_text(cls, input_data):
        tokens = input_data.split()
        if not tokens:
            return ""

        it = iter(tokens)
        t = int(next(it))
        out = []

        for _ in range(t):
            n = int(next(it))
            points = [(int(next(it)), int(next(it))) for _ in range(n)]
            best, count = cls._reference_case(points)
            out.append(f"{best} {count}")

        return "\n".join(out) + "\n"

    @staticmethod
    def _bruteforce_case(points):
        # 小範圍暴力對拍：只掃描座標範圍內的整數點
        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)

        best = None
        count = 0
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                total = sum(abs(x - px) + abs(y - py) for px, py in points)
                if best is None or total < best:
                    best = total
                    count = 1
                elif total == best:
                    count += 1
        return best, count

    def _run_target(self, input_data):
        module = self.target_module

        # 優先嘗試常見函式介面
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

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample_case(self):
        # 題目範例：三個點都在對角線上，答案應是 4 1
        cases = [[(0, 0), (1, 1), (2, 2)]]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._parse_output(got), self._parse_output(expected))

    def test_even_count_multiple_solutions(self):
        # 兩個點在水平線上，任何介於中位數區間的整數點都可達到最小值
        cases = [[(0, 0), (2, 0)]]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._parse_output(got), self._parse_output(expected))

    def test_square_case(self):
        # 四個角點，x 與 y 的中位數區間都很大，測試計數是否正確
        cases = [[(0, 0), (0, 2), (2, 0), (2, 2)]]
        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._parse_output(got), self._parse_output(expected))

    def test_randomized_small_against_bruteforce(self):
        # 小範圍隨機對拍：暴力枚舉 bounding box 內所有整數點
        random.seed(10252)

        cases = []
        for _ in range(40):
            n = random.randint(1, 7)
            points = []
            for _ in range(n):
                x = random.randint(-4, 4)
                y = random.randint(-4, 4)
                points.append((x, y))
            cases.append(points)

        input_data = self._build_input(cases)
        got = self._parse_output(self._run_target(input_data))

        expected = [self._bruteforce_case(points) for points in cases]
        self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
