# R11. 命名切片 slice（1.11）
#
# 這份程式示範「固定欄寬字串（fixed-width text）」的欄位擷取。
# 重點是用 slice 物件先把位置命名，避免程式到處寫神祕數字。

# 一筆固定格式的文字紀錄：
# - 某段位置放股數（shares）
# - 另一段位置放單價（price）
record = '....................100 .......513.25 ..........'

# slice(start, stop)
# - start 含在內
# - stop 不含在內
#
# 這裡命名欄位範圍：
# SHARES 對應索引 [20:23]
# PRICE  對應索引 [31:37]
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 用命名切片取出欄位後轉型計算：
# int(record[SHARES])   -> 100
# float(record[PRICE])  -> 513.25
# cost = 股數 * 單價
cost = int(record[SHARES]) * float(record[PRICE])


# 讀懂這份程式的步驟：
# 1. 先把 record 想成「固定欄位報表」的一行資料。
# 2. 確認每個欄位在字串中的位置（start/stop）。
# 3. 用 slice 命名欄位，讓 record[SHARES] 比 record[20:23] 更可讀。
# 4. 擷取後依欄位型別轉換（int/float）再運算。
