"""
UVA 948 - 假幣偵測（正式版）

題意摘要：
  N 枚硬幣中有一枚假的（重量不同，可能偏輕或偏重）。
  進行 K 次天平秤重，每次記錄左右硬幣編號與結果（< > =）。
  找出假幣編號；若無法唯一確定則輸出 0。

解法：
  對每枚硬幣分別假設「偏輕」與「偏重」，
  檢查該假設是否與所有秤重結果一致。
  最終只有一枚硬幣（不論偏輕或偏重）通過所有驗證，即為答案；
  否則輸出 0。

時間複雜度：O(N × K)
空間複雜度：O(K)
"""

from __future__ import annotations

import sys
from typing import Optional


def check_consistent(
    coin: int,
    heavy: bool,
    weighings: list[tuple[list[int], list[int], str]],
) -> bool:
    """
    驗證「coin 號硬幣是假幣且偏重(heavy=True)/偏輕(heavy=False)」
    是否與所有秤重結果一致。

    :param coin:      假幣候選編號（1-based）
    :param heavy:     True = 假幣偏重；False = 假幣偏輕
    :param weighings: [(左側列表, 右側列表, 結果字元)] 的清單
    :return:          全部秤重均一致則回傳 True
    """
    for left, right, result in weighings:
        on_left  = coin in left    # 假幣在左側
        on_right = coin in right   # 假幣在右側

        if result == "=":
            # 兩邊等重 → 假幣不能出現在任何一側
            if on_left or on_right:
                return False

        elif result == "<":
            # 左輕右重
            if on_left and heavy:
                # 假幣偏重卻在左側 → 左側應該更重，矛盾
                return False
            if on_right and not heavy:
                # 假幣偏輕卻在右側 → 右側應該更輕，矛盾
                return False
            if not on_left and not on_right:
                # 假幣不在兩側 → 兩邊應等重，矛盾
                return False

        else:  # ">"
            # 左重右輕
            if on_left and not heavy:
                # 假幣偏輕卻在左側 → 左側應該更輕，矛盾
                return False
            if on_right and heavy:
                # 假幣偏重卻在右側 → 右側應該更重，矛盾
                return False
            if not on_left and not on_right:
                return False

    return True


def find_fake_coin(
    n: int,
    weighings: list[tuple[list[int], list[int], str]],
) -> int:
    """
    從 N 枚硬幣中找出假幣編號。

    :param n:         硬幣總數
    :param weighings: 秤重紀錄清單
    :return:          假幣編號（1-based），無法確定時回傳 0
    """
    candidates: set[int] = set()

    for coin in range(1, n + 1):
        # 嘗試「偏輕」與「偏重」兩種假設
        for heavy in (True, False):
            if check_consistent(coin, heavy, weighings):
                candidates.add(coin)
                break  # 同一枚硬幣只要有一種假設成立即算候選

    return next(iter(candidates)) if len(candidates) == 1 else 0


def parse_input(text: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    """
    解析輸入文字，回傳每組測試資料的 (N, weighings)。
    """
    lines = [l for l in text.strip().splitlines()]
    idx = 0

    def next_line() -> str:
        nonlocal idx
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1
        line = lines[idx]
        idx += 1
        return line.strip()

    m = int(next_line())
    results = []

    for _ in range(m):
        header = next_line().split()
        n, k = int(header[0]), int(header[1])
        weighings = []
        for _ in range(k):
            parts = next_line().split()
            p = int(parts[0])
            left  = list(map(int, parts[1: p + 1]))
            right = list(map(int, parts[p + 1: 2 * p + 1]))
            result_char = next_line()
            weighings.append((left, right, result_char))
        results.append((n, weighings))

    return results


def main() -> None:
    """讀取標準輸入，輸出每組測試的假幣編號。"""
    data = parse_input(sys.stdin.read())
    output = []
    for n, weighings in data:
        output.append(str(find_fake_coin(n, weighings)))
    sys.stdout.write("\n\n".join(output) + "\n")


if __name__ == "__main__":
    main()
