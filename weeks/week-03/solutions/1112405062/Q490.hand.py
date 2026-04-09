import sys


def rotate(lines):
    """旋轉矩陣"""
    if not lines:
        return []

    # 1. 墊高：讓每行長度一樣
    w = max(len(x) for x in lines)
    p = [x.ljust(w) for x in lines]

    # 2. 旋轉：顛倒 + 轉置
    return ["".join(p[r][c] for r in range(len(p) - 1, -1, -1)) for c in range(w)]


if __name__ == "__main__":
    print("\n".join(rotate(sys.stdin.read().splitlines())))