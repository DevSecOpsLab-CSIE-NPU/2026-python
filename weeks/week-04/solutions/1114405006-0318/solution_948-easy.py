"""UVA 948 假幣問題（簡單好記版）。

這份程式刻意用「容易記憶」的寫法：
1. 先把題目輸入拆成 token（自動忽略空白行）。
2. 對每一顆硬幣做兩種假設：它比較重、或它比較輕。
3. 把每一次秤重都模擬一次，比對是否和題目紀錄一致。
4. 若最後只有一顆硬幣還有可能是假幣，就輸出它；否則輸出 0。
"""

from __future__ import annotations

import sys


# 好記口訣：
# 1) 枚舉每顆硬幣 i
# 2) 假設 i 較重（+1）或較輕（-1）
# 3) 每筆秤重都能對上結果才算可能
# 4) 最後只剩一顆就輸出它，不是唯一就輸出 0


def sign_to_char(x: int) -> str:
    """
    把數值差轉成題目秤重符號。

    x < 0 代表左邊比較輕，回傳 "<"。
    x > 0 代表左邊比較重，回傳 ">"。
    x = 0 代表一樣重，回傳 "="。
    """
    if x < 0:
        return "<"
    if x > 0:
        return ">"
    return "="


def check_one_assumption(coin: int, heavy_or_light: int, records: list[tuple[list[int], list[int], str]]) -> bool:
    """
    檢查某顆硬幣在某個假設（重或輕）下，是否符合所有秤重紀錄。

    參數說明：
    coin:
        目前正在驗證的硬幣編號。
    heavy_or_light:
        +1 表示「假設這顆硬幣比較重」。
        -1 表示「假設這顆硬幣比較輕」。
    records:
        每筆秤重資料，格式為 (left, right, result)
        left / right 是硬幣編號清單，result 是 < > = 其中之一。

    核心觀念：
    - 若 coin 在 left，則左邊重量要加上 heavy_or_light。
    - 若 coin 在 right，則右邊重量相對變重，因此 diff 要扣 heavy_or_light。
    - 最後用 sign_to_char(diff) 和題目結果比對。
      只要有一筆對不上，該假設立刻失敗。
    """
    for left, right, result in records:
        # diff 代表「左盤相對右盤」的重量差。
        # 這裡只在意正負與是否為 0，不需要真實重量值。
        diff = 0

        # 假幣在左盤：左盤相對變重（或變輕）。
        if coin in left:
            diff += heavy_or_light

        # 假幣在右盤：右盤相對變重（或變輕），
        # 轉成左-右差值時就是相反方向，因此用減法。
        if coin in right:
            diff -= heavy_or_light

        # 只要任何一筆秤重結果不一致，這顆硬幣在此假設下就不可能。
        if sign_to_char(diff) != result:
            return False

    # 全部秤重都一致，代表此假設成立。
    return True


def find_fake_coin(n: int, records: list[tuple[list[int], list[int], str]]) -> int:
    """
    找唯一假幣；無法唯一判定就回傳 0。

    這裡做的是「完整枚舉」：
    - coin 從 1 到 n 每顆都試。
    - 每顆 coin 都試兩個方向（重 / 輕）。
    - 只要其中一個方向能通過全部紀錄，就把 coin 放進 possible。

    possible 代表「仍有可能是假幣」的候選清單。
    最後如果候選數量剛好是 1，才能唯一確定答案。
    """
    possible = []

    for coin in range(1, n + 1):
        can_be_heavy = check_one_assumption(coin, 1, records)
        can_be_light = check_one_assumption(coin, -1, records)

        # 這顆硬幣只要有一種狀態成立，就先保留在候選名單。
        if can_be_heavy or can_be_light:
            possible.append(coin)

    # 題目要求：只有唯一答案才輸出該編號，否則輸出 0。
    if len(possible) == 1:
        return possible[0]
    return 0


def solve(data: str) -> str:
    """
    讀入整份輸入字串並回傳完整輸出字串。

    解析技巧：
    - 使用 split() 把所有空白（包含換行與空白列）都當成分隔。
    - 用指標 p 依序往後讀，不需要特別處理空行。

    輸出格式：
    - 每組測資輸出一行答案。
    - 組與組之間要有一個空白行，因此用 "\n\n" 連接。
    """
    tok = data.split()
    p = 0

    # t: 測資組數
    t = int(tok[p])
    p += 1

    answers = []

    for _ in range(t):
        # n: 硬幣數量，k: 秤重次數
        n = int(tok[p])
        k = int(tok[p + 1])
        p += 2

        records = []
        for _ in range(k):
            # cnt: 這次秤重每邊各放幾顆硬幣
            cnt = int(tok[p])
            p += 1

            # 依序切出左盤與右盤的硬幣清單
            left = list(map(int, tok[p : p + cnt]))
            p += cnt
            right = list(map(int, tok[p : p + cnt]))
            p += cnt

            # 本次秤重結果（<、>、=）
            result = tok[p]
            p += 1

            records.append((left, right, result))

        answers.append(str(find_fake_coin(n, records)))

    return "\n\n".join(answers) + "\n"


def main() -> None:
    # CPE / UVA 標準模式：從 stdin 讀完整輸入，輸出到 stdout。
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()
