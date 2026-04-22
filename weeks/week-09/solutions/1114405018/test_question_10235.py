import os
import random
import re
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


MOD = 1_000_000_007


class TestQuestion10235(unittest.TestCase):
    """題目 10235（蛇環覆蓋計數）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10235.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10235.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10235.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先用 import 測函式，失敗時退回 subprocess 測標準輸入輸出
        try:
            spec = importlib.util.spec_from_file_location("target_10235", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases: [(n, m, grid), ...], grid 內為 0/1 整數矩陣
        lines = [str(len(cases))]
        for n, m, grid in cases:
            lines.append(f"{n} {m}")
            for row in grid:
                lines.append("".join(str(x) for x in row))
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        # 嚴格解析格式：Case i: ans
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        ans = []
        for i, line in enumerate(lines, start=1):
            m = re.fullmatch(r"Case\s+(\d+)\s*:\s*(-?\d+)", line)
            if m is None:
                raise AssertionError(f"輸出格式錯誤：{line!r}")
            case_idx = int(m.group(1))
            if case_idx != i:
                raise AssertionError(f"Case 編號不連續：預期 {i}，得到 {case_idx}")
            ans.append(int(m.group(2)))
        return ans

    @staticmethod
    def _edges_of_free_cells(n, m, grid):
        # 將可用格（值為 1）建成無向圖，回傳頂點與邊
        verts = []
        vid = {}
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    vid[(r, c)] = len(verts)
                    verts.append((r, c))

        edges = []
        for r, c in verts:
            u = vid[(r, c)]
            if r + 1 < n and grid[r + 1][c] == 1:
                v = vid[(r + 1, c)]
                edges.append((u, v))
            if c + 1 < m and grid[r][c + 1] == 1:
                v = vid[(r, c + 1)]
                edges.append((u, v))

        return len(verts), edges

    @classmethod
    def _reference_count_case(cls, n, m, grid):
        # 參考解：統計「每個可用格度數恰為 2」的邊集合數（即若干不相交環覆蓋全部可用格）
        v_cnt, edges = cls._edges_of_free_cells(n, m, grid)

        if v_cnt == 0:
            return 1

        # 任一頂點在完整解中度數必須為 2，若原圖鄰接度不足可直接判 0
        deg_cap = [0] * v_cnt
        for u, v in edges:
            deg_cap[u] += 1
            deg_cap[v] += 1
        if any(d < 2 for d in deg_cap):
            return 0

        e_cnt = len(edges)
        incident = [[] for _ in range(v_cnt)]
        for i, (u, v) in enumerate(edges):
            incident[u].append(i)
            incident[v].append(i)

        # rem[v][i] = 從第 i 條邊到最後，仍可影響 v 的邊數，用於剪枝
        rem = [[0] * (e_cnt + 1) for _ in range(v_cnt)]
        for i in range(e_cnt - 1, -1, -1):
            u, v = edges[i]
            for x in range(v_cnt):
                rem[x][i] = rem[x][i + 1]
            rem[u][i] += 1
            rem[v][i] += 1

        deg = [0] * v_cnt
        answer = 0

        def dfs(i):
            nonlocal answer

            # 剪枝：度數不可 >2，也不可在剩餘邊不足時達到 2
            for x in range(v_cnt):
                if deg[x] > 2:
                    return
                if deg[x] + rem[x][i] < 2:
                    return

            if i == e_cnt:
                if all(d == 2 for d in deg):
                    answer = (answer + 1) % MOD
                return

            u, v = edges[i]

            # 分支 1：不選這條邊
            dfs(i + 1)

            # 分支 2：選這條邊
            deg[u] += 1
            deg[v] += 1
            dfs(i + 1)
            deg[u] -= 1
            deg[v] -= 1

        dfs(0)
        return answer

    @classmethod
    def _reference_solve_from_text(cls, input_data):
        lines = [line.strip() for line in input_data.splitlines() if line.strip()]
        t = int(lines[0])
        idx = 1
        out = []

        for case_idx in range(1, t + 1):
            n, m = map(int, lines[idx].split())
            idx += 1

            grid = []
            for _ in range(n):
                row_str = lines[idx]
                idx += 1

                # 兼容「0101」與「0 1 0 1」兩種形式
                if " " in row_str:
                    row = [int(x) for x in row_str.split()]
                else:
                    row = [int(ch) for ch in row_str]
                grid.append(row)

            ans = cls._reference_count_case(n, m, grid)
            out.append(f"Case {case_idx}: {ans}")

        return "\n".join(out) + "\n"

    def _run_target(self, input_data):
        m = self.target_module

        # 優先尋找常見函式介面
        if m is not None:
            for fn_name in ("solve", "solve_text", "run", "main_solve"):
                if hasattr(m, fn_name):
                    fn = getattr(m, fn_name)
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

    def test_basic_cases(self):
        # 基礎案例：空可用格、單格、2x2 全可用
        cases = [
            (1, 1, [[0]]),
            (1, 1, [[1]]),
            (2, 2, [[1, 1], [1, 1]]),
        ]
        input_data = self._build_input(cases)

        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)

        self.assertEqual(self._parse_output(got), self._parse_output(expected))

    def test_with_holes(self):
        # 含插座（洞）的案例
        cases = [
            (2, 3, [[1, 0, 1], [1, 1, 1]]),
            (3, 3, [[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        ]
        input_data = self._build_input(cases)

        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)

        self.assertEqual(self._parse_output(got), self._parse_output(expected))

    def test_output_format(self):
        # 驗證輸出格式必須是 Case i: ans
        input_data = self._build_input([(1, 1, [[0]])])
        got = self._run_target(input_data)
        parsed = self._parse_output(got)

        self.assertEqual(parsed, [1])

    def test_randomized_small_against_reference(self):
        # 小範圍隨機對拍（2x2、2x3、3x3）
        random.seed(10235)
        shapes = [(2, 2), (2, 3), (3, 3)]

        cases = []
        for _ in range(18):
            n, m = random.choice(shapes)
            grid = []
            for _r in range(n):
                row = []
                for _c in range(m):
                    row.append(1 if random.random() < 0.7 else 0)
                grid.append(row)
            cases.append((n, m, grid))

        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)

        self.assertEqual(self._parse_output(got), self._parse_output(expected))


if __name__ == "__main__":
    unittest.main(verbosity=2)
