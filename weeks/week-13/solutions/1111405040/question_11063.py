"""
UVA 11063 B2-Sequence。
"""

from __future__ import annotations


def is_b2_sequence(numbers: list[int]) -> bool:
    """判斷是否為 B2-Sequence。"""
    if not numbers:
        return False

    # B2-Sequence 需要全部是正整數，且必須嚴格遞增。
    if numbers[0] < 1:
        return False
    for left, right in zip(numbers, numbers[1:]):
        if left >= right:
            return False

    # 任意 i <= j 的兩數和都不能重複。
    seen_sums: set[int] = set()
    for index, first in enumerate(numbers):
        for second in numbers[index:]:
            pair_sum = first + second
            if pair_sum in seen_sums:
                return False
            seen_sums.add(pair_sum)

    return True


def solve(data: str) -> str:
    """處理直到 EOF 的多組測資。"""
    tokens = data.split()
    index = 0
    case_number = 1
    outputs: list[str] = []

    while index < len(tokens):
        count = int(tokens[index])
        index += 1

        numbers = [int(token) for token in tokens[index:index + count]]
        index += count

        if is_b2_sequence(numbers):
            message = "It is a B2-Sequence."
        else:
            message = "It is not a B2-Sequence."

        outputs.append(f"Case #{case_number}: {message}\n")
        case_number += 1

    return "\n".join(outputs).rstrip()


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
