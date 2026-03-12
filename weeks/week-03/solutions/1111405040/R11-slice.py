"""
R11: slice 物件

把固定欄位位置包成 slice，讓字串欄位切割更可讀、可重用。
"""

record = "....................100 .......513.25 .........."

# 欄位索引集中定義，避免在程式中散落魔術數字。
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 先用 slice 取出字串欄位，再轉成數值計算總成本。
cost = int(record[SHARES]) * float(record[PRICE])
