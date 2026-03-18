"""題目 10019 附件描述版本：輸出兩數差的絕對值。"""

import sys


def solve(text: str) -> str:
    """逐行讀入兩個整數，輸出其正差值。"""
    outputs: list[str] = []

    for line in text.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        left, right = map(int, parts)
        # 題目要正數差值，因此直接取絕對值即可。
        outputs.append(str(abs(left - right)))

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))