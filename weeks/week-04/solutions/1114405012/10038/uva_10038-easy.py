from __future__ import annotations

import sys


def is_jolly(nums: list[int]) -> bool:
    """
    判斷序列是否為 Jolly Jumper。

    長度 n 的序列，如果相鄰差的絕對值剛好湊齊 {1,2,...,n-1}，就是 Jolly。
    """
    n = len(nums)
    if n <= 1:
        # 長度 0 或 1 沒有相鄰差，自然視為 Jolly
        return True

    # 收集所有相鄰差的絕對值
    diff_set: set[int] = set()
    for i in range(1, n):
        diff_set.add(abs(nums[i] - nums[i - 1]))

    # easy 版直接比對集合是否完全相同：
    # 需要剛好包含 1 到 n-1，每個值都出現過（至少一次）
    need_set = set(range(1, n))
    return diff_set == need_set


def solve(data: str) -> str:
    """
    UVA 10038 easy 版

    每筆資料格式：
    n a1 a2 ... an
    讀到 EOF 為止。

    這裡使用 token 方式解析，可容忍換行位置不固定。
    """
    tokens = data.split()
    i = 0
    ans: list[str] = []

    # 每回合先讀一個 n，再讀 n 個整數
    while i < len(tokens):
        n = int(tokens[i])
        i += 1

        # 如果剩餘 token 不夠 n 個，代表輸入不完整，直接停止
        if i + n > len(tokens):
            break

        arr = [int(tokens[i + j]) for j in range(n)]
        i += n

        if is_jolly(arr):
            ans.append("Jolly")
        else:
            ans.append("Not jolly")

    # 每筆測資結果占一行
    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()
