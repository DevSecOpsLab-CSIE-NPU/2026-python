"""
UVA 10050 - Hartals（手打版）
口訣：列罷會日 -> 排除五六 -> 去重計數
"""

from __future__ import annotations


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    i = 1
    out = []

    for _ in range(t):
        n = nums[i]
        i += 1
        p = nums[i]
        i += 1

        lost = set()
        for _ in range(p):
            h = nums[i]
            i += 1

            for d in range(h, n + 1, h):
                # day=1 是星期日，故 6=星期五、0=星期六
                if d % 7 in (6, 0):
                    continue
                lost.add(d)

        out.append(str(len(lost)))

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
