"""題目 10019 附件描述版本：容易記憶寫法。"""

import sys


def solve(text: str) -> str:
    result = []
    for line in text.splitlines():
        if not line.strip():
            continue
        a, b = map(int, line.split())
        # Python 整數沒有固定長度限制，適合直接處理大數。
        result.append(str(abs(a - b)))
    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))