"""
UVA 10101 / ZeroJudge a094
手打解題版（可直接提交 OJ）

題意：
給一個不成立等式，若能只移動一根木棒（僅可動數字七段顯示）使等式成立，
輸出新等式（含 #）；否則輸出 No。
"""

from __future__ import annotations

from datetime import datetime
import sys


DIGIT_TO_MASK: dict[str, int] = {
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


def trim_to_expr(raw: str) -> str:
    p = raw.find("#")
    if p == -1:
        return raw + "#"
    return raw[:p] + "#"


def eval_side(side: str) -> int:
    i = 0
    total = 0
    n = len(side)

    while i < n:
        sign = 1
        if side[i] == "+":
            i += 1
        elif side[i] == "-":
            sign = -1
            i += 1

        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            return 10**30

        total += sign * int(side[i:j])
        i = j

    return total


def is_equation_true(body: str) -> bool:
    if body.count("=") != 1:
        return False
    left, right = body.split("=", 1)
    return eval_side(left) == eval_side(right)


def replace_char(s: str, idx: int, ch: str) -> str:
    return s[:idx] + ch + s[idx + 1 :]


def build_transition_tables() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    remove1: dict[str, list[str]] = {str(x): [] for x in range(10)}
    add1: dict[str, list[str]] = {str(x): [] for x in range(10)}
    move1: dict[str, list[str]] = {str(x): [] for x in range(10)}

    for d in range(10):
        dch = str(d)
        mask = DIGIT_TO_MASK[dch]

        for nd in range(10):
            nch = str(nd)
            nmask = DIGIT_TO_MASK[nch]

            removed = (mask & ~nmask).bit_count()
            added = (nmask & ~mask).bit_count()

            if removed == 1 and added == 0:
                remove1[dch].append(nch)
            if removed == 0 and added == 1:
                add1[dch].append(nch)
            if removed == 1 and added == 1:
                move1[dch].append(nch)

    return remove1, add1, move1


REMOVE1, ADD1, MOVE1 = build_transition_tables()


def solve(raw_expr: str) -> str:
    expr = trim_to_expr(raw_expr)
    body = expr[:-1]
    digit_pos = [i for i, ch in enumerate(body) if ch.isdigit()]

    # 情況 1：同一數字內搬一根
    for i in digit_pos:
        old = body[i]
        for nd in MOVE1[old]:
            cand = replace_char(body, i, nd)
            if is_equation_true(cand):
                return cand + "#"

    # 情況 2：從 i 拿一根，搬到 j
    for i in digit_pos:
        src_old = body[i]
        for src_new in REMOVE1[src_old]:
            removed_body = replace_char(body, i, src_new)

            for j in digit_pos:
                if j == i:
                    continue
                dst_old = body[j]
                for dst_new in ADD1[dst_old]:
                    cand = replace_char(removed_body, j, dst_new)
                    if is_equation_true(cand):
                        return cand + "#"

    return "No"


def run_selftest_and_log() -> int:
    """執行內建小測試並輸出 LOG 檔，回傳失敗數量。"""
    cases = [
        ("1+1=3#", True),
        ("9-5=3#", False),
        ("1+1=2#", False),
    ]

    fail = 0
    lines: list[str] = []
    lines.append(f"[{datetime.now().isoformat(timespec='seconds')}] selftest start")

    for idx, (expr, should_have_solution) in enumerate(cases, start=1):
        got = solve(expr)
        ok = (got != "No") if should_have_solution else (got == "No")
        if not ok:
            fail += 1
        lines.append(
            f"case {idx}: expr={expr}, should_have_solution={should_have_solution}, got={got}, ok={ok}"
        )

    lines.append(f"summary: total={len(cases)}, failed={fail}, passed={len(cases) - fail}")

    log_path = __file__.replace(".py", "_test.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return fail


def main() -> None:
    raw = sys.stdin.read()
    if not raw:
        return

    line = raw.splitlines()[0] if "\n" in raw else raw
    print(solve(line.strip()))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "selftest":
        failed = run_selftest_and_log()
        print(f"selftest finished, failed={failed}")
    else:
        main()
