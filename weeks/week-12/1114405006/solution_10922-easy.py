"""
UVA 10922 — 2 the 9s 簡易版（含繁體中文詳細註解）

問題核心：計算一個數字的 "9-degree"。
- 如果數字不是 9 的倍數，則輸出 "is not a multiple of 9."
- 若是 9 的倍數，則不斷將數字的各位相加，直到變成 9，
  這個序列的長度（包含原數）就是 9-degree。

這個簡易版強調記憶口訣：
1. 先檢查各位數字總和是否為 9 的倍數（若不是，直接結束）。
2. 若是 9 的倍數，則重複把各位數字加總，直到得到 9 為止，
   每做一次加總就把計數器 +1。
3. 特殊情況：輸入為 '9' 時，9-degree 為 1（原數就是 9）。

實作上使用純字串處理（不會轉為大整數做運算），適合處理很長的數字字串。
"""


def digit_sum(text: str) -> int:
    """計算字串中所有數字字元的數值總和。

    範例：
    >>> digit_sum('123')
    6
    """
    return sum(int(ch) for ch in text)


def nine_degree_easy(num_str: str):
    """計算輸入字串表示數字的 9-degree。

    參數：
    - num_str: 字串形式的非負整數（例如 '123', '009', '0'）

    回傳：
    - 若輸入不是 9 的倍數，回傳 None
    - 若是 9 的倍數，回傳正整數表示其 9-degree

    實作要點（步驟）：
    1. 去除前導零（前導零不影響是否為 9 的倍數）
    2. 若字串為 '9'，直接回傳 1（原數就是 9）
    3. 計算各位數字總和，若不是 9 的倍數回傳 None
    4. 否則進入迴圈：反覆用 digit_sum 將目前的數值字串化並求和，
       直到 total == 9 為止，同時計數每次的轉換次數（包含原始數），
       最後回傳該序列長度。
    """
    # 移除前導零，確保 '0' 仍會保留為 '0'
    num_str = num_str.lstrip('0') or '0'

    # 如果輸入正好是 '9'，那麼 9-degree 就是 1
    if num_str == '9':
        return 1

    # 第一步：先判斷整數各位和是否為 9 的倍數
    total = digit_sum(num_str)
    if total % 9 != 0:
        # 不是 9 的倍數，題目要求輸出 'is not a multiple of 9.'
        return None

    # 若是 9 的倍數，重複做各位和直到變成 9
    # 我們用 degree 追蹤「已進行了幾次合併」；
    # 注意：原數字也算在序列中，題目範例把原數算作第一個元素
    degree = 1

    # total 現在是第一次各位和的結果（也可能已經是 9）
    while True:
        if total == 9:
            # 當 total 等於 9，序列結束，回傳包含原數的長度
            return degree + 1
        # 若 total 小於 10（但不是 9），表示無法再繼續合法縮減
        # 此情況理論上對於能被 9 整除的數字不會發生，但為保險起見仍檢查
        if total < 10:
            return None
        # 否則，把 total 轉為字串後再計算各位和，degree 加一
        total = digit_sum(str(total))
        degree += 1


def parse_and_run():
    """從標準輸入讀取多行數字字串，遇到 '0' 終止，並輸出題目要求的格式。"""
    import sys

    out = []
    for line in sys.stdin:
        n = line.strip()
        if not n:
            continue
        if n == '0':
            break

        degree = nine_degree_easy(n)
        if degree is None:
            out.append(f"{n} is not a multiple of 9.")
        else:
            out.append(f"9-degree of {n} is {degree}.")

    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    parse_and_run()
