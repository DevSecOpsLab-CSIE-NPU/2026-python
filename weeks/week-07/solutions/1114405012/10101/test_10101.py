"""10101 單元測試。

重點檢查：
1) 有解時，輸出必須是合法等式且以 # 結尾。
2) 新舊字串之間必須符合「只移動一根數字木棒」。
3) 無解時輸出 No。
"""

import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path


DEFAULT_FILE = "10101.py"

SEG = {
    "0": 0b1111110,
    "1": 0b0110000,
    "2": 0b1101101,
    "3": 0b1111001,
    "4": 0b0110011,
    "5": 0b1011011,
    "6": 0b1011111,
    "7": 0b1110000,
    "8": 0b1111111,
    "9": 0b1111011,
}


def bit_count(x: int) -> int:
    return bin(x).count("1")


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()).strip()


def eval_side(side_expr: str) -> int:
    i = 0
    n = len(side_expr)
    total = 0
    while i < n:
        sign = 1
        if side_expr[i] == "+":
            i += 1
        elif side_expr[i] == "-":
            sign = -1
            i += 1

        j = i
        while j < n and side_expr[j].isdigit():
            j += 1
        num = int(side_expr[i:j])
        total += sign * num
        i = j
    return total


def is_valid_equation(expr_with_hash: str) -> bool:
    if not expr_with_hash.endswith("#"):
        return False
    expr = expr_with_hash[:-1]
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=")
    return eval_side(left) == eval_side(right)


def is_one_stick_move(old_with_hash: str, new_with_hash: str) -> bool:
    if not old_with_hash.endswith("#") or not new_with_hash.endswith("#"):
        return False

    old_expr = old_with_hash[:-1]
    new_expr = new_with_hash[:-1]

    if len(old_expr) != len(new_expr):
        return False

    removed = 0
    added = 0
    for oc, nc in zip(old_expr, new_expr):
        if oc.isdigit() != nc.isdigit():
            return False

        if not oc.isdigit():
            if oc != nc:
                return False
            continue

        mo = SEG[oc]
        mn = SEG[nc]
        removed += bit_count(mo & ~mn)
        added += bit_count(mn & ~mo)

    return removed == 1 and added == 1


class Runner:
    def __init__(self):
        base = Path(__file__).resolve().parent
        env = os.environ.get("SOLUTION_FILE")
        self.path = (base / DEFAULT_FILE) if not env else Path(env).resolve()
        if not self.path.exists():
            raise FileNotFoundError(f"找不到解答檔：{self.path}")

    def run(self, input_data: str) -> str:
        mod = self._load_module(self.path)
        if mod is not None and hasattr(mod, "solve"):
            out = mod.solve(input_data)
            return normalize(str(out))

        proc = subprocess.run(
            [sys.executable, str(self.path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr)
        return normalize(proc.stdout)

    @staticmethod
    def _load_module(path: Path):
        try:
            spec = importlib.util.spec_from_file_location("student_solution_10101", path)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            return None


class Test10101(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = Runner()

    def assert_solvable(self, expr: str):
        inp = expr
        out = self.runner.run(inp)
        self.assertNotEqual(out, "No")
        self.assertTrue(is_valid_equation(out), msg=f"輸出非合法等式: {out}")
        self.assertTrue(is_one_stick_move(inp, out), msg=f"不是單次移棒: {inp} -> {out}")

    def test_simple_solvable_1(self):
        self.assert_solvable("1+1=3#")

    def test_simple_solvable_2(self):
        self.assert_solvable("0+0=6#")

    def test_no_solution(self):
        out = self.runner.run("1=1#")
        self.assertEqual(out, "No")


if __name__ == "__main__":
    unittest.main(verbosity=2)
