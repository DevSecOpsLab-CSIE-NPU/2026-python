"""
UVA 10071: Back to High School Physics（簡單版）
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    """每行讀入 v 與 t，直接輸出 2*v*t。"""
    results: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        v_str, t_str = line.split()
        v = int(v_str)
        t = int(t_str)
        results.append(str(2 * v * t))

    return "\n".join(results)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
