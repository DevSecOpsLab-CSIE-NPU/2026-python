import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10242(unittest.TestCase):
    """題目 10242（ATM 最大可搶金額）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10242.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10242.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10242.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先嘗試 import 模式，失敗時再退回 subprocess 腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10242", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(n, edges, money, start, bars):
        lines = [f"{n} {len(edges)}"]
        for u, v in edges:
            lines.append(f"{u} {v}")
        for x in money:
            lines.append(str(x))
        lines.append(f"{start} {len(bars)}")
        lines.append(" ".join(str(x) for x in bars))
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_output(text):
        data = text.strip().split()
        if not data:
            raise AssertionError("輸出為空，預期應輸出一個整數")
        return int(data[0])

    @staticmethod
    def _reference_bruteforce_small(n, edges, money, start, bars):
        """小圖暴力參考解。

        狀態定義：
        - 位置 node（1-based）
        - 已搶節點集合 mask（bitmask）
        - 對應的已搶總額 total

        由於可重走邊/點，所以必須把「是否已搶過某節點」放進狀態。
        這個方法只用在小圖隨機對拍（n <= 8）。
        """
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)

        start_mask = 1 << (start - 1)
        best = {(start, start_mask): money[start - 1]}
        stack = [(start, start_mask)]

        while stack:
            node, mask = stack.pop()
            cur_total = best[(node, mask)]

            for nxt in adj[node]:
                bit = 1 << (nxt - 1)
                if mask & bit:
                    nxt_mask = mask
                    nxt_total = cur_total
                else:
                    nxt_mask = mask | bit
                    nxt_total = cur_total + money[nxt - 1]

                key = (nxt, nxt_mask)
                if key not in best or nxt_total > best[key]:
                    best[key] = nxt_total
                    stack.append(key)

        ans = 0
        bar_set = set(bars)
        for (node, _mask), total in best.items():
            if node in bar_set and total > ans:
                ans = total
        return ans

    def _run_target(self, input_data):
        module = self.target_module

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
                    if isinstance(result, int):
                        return str(result) + "\n"

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_simple_chain(self):
        # 1 -> 2 -> 3，酒吧在 3，答案為 1+2+3=6
        n = 3
        edges = [(1, 2), (2, 3)]
        money = [1, 2, 3]
        start = 1
        bars = [3]

        input_data = self._build_input(n, edges, money, start, bars)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, 6)

    def test_cycle_collect_once(self):
        # 有環 1->2->3->1，雖可重走但每點只搶一次
        # 走到酒吧 4 的最佳路徑：1->2->3->4，總和 5+6+7+8=26
        n = 4
        edges = [(1, 2), (2, 3), (3, 1), (3, 4)]
        money = [5, 6, 7, 8]
        start = 1
        bars = [4]

        input_data = self._build_input(n, edges, money, start, bars)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, 26)

    def test_unreachable_bars(self):
        # 酒吧不可達時，答案應為 0
        n = 4
        edges = [(1, 2)]
        money = [10, 20, 30, 40]
        start = 1
        bars = [3, 4]

        input_data = self._build_input(n, edges, money, start, bars)
        got = self._parse_output(self._run_target(input_data))
        self.assertEqual(got, 0)

    def test_randomized_small_against_bruteforce(self):
        # 小圖隨機對拍：以暴力狀態圖當參考答案
        random.seed(10242)

        for _ in range(40):
            n = random.randint(2, 8)

            edges = []
            for u in range(1, n + 1):
                for v in range(1, n + 1):
                    if u != v and random.random() < 0.22:
                        edges.append((u, v))

            # 保證至少有一些邊，避免全空圖過度單一
            if not edges:
                u = random.randint(1, n)
                v = random.randint(1, n)
                while v == u:
                    v = random.randint(1, n)
                edges.append((u, v))

            money = [random.randint(0, 20) for _ in range(n)]
            start = random.randint(1, n)

            bar_count = random.randint(1, n)
            bars = random.sample(list(range(1, n + 1)), bar_count)

            input_data = self._build_input(n, edges, money, start, bars)
            expected = self._reference_bruteforce_small(n, edges, money, start, bars)
            got = self._parse_output(self._run_target(input_data))

            self.assertEqual(
                got,
                expected,
                msg=(
                    f"failed n={n}, edges={edges}, money={money}, "
                    f"start={start}, bars={bars}"
                ),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
