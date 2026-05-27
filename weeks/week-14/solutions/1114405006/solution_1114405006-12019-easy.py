# -*- coding: utf-8 -*-
"""
簡易版（-easy）：UVA 12019 — Doom's Day Algorithm

這份版本的目標是「好記、好寫、好檢查」，適合現場手寫或快速重建。

題目重點：
- 題目已經固定年份為 2012，因此不需要真的實作完整的 Doomsday
    演算法，也不用自己計算閏年規則或每月基準日。
- 只要把輸入的年月日轉成 2012 年的日期物件，再查出它對應的星期幾即可。

為什麼用 `date.weekday()`：
- `strftime("%A")` 會受系統語系影響，在某些環境下可能不是英文全名。
- `date.weekday()` 則固定回傳 0~6 的星期索引，因此我們可以自己準備
    英文星期對照表，避免輸出格式出現不一致。

這份簡單版的優點：
- 程式碼短，邏輯直接。
- 不需要背 doomsday 公式，只要知道 2012 年的日期即可。
- 方便在考場快速打出來，也容易用單元測試驗證。

時間複雜度：O(1)
空間複雜度：O(1)
"""
import sys
from datetime import date


# Python 的 `weekday()` 回傳值規則：Monday = 0, Tuesday = 1, ..., Sunday = 6
# 這張表就是把索引對應回題目要輸出的英文星期全名。
WEEKDAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday_2012_easy(month: int, day: int) -> str:
    """回傳 2012 年指定日期的星期幾。

    這個函式是整份程式最核心的部分：
    1. 先建立 2012 年的日期物件；
    2. 用 `weekday()` 取得星期索引；
    3. 再用 `WEEKDAY_NAMES` 轉回英文星期名稱。

    參數：
    - month: 月份（1~12）
    - day: 日期

    回傳：
    - 英文星期名稱，例如 Monday、Tuesday、Wednesday
    """
    # 先把輸入的月份與日期包成 2012 年的日期物件。
    # 如果日期不合法，`date(...)` 會直接丟出錯誤，這也能幫我們檢查資料。
    current_date = date(2012, month, day)

    # `weekday()` 會回傳 0~6 的星期索引，依序對應 Monday 到 Sunday。
    # 再把索引拿去查表，就能得到題目要求的英文星期全名。
    return WEEKDAY_NAMES[current_date.weekday()]


def main() -> None:
    """從標準輸入讀取多組測資，並輸出每組對應的星期幾。

    輸入格式：
    - 第一個整數 T，代表測資組數
    - 接著每組有兩個整數 month 與 day

    輸出格式：
    - 每組測資輸出一行英文星期名稱
    """
    # 一次讀入全部輸入，再用 split() 分割成 token。
    # 這種寫法很適合競賽題，因為可以簡化多行輸入的處理。
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # 第一個 token 是測資數量 T。
    t = int(data[0])
    index = 1

    for _ in range(t):
        # 依照順序取出 month 與 day。
        # 題目保證輸入格式正確，因此這裡直接轉成整數即可。
        month = int(data[index])
        day = int(data[index + 1])
        index += 2

        # 每組測資輸出一行，符合題目要求。
        print(weekday_2012_easy(month, day))


if __name__ == '__main__':
    main()
