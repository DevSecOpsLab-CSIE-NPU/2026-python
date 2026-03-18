from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10019（依題目敘述內容）
    每組輸入有兩個整數，輸出其差的絕對值。
    """
    tokens = data.split()
    if len(tokens) < 2:
        return ""

    values = [int(token) for token in tokens]
    result_lines: list[str] = []

    # 每兩個整數為一組測資
    for i in range(0, len(values) - 1, 2):
        a = values[i]
        b = values[i + 1]
        result_lines.append(str(abs(a - b)))

    return "\n".join(result_lines)


def main() -> None:
    raw_input = sys.stdin.read()
    sys.stdout.write(solve(raw_input))


if __name__ == "__main__":
    main()
