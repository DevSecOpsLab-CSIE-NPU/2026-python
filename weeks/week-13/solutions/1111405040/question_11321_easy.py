"""
UVA 11321 Sort! Sort!! and Sort!!! 簡單版。
"""

from __future__ import annotations


def c_mod(number: int, modulus: int) -> int:
    """把 Python 的餘數改成題目需要的 C 風格。"""
    value = number % modulus
    if number < 0 and value != 0:
        value -= modulus
    return value


def solve(data: str) -> str:
    """簡單版做法：每組資料直接排序後輸出。"""
    tokens = data.split()
    index = 0
    lines: list[str] = []

    while index < len(tokens):
        count = int(tokens[index])
        modulus = int(tokens[index + 1])
        index += 2

        lines.append(f"{count} {modulus}")
        if count == 0 and modulus == 0:
            break

        numbers = [int(token) for token in tokens[index:index + count]]
        index += count

        numbers.sort(
            key=lambda number: (
                c_mod(number, modulus),
                0 if abs(number) % 2 == 1 else 1,
                -number if abs(number) % 2 == 1 else number,
            )
        )
        lines.extend(str(number) for number in numbers)

    return "\n".join(lines)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
