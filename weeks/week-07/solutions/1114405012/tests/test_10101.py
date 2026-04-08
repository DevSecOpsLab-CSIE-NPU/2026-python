"""10101 單元測試（黑箱）。

測試策略：
- 先用小型暴力產生「所有一根木棒可達的正確等式」
- 再比對程式輸出是否在可行解集合中
- 若集合為空，程式應輸出 No
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


SEG = {
    "0": frozenset("abcefd"),
    "1": frozenset("bc"),
    "2": frozenset("abdeg"),
    "3": frozenset("abcdg"),
    "4": frozenset("bcfg"),
    "5": frozenset("acdfg"),
    "6": frozenset("acdefg"),
    "7": frozenset("abc"),
    "8": frozenset("abcdefg"),
    "9": frozenset("abcdfg"),
}


def parse_side(side: str) -> int | None:
    # 解析單側算式（僅 + / -），非法格式回傳 None。
    i = 0
    n = len(side)
    sign = 1
    total = 0
    if i < n and side[i] in "+-":
        sign = 1 if side[i] == "+" else -1
        i += 1
    while i < n:
        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            return None
        total += sign * int(side[i:j])
        if j == n:
            return total
        op = side[j]
        if op not in "+-":
            return None
        sign = 1 if op == "+" else -1
        i = j + 1
    return total


def is_valid(expr: str) -> bool:
    # 判斷等式是否格式正確且左右值相等。
    if expr.count("=") != 1:
        return False
    l, r = expr.split("=", 1)
    lv = parse_side(l)
    rv = parse_side(r)
    return lv is not None and rv is not None and lv == rv


def transitions(d: str) -> tuple[list[str], list[str], list[str]]:
    # 列出一根木棒操作下，數字 d 可到達的數字集合。
    s = SEG[d]
    rem, add, mov = [], [], []
    for e, t in SEG.items():
        if e == d:
            continue
        if len(s) == len(t) + 1 and t.issubset(s):
            rem.append(e)
        if len(s) + 1 == len(t) and s.issubset(t):
            add.append(e)
        if len(s) == len(t) and len(s ^ t) == 2:
            mov.append(e)
    return rem, add, mov


def brute_solutions(raw: str) -> set[str]:
    # 暴力找出「所有」只移動一根木棒後可成立的等式。
    expr = raw.split("#", 1)[0]
    chars = list(expr)
    dpos = [i for i, ch in enumerate(chars) if ch.isdigit()]
    trans = {d: transitions(d) for d in SEG}

    sols: set[str] = set()

    for i in dpos:
        d = chars[i]
        _rem, _add, mov = trans[d]
        for nd in mov:
            cand = chars[:]
            cand[i] = nd
            cexpr = "".join(cand)
            if is_valid(cexpr):
                sols.add(cexpr + "#")

    for i in dpos:
        d1 = chars[i]
        rem1, _add1, _mov1 = trans[d1]
        for nd1 in rem1:
            for j in dpos:
                if i == j:
                    continue
                d2 = chars[j]
                _rem2, add2, _mov2 = trans[d2]
                for nd2 in add2:
                    cand = chars[:]
                    cand[i] = nd1
                    cand[j] = nd2
                    cexpr = "".join(cand)
                    if is_valid(cexpr):
                        sols.add(cexpr + "#")

    return sols


class Test10101(unittest.TestCase):
    def setUp(self) -> None:
        # 目標程式路徑。
        self.root = Path(__file__).resolve().parents[1]
        self.script = self.root / "10101.py"
        if not self.script.exists():
            self.fail("找不到 10101.py")

    def run_case(self, raw: str) -> str:
        # 黑箱執行程式並取標準輸出。
        p = subprocess.run(
            [sys.executable, str(self.script)],
            input=raw,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(p.returncode, 0, msg=p.stderr)
        return p.stdout.strip()

    def test_matchstick_cases(self):
        # 混合多組案例：有解、可能無解、含加減號等。
        cases = [
            "1+1=3#",
            "2+3=9#",
            "0+0=0#",
            "9-5=3#",
            "6+4=4#",
        ]

        for raw in cases:
            expected_set = brute_solutions(raw)
            out = self.run_case(raw + "\n")
            with self.subTest(expr=raw):
                if expected_set:
                    self.assertIn(out, expected_set)
                else:
                    self.assertEqual(out, "No")


if __name__ == "__main__":
    unittest.main()
