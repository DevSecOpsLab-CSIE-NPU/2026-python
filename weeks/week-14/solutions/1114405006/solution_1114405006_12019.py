# -*- coding: utf-8 -*-
"""
解題模組：UVA 12019 — Doom's Day Algorithm

題目重點：
- 題目已固定年份為 2012 年，所以我們不需要自己推導一般年份的
    Doomsday 規則，只要直接算出 2012 年某一天對應的星期幾即可。
- 輸入是一組一組的 (month, day)，第一個數字 T 表示測資數量。
- 每組測資輸出一行英文星期名稱，例如 Monday、Tuesday、Wednesday ...

功能：
- `weekday_2012(month, day)`：回傳 2012 年指定月日對應的星期幾。
- `main()`：從標準輸入讀取多組測資並輸出答案。

繁體中文說明：
本題固定只處理 2012 年，因此可以直接使用標準函式庫 `datetime`
計算日期對應的星期幾。這種寫法最簡潔，也最不容易出錯。

詳細做法：
1. 先用 `date(2012, month, day)` 建立日期物件，這一步會把年月日
     封裝成一個可運算的日期資料型態。
2. 再用 `strftime("%A")` 把日期轉成英文星期全名。
3. 將結果直接輸出即可，符合題目的格式要求。

時間複雜度：O(1)
空間複雜度：O(1)

補充：
- 由於 `datetime` 會自動處理日期與星期的計算，所以程式很短也很好記。
- 這種寫法很適合考試或現場手寫，因為邏輯清楚、容易驗證。
"""
import sys
from datetime import date


def weekday_2012(month: int, day: int) -> str:
    """回傳 2012 年指定日期的星期幾。

    參數：
    - month: 月份（1~12）
    - day: 日期

    回傳：
    - 星期名稱（英文全名）
    """
    # 2012 年固定，可直接交給標準函式庫計算星期幾。
    # 這裡不需要手動推算 Doomsday，只要建立日期物件後取出星期名稱即可。
    return date(2012, month, day).strftime("%A")


def main() -> None:
    """讀取多組月份與日期，並輸出對應星期幾。

    輸入格式：
    - 第一個整數 T 代表測資組數
    - 接下來每組有兩個整數 month 與 day

    輸出格式：
    - 每組測資輸出一行英文星期名稱
    """
    # 將整份輸入一次讀入，再用 split() 拆成 token。
    # 這樣可以同時支援多行、多個空白的輸入格式。
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # 第一個 token 是測資數量 T。
    t = int(data[0])
    idx = 1
    for _ in range(t):
        # 每次依序取出 month 與 day，並往後移動索引。
        month = int(data[idx])
        day = int(data[idx + 1])
        idx += 2
        # 直接印出該日期對應的星期幾。
        print(weekday_2012(month, day))


if __name__ == '__main__':
    main()
