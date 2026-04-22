import os
import random
import subprocess
import sys
import unittest
from itertools import permutations
from pathlib import Path
import importlib.util


class TestQuestion10226(unittest.TestCase):
    """題目 10226（a219 限制排列）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10226.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10226.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10226.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 優先嘗試匯入，方便直接測函式；失敗再退回 subprocess
        try:
            spec = importlib.util.spec_from_file_location("target_10226", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _build_input(cases):
        # cases 格式：[(n, [set(), set({1,3}), ...]), ...]
        lines = []
        for n, dislike in cases:
            lines.append(str(n))
            for i in range(n):
                bad_positions = sorted(dislike[i])
                if bad_positions:
                    lines.append(" ".join(str(x) for x in bad_positions) + " 0")
                else:
                    lines.append("0")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _parse_input(text):
        lines = [line.strip() for line in text.splitlines()]
        idx = 0
        cases = []

        while idx < len(lines):
            if lines[idx] == "":
                idx += 1
                continue

            n = int(lines[idx])
            idx += 1
            dislike = []

            for _ in range(n):
                if idx >= len(lines):
                    raise AssertionError("輸入格式不完整：缺少限制行")
                nums = [int(x) for x in lines[idx].split()]
                idx += 1

                cur = set()
                for x in nums:
                    if x == 0:
                        break
                    cur.add(x)
                dislike.append(cur)

            cases.append((n, dislike))

        return cases

    @staticmethod
    def _compress_by_previous(valid_perms):
        # 只輸出與上一組不同的後綴：找到第一個不同位置後輸出剩餘字串
        if not valid_perms:
            return []

        out = [valid_perms[0]]
        prev = valid_perms[0]

        for cur in valid_perms[1:]:
            first_diff = 0
            while first_diff < len(cur) and cur[first_diff] == prev[first_diff]:
                first_diff += 1
            out.append(cur[first_diff:])
            prev = cur

        return out

    @classmethod
    def _reference_solve_from_text(cls, input_data):
        # 參考解：枚舉排列、套用限制、再做差異後綴輸出
        cases = cls._parse_input(input_data)
        blocks = []

        for n, dislike in cases:
            names = [chr(ord("A") + i) for i in range(n)]
            valid = []

            for p in permutations(names):
                ok = True
                for person_idx in range(n):
                    pos_1_based = p.index(names[person_idx]) + 1
                    if pos_1_based in dislike[person_idx]:
                        ok = False
                        break
                if ok:
                    valid.append("".join(p))

            block = cls._compress_by_previous(valid)
            blocks.append("\n".join(block))

        return "\n\n".join(blocks) + "\n"

    @staticmethod
    def _normalize_output(text):
        # 以「每行右側去空白」做正規化，保留空行，避免換行風格造成誤判
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines).rstrip() + "\n"

    def _run_target(self, input_data):
        module = self.target_module

        # 優先嘗試常見函式介面
        if module is not None:
            for fn_name in ("solve", "solve_text", "solve_io", "run"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(input_data)
                    except TypeError:
                        # 若函式參數不是文字，改走腳本模式
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
        # 題目範例：驗證「字典序 + 差異後綴輸出」規則是否正確
        sample_input = (
            "3\n"
            "0\n"
            "0\n"
            "0\n"
            "3\n"
            "1 0\n"
            "3 0\n"
            "0\n"
        )
        expected = self._reference_solve_from_text(sample_input)
        got = self._run_target(sample_input)
        self.assertEqual(self._normalize_output(got), self._normalize_output(expected))

    def test_single_person_allows_only_one(self):
        # N=1 且無限制，只會輸出 A
        input_data = "1\n0\n"
        expected = "A\n"
        got = self._run_target(input_data)
        self.assertEqual(self._normalize_output(got), self._normalize_output(expected))

    def test_no_valid_permutation(self):
        # A 不可在 1、B 不可在 2（N=2）時沒有任何合法排列
        input_data = "2\n1 0\n2 0\n"
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._normalize_output(got), self._normalize_output(expected))

    def test_multiple_cases_and_blank_line(self):
        # 多測資時，案例之間需保留一個空行
        input_data = (
            "2\n"
            "0\n"
            "0\n"
            "2\n"
            "1 0\n"
            "0\n"
        )
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._normalize_output(got), self._normalize_output(expected))

    def test_randomized_against_reference(self):
        # 小規模隨機對拍：N<=7，精確比對參考解
        random.seed(10226)
        cases = []
        case_count = 24

        for _ in range(case_count):
            n = random.randint(1, 7)
            dislike = []
            for _person in range(n):
                banned = set()
                for pos in range(1, n + 1):
                    # 以固定機率產生不想站的位置，保持測資多樣性
                    if random.random() < 0.28:
                        banned.add(pos)
                dislike.append(banned)
            cases.append((n, dislike))

        input_data = self._build_input(cases)
        expected = self._reference_solve_from_text(input_data)
        got = self._run_target(input_data)
        self.assertEqual(self._normalize_output(got), self._normalize_output(expected))


if __name__ == "__main__":
    unittest.main(verbosity=2)
