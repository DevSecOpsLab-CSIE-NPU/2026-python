"""
UVA 11150 Cola。
"""

from __future__ import annotations


def max_colas(initial_bottles: int) -> int:
    """計算最多能喝到幾瓶可樂。"""
    # 這題允許在最後向店家借一個空瓶來完成最後一次交換，
    # 因此答案可以化簡成 n + n // 2。
    return initial_bottles + initial_bottles // 2


def solve(data: str) -> str:
    """處理多筆輸入直到 EOF。"""
    outputs: list[str] = []
    for token in data.split():
        outputs.append(str(max_colas(int(token))))
    return "\n".join(outputs)


def main() -> None:
    """讀取標準輸入並輸出答案。"""
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
