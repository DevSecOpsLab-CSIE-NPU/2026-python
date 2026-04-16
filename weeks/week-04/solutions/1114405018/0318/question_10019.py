"""UVA 10019（依題目敘述）

讀入多行，每行兩個整數，輸出兩者差值的絕對值。
"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        out.append(str(abs(a - b)))
    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
