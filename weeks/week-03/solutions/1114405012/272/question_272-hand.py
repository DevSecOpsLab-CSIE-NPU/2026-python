"""
UVA 272 手打版（簡單好記）

規則：
遇到雙引號時依序換成 ``、''、``、''...
其他字元保持不變。
"""


def convert_hand(text: str) -> str:
    out = []
    open_now = True

    for c in text:
        if c == '"':
            out.append("``" if open_now else "''")
            open_now = not open_now
        else:
            out.append(c)

    return "".join(out)


def solve_all(text: str) -> str:
    return convert_hand(text)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data:
        print(solve_all(data), end="")
