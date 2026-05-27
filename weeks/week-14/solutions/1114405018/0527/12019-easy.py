"""UVA 12019 - Doom's Day Algorithm (easy version).

說明（繁體中文註解）：

本題限定在 2012 年，因此最簡單且直觀的做法是直接使用 Python 的日期模組 `datetime`。
流程如下：
- 從 stdin 讀取整數資料，第一個數字為測資數量 T，接著每筆測資是一組 m d（月份與日期）。
- 對於每組 m, d，建立 `date(2012, m, d)` 物件，呼叫 `.weekday()` 取得星期索引（0=Monday, ... ,6=Sunday）。
- 把索引轉成英文星期名稱並輸出，每筆測資獨立一行。

使用 `datetime` 的好處是處理閏年與每月日數都交給標準函式庫處理，不需自己手動推算 Doomsday。
"""

from __future__ import annotations

from datetime import date
import sys


WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        m = int(data[idx]); d = int(data[idx+1]); idx += 2
        wd = date(2012, m, d).weekday()
        out.append(WEEKDAYS[wd])

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
