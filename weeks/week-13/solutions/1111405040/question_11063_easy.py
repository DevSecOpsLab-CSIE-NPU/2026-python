"""
UVA 11063 B2-Sequence 簡單版。
"""

from __future__ import annotations


def check_b2(numbers: list[int]) -> bool:
    """用最直接的條件檢查是否符合 B2-Sequence。"""
    if not numbers:
        return False

    for index, number in enumerate(numbers):
        if number < 1:
            return False
        if index > 0 and numbers[index - 1] >= number:
            return False

    used: set[int] = set()
    for left in range(len(numbers)):
        for right in range(left, len(numbers)):
            value = numbers[left] + numbers[right]
            if value in used:
                return False
            used.add(value)

    return True


def solve(data: str) -> str:
    """依序處理每一組輸入。"""
    tokens = data.split()
    index = 0
    case_number = 1
    lines: list[str] = []

    while index < len(tokens):
        count = int(tokens[index])
        index += 1
        numbers = [int(token) for token in tokens[index:index + count]]
        index += count

        if check_b2(numbers):
            lines.append(f"Case #{case_number}: It is a B2-Sequence.\n")
        else:
            lines.append(f"Case #{case_number}: It is not a B2-Sequence.\n")
        case_number += 1

    return "\n".join(lines).rstrip()


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
