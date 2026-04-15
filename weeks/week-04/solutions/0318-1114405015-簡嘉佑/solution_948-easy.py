"""
UVA 948 - 假幣偵測（easy 版）

簡單記法：
  對每枚硬幣，分別嘗試「它是假幣且偏輕」或「它是假幣且偏重」。
  只要某種假設與所有秤重結果都吻合，就加入候選。
  最後只剩一個候選 → 輸出；否則輸出 0。

逐筆驗證的規則（三種結果）：
  - 結果 "=" : 假幣不能在任何一側盤子裡。
  - 結果 "<" : 假幣若在左側必須偏輕；若在右側必須偏重；
               若完全不在兩側則矛盾（兩邊應等重）。
  - 結果 ">" : 假幣若在左側必須偏重；若在右側必須偏輕；
               若完全不在兩側則矛盾。
"""

from __future__ import annotations

import sys


def is_ok(coin: int, heavy: bool,
          weighings: list[tuple[list[int], list[int], str]]) -> bool:
    """
    檢查「假設 coin 是假幣，heavy 決定偏重或偏輕」是否與所有秤重結果一致。

    :param coin:      假幣候選的硬幣編號（1-based）
    :param heavy:     True = 偏重；False = 偏輕
    :param weighings: [(左側列表, 右側列表, 結果字元)] 的清單
    :return:          全部一致則 True
    """
    for left, right, res in weighings:
        # 判斷假幣位置
        in_left  = coin in left
        in_right = coin in right

        # 依結果逐一比對
        if res == "=":
            # 等重 → 假幣不可在任何一側
            if in_left or in_right:
                return False
        elif res == "<":
            # 左輕右重
            if not in_left and not in_right:
                return False          # 假幣不在兩側，兩邊應等重，矛盾
            if in_left and heavy:
                return False          # 假幣偏重在左，左應該重，矛盾
            if in_right and not heavy:
                return False          # 假幣偏輕在右，右應該輕，矛盾
        else:  # ">"
            # 左重右輕
            if not in_left and not in_right:
                return False
            if in_left and not heavy:
                return False          # 假幣偏輕在左，左應該輕，矛盾
            if in_right and heavy:
                return False          # 假幣偏重在右，右應該重，矛盾

    return True


def solve(n: int,
          weighings: list[tuple[list[int], list[int], str]]) -> int:
    """
    回傳假幣編號；無法唯一確定則回傳 0。

    :param n:         硬幣總數
    :param weighings: 秤重紀錄清單
    """
    # 收集所有通過驗證的候選硬幣
    candidates = []
    for coin in range(1, n + 1):
        # 只要偏輕或偏重其中一種假設成立，就把它加進候選
        if is_ok(coin, True, weighings) or is_ok(coin, False, weighings):
            candidates.append(coin)

    # 唯一候選才有答案
    return candidates[0] if len(candidates) == 1 else 0


def main() -> None:
    """讀取標準輸入並輸出每組測試的結果。"""
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    idx = 0

    m = int(lines[idx]); idx += 1
    out = []

    for _ in range(m):
        n, k = map(int, lines[idx].split()); idx += 1
        weighings = []
        for _ in range(k):
            parts = lines[idx].split(); idx += 1
            p = int(parts[0])
            left  = list(map(int, parts[1: p + 1]))
            right = list(map(int, parts[p + 1: 2 * p + 1]))
            res   = lines[idx]; idx += 1
            weighings.append((left, right, res))
        out.append(str(solve(n, weighings)))

    sys.stdout.write("\n\n".join(out) + "\n")


if __name__ == "__main__":
    main()
