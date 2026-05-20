"""
UVA 11321 Sort! Sort!! and Sort!!!。
"""

from __future__ import annotations


def c_style_mod(number: int, divisor: int) -> int:
    """模擬 C / C++ 對負數取餘數的結果。"""
    remainder = number % divisor
    if number < 0 and remainder != 0:
        return remainder - divisor
    return remainder


def sort_numbers(numbers: list[int], modulus: int) -> list[int]:
    """依題目指定規則排序。"""

    def sort_key(number: int) -> tuple[int, int, int]:
        remainder = c_style_mod(number, modulus)
        is_odd = abs(number) % 2 == 1

        # 餘數小的先排。
        # 奇數排在偶數前面。
        # 奇數依數值遞減，偶數依數值遞增。
        if is_odd:
            return (remainder, 0, -number)
        return (remainder, 1, number)

    return sorted(numbers, key=sort_key)


def solve(data: str) -> str:
    """處理多組資料直到 0 0。"""
    tokens = data.split()
    index = 0
    outputs: list[str] = []

    while index < len(tokens):
        count = int(tokens[index])
        modulus = int(tokens[index + 1])
        index += 2

        outputs.append(f"{count} {modulus}")
        if count == 0 and modulus == 0:
            break

        numbers = [int(token) for token in tokens[index:index + count]]
        index += count

        outputs.extend(str(number) for number in sort_numbers(numbers, modulus))

    return "\n".join(outputs)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
