"""UVA 490 - Rotating Sentences"""

import sys


def solve(text: str) -> str:
    src = text.splitlines()
    if not src:
        return ""

    max_len = max(len(line) for line in src)
    result = []

    for c in range(max_len):
        current = []
        for r in range(len(src) - 1, -1, -1):
            if c < len(src[r]):
                current.append(src[r][c])
            else:
                current.append(" ")
        result.append("".join(current).rstrip())

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
