import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


SEG_MASK = {
    "0": 0b0111111,
    "1": 0b0000110,
    "2": 0b1011011,
    "3": 0b1001111,
    "4": 0b1100110,
    "5": 0b1101101,
    "6": 0b1111101,
    "7": 0b0000111,
    "8": 0b1111111,
    "9": 0b1101111,
}
DIGITS = "0123456789"


def build_transitions():
    remove_map = {d: [] for d in DIGITS}
    add_map = {d: [] for d in DIGITS}
    move_within_map = {d: [] for d in DIGITS}

    for a in DIGITS:
        ma = SEG_MASK[a]
        ca = ma.bit_count()
        for b in DIGITS:
            if a == b:
                continue
            mb = SEG_MASK[b]
            cb = mb.bit_count()
            diff = (ma ^ mb).bit_count()

            if diff == 1:
                if ca == cb + 1:
                    remove_map[a].append(b)
                elif cb == ca + 1:
                    add_map[a].append(b)
            elif diff == 2 and ca == cb:
                move_within_map[a].append(b)

    for d in DIGITS:
        remove_map[d].sort()
        add_map[d].sort()
        move_within_map[d].sort()

    return remove_map, add_map, move_within_map


REMOVE_MAP, ADD_MAP, MOVE_WITHIN_MAP = build_transitions()


def eval_side(side):
    i = 0
    n = len(side)
    sign = 1
    total = 0

    while i < n:
        ch = side[i]
        if ch == "+":
            sign = 1
            i += 1
            continue
        if ch == "-":
            sign = -1
            i += 1
            continue

        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            return None

        total += sign * int(side[i:j])
        i = j

    return total


def is_equation_true(expr):
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=")
    lv = eval_side(left)
    rv = eval_side(right)
    if lv is None or rv is None:
        return False
    return lv == rv


def reference_solutions(expr):
    positions = [i for i, ch in enumerate(expr) if ch.isdigit()]
    chars = list(expr)
    out = set()

    for i in positions:
        old_i = chars[i]
        for new_i in MOVE_WITHIN_MAP[old_i]:
            cand = chars[:]
            cand[i] = new_i
            s = "".join(cand)
            if is_equation_true(s):
                out.add(s + "#")

    for i in positions:
        old_i = chars[i]
        for mid_i in REMOVE_MAP[old_i]:
            for j in positions:
                if j == i:
                    continue
                old_j = chars[j]
                for new_j in ADD_MAP[old_j]:
                    cand = chars[:]
                    cand[i] = mid_i
                    cand[j] = new_j
                    s = "".join(cand)
                    if is_equation_true(s):
                        out.add(s + "#")

    return out


class TestQuestion10101(unittest.TestCase):
    """題目 10101（移動一根木棒）單元測試。"""

    @classmethod
    def setUpClass(cls):
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10101.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案: {cls.target_file}。請建立 10101.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path):
        try:
            spec = importlib.util.spec_from_file_location("target_10101", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    def _run_target(self, expr):
        input_data = expr + "#ignored tail\n"
        m = self.target_module

        if m is not None and hasattr(m, "solve"):
            result = m.solve(input_data)
            return str(result).strip()

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def _assert_matches_reference(self, expr):
        expected_set = reference_solutions(expr)
        got = self._run_target(expr)

        if not expected_set:
            self.assertEqual(got, "No", msg=f"expr={expr}")
        else:
            self.assertIn(got, expected_set, msg=f"expr={expr}, expected={sorted(expected_set)[:5]}")

    def test_known_solvable(self):
        self._assert_matches_reference("1+1=3")

    def test_known_unsolvable(self):
        self._assert_matches_reference("1=1")

    def test_with_negative_numbers(self):
        self._assert_matches_reference("-3+1=-9")

    def test_randomized_against_reference(self):
        random.seed(10101)

        def rand_num():
            if random.random() < 0.2:
                return "0"
            length = random.randint(1, 3)
            first = str(random.randint(1, 9))
            rest = "".join(str(random.randint(0, 9)) for _ in range(length - 1))
            return first + rest

        def rand_side():
            terms = random.randint(1, 3)
            parts = []
            first = rand_num()
            if random.random() < 0.3:
                first = "-" + first
            parts.append(first)

            for _ in range(terms - 1):
                op = random.choice(["+", "-"])
                parts.append(op + rand_num())
            return "".join(parts)

        for _ in range(80):
            expr = rand_side() + "=" + rand_side()
            self._assert_matches_reference(expr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
