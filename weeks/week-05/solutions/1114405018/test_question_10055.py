import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10055(unittest.TestCase):
    """題目 10055（函數增減性查詢）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10055.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10055.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10055.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 嘗試載入模組；失敗時退回 subprocess 腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10055", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _reference_simulate(n, operations):
        # 參考解：直接維護每個函數目前是否為減函數（0=增，1=減）
        state = [0] * (n + 1)
        out = []

        for op in operations:
            if op[0] == 1:
                i = op[1]
                state[i] ^= 1
            else:
                l, r = op[1], op[2]
                parity = sum(state[l:r + 1]) % 2
                out.append(parity)

        return out

    @staticmethod
    def _build_input(n, operations):
        # 組回題目輸入格式
        lines = [f"{n} {len(operations)}"]
        for op in operations:
            lines.append(" ".join(map(str, op)))
        return "\n".join(lines) + "\n"

    def _run_target(self, n, operations):
        # 優先測函式，找不到再跑整支腳本
        m = self.target_module
        input_data = self._build_input(n, operations)

        if m is not None and hasattr(m, "process_queries"):
            result = m.process_queries(n, operations)
            return [int(x) for x in result]

        if m is not None and hasattr(m, "solve"):
            output = str(m.solve(input_data)).strip()
            if not output:
                return []
            return [int(x) for x in output.split()]

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        output = completed.stdout.strip()
        if not output:
            return []
        return [int(x) for x in output.split()]

    def test_only_queries_no_flips(self):
        # 全部維持增函數，任何查詢都應為 0
        n = 5
        operations = [
            (2, 1, 1),
            (2, 1, 5),
            (2, 3, 4),
        ]
        expected = [0, 0, 0]
        got = self._run_target(n, operations)
        self.assertEqual(got, expected)

    def test_flip_and_query_basic(self):
        # 基本翻轉與查詢混合測試
        n = 6
        operations = [
            (1, 2),      # f2: 減
            (2, 1, 3),   # 區間有 1 個減 -> 1
            (1, 3),      # f3: 減
            (2, 1, 3),   # 區間有 2 個減 -> 0
            (1, 2),      # f2: 回到增
            (2, 2, 3),   # 區間有 1 個減 -> 1
        ]
        expected = [1, 0, 1]
        got = self._run_target(n, operations)
        self.assertEqual(got, expected)

    def test_edge_single_element_range(self):
        # 查詢單點區間，答案應等於該點目前狀態
        n = 3
        operations = [
            (1, 1),
            (2, 1, 1),
            (2, 2, 2),
            (1, 1),
            (2, 1, 1),
        ]
        expected = [1, 0, 0]
        got = self._run_target(n, operations)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍：與參考模擬結果一致才算通過
        random.seed(10055)
        for _ in range(60):
            n = random.randint(1, 60)
            q = random.randint(1, 180)
            operations = []

            for _ in range(q):
                if random.random() < 0.45:
                    i = random.randint(1, n)
                    operations.append((1, i))
                else:
                    l = random.randint(1, n)
                    r = random.randint(l, n)
                    operations.append((2, l, r))

            expected = self._reference_simulate(n, operations)
            got = self._run_target(n, operations)
            self.assertEqual(got, expected, msg=f"failed n={n}, q={q}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
