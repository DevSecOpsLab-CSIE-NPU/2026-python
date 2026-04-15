import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10189(unittest.TestCase):
    """題目 10189（Minesweeper）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10189.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10189.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10189.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 先嘗試直接匯入，方便測試已封裝成函式的版本
        try:
            spec = importlib.util.spec_from_file_location("target_10189", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases 格式：[(n, m, grid), ...]
        lines = []
        for n, m, grid in cases:
            lines.append(f"{n} {m}")
            lines.extend(grid)
        lines.append("0 0")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _reference_output(cases):
        # 參考解：逐格計算八方向地雷數，並依題目格式輸出
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),   (1, 1),
        ]

        blocks = []
        for index, (n, m, grid) in enumerate(cases, start=1):
            lines = [f"Field #{index}:"]
            for row_index in range(n):
                row = []
                for col_index in range(m):
                    if grid[row_index][col_index] == "*":
                        row.append("*")
                        continue

                    mines = 0
                    for dr, dc in directions:
                        nr = row_index + dr
                        nc = col_index + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                            mines += 1
                    row.append(str(mines))
                lines.append("".join(row))
            blocks.append("\n".join(lines))

        return "\n\n".join(blocks) + "\n"

    def _run_target(self, cases):
        input_data = self._build_input(cases)
        module = self.target_module

        # 優先測試常見函式名稱；若沒有，就改走標準輸入輸出模式
        if module is not None:
            for fn_name in ("solve", "minesweeper", "solve_case"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(cases)
                    except TypeError:
                        result = fn(input_data)

                    if isinstance(result, str):
                        return result
                    if result is not None:
                        return str(result)

            if hasattr(module, "main"):
                fn = getattr(module, "main")
                try:
                    result = fn()
                except TypeError:
                    result = fn(input_data)

                if isinstance(result, str):
                    return result
                if result is not None:
                    return str(result)

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample_case(self):
        # 題目範例，確認基本輸出與空行格式正確
        cases = [
            (4, 4, [
                "*...",
                "....",
                ".*..",
                "....",
            ]),
            (3, 5, [
                "**...",
                ".....",
                ".*...",
            ]),
        ]
        expected = self._reference_output(cases)
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_single_cell_mine(self):
        # 最小尺寸且只有地雷，確認不會把 * 轉成數字
        cases = [
            (1, 1, [
                "*",
            ]),
        ]
        expected = self._reference_output(cases)
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_single_cell_empty(self):
        # 最小尺寸且沒有地雷，答案應為 0
        cases = [
            (1, 1, [
                ".",
            ]),
        ]
        expected = self._reference_output(cases)
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_edge_and_corner_counts(self):
        # 驗證角落、邊界與中心的八方向計數
        cases = [
            (3, 3, [
                "*.*",
                ".*.",
                "*.*",
            ]),
        ]
        expected = self._reference_output(cases)
        got = self._run_target(cases)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 小型隨機對拍：用參考解比對多組地圖，抓出邊界處理錯誤
        random.seed(10189)
        for _ in range(80):
            case_count = random.randint(1, 3)
            cases = []
            for _case in range(case_count):
                n = random.randint(1, 5)
                m = random.randint(1, 5)
                grid = []
                for _row in range(n):
                    row = "".join("*" if random.random() < 0.28 else "." for _col in range(m))
                    grid.append(row)
                cases.append((n, m, grid))

            expected = self._reference_output(cases)
            got = self._run_target(cases)
            self.assertEqual(got, expected, msg=f"failed cases={cases}")


if __name__ == "__main__":
    unittest.main(verbosity=2)