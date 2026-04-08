import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10093(unittest.TestCase):
    """題目 10093（炮兵部署）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10093.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10093.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10093.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先用 import 測函式，失敗時退回 subprocess 腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10093", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(grid):
        n = len(grid)
        m = len(grid[0]) if n else 0
        lines = [f"{n} {m}"]
        lines.extend(grid)
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        data = text.strip().split()
        if not data:
            raise AssertionError("輸出為空，預期應輸出一個整數")
        return int(data[0])

    @staticmethod
    def _valid_row_states(m):
        # 單列合法：同列內任兩炮兵距離不得為 1 或 2
        states = []
        for s in range(1 << m):
            if (s & (s << 1)) != 0:
                continue
            if (s & (s << 2)) != 0:
                continue
            states.append(s)
        return states

    @staticmethod
    def _reference_solve(grid):
        # 小資料精確解：列舉每列狀態 + 記憶化 DFS
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        blocked = []
        for r in grid:
            mask = 0
            for j, ch in enumerate(r):
                if ch == "H":
                    mask |= 1 << j
            blocked.append(mask)

        states = TestQuestion10093._valid_row_states(m)
        counts = [s.bit_count() for s in states]

        row_cands = []
        for i in range(n):
            cands = []
            for idx, s in enumerate(states):
                if (s & blocked[i]) == 0:
                    cands.append(idx)
            row_cands.append(cands)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, prev1, prev2):
            if i == n:
                return 0

            best = 0
            s_prev1 = states[prev1]
            s_prev2 = states[prev2]

            for cur in row_cands[i]:
                s_cur = states[cur]

                # 與上一列、上上列不得同欄（垂直距離 1 與 2）
                if (s_cur & s_prev1) != 0:
                    continue
                if (s_cur & s_prev2) != 0:
                    continue

                best = max(best, counts[cur] + dfs(i + 1, cur, prev1))
            return best

        zero_idx = states.index(0)
        return dfs(0, zero_idx, zero_idx)

    def _run_target(self, grid):
        input_data = self._build_input(grid)
        m = self.target_module

        if m is not None:
            for fn_name in ("max_artillery", "solve", "solve_case"):
                if hasattr(m, fn_name):
                    fn = getattr(m, fn_name)
                    try:
                        if fn_name == "max_artillery":
                            return int(fn(grid))
                        result = fn(input_data)
                    except TypeError:
                        result = fn(grid)

                    if isinstance(result, str):
                        return self._parse_output(result)
                    return int(result)

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_all_mountain(self):
        # 全部山地，無法部署
        grid = [
            "HHH",
            "HHH",
            "HHH",
        ]
        expected = 0
        got = self._run_target(grid)
        self.assertEqual(got, expected)

    def test_single_plain(self):
        # 1x1 平原，最多放 1
        grid = ["P"]
        expected = 1
        got = self._run_target(grid)
        self.assertEqual(got, expected)

    def test_one_row_spacing(self):
        # 同列間距需 >= 3，長度 4 可放在第 1 與第 4 格
        grid = ["PPPP"]
        expected = 2
        got = self._run_target(grid)
        self.assertEqual(got, expected)

    def test_small_mixed_case(self):
        grid = [
            "PPP",
            "PHP",
            "PPP",
        ]
        expected = self._reference_solve(grid)
        got = self._run_target(grid)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：以小尺寸地圖和精確解比對
        random.seed(10093)
        for _ in range(80):
            n = random.randint(1, 6)
            m = random.randint(1, 6)

            grid = []
            for _r in range(n):
                row = "".join("H" if random.random() < 0.35 else "P" for _c in range(m))
                grid.append(row)

            expected = self._reference_solve(grid)
            got = self._run_target(grid)
            self.assertEqual(got, expected, msg=f"failed grid={grid}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
