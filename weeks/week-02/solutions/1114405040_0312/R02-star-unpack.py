# R2. 解包數量不固定：星號解包（Star Unpacking）—— Python Cookbook 1.2

# ── 函式中的星號解包 ──────────────────────────────────────
# *middle 會把「夾在 first 和 last 之間的所有元素」打包成 list
# 用途：計算去頭去尾後的平均（例如：比賽去掉最高/最低分）
def drop_first_last(grades):
    first, *middle, last = grades   # first = 最低分, last = 最高分
    return sum(middle) / len(middle)

# ── 元素數量不確定時的解包 ────────────────────────────────
# record 有 4 個欄位，但電話號碼數量未知
# *phone_numbers 把剩餘所有電話號碼打包成 list（可能 0 個或多個）
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
# name = 'Dave'
# email = 'dave@example.com'
# phone_numbers = ['773-555-1212', '847-555-1212']

# ── 星號放前面：取「最後一個」＋「前面全部」 ───────────────
# *trailing 接收除最後一個以外的所有元素
# 常見情境：取最新一筆資料（current），其餘為歷史（trailing）
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# trailing = [10, 8, 7, 1, 9, 5, 10]
# current  = 3
