# 【Bloom 階段：R - 記憶與基本操作】
# R2. 星號解包 (Star Unpacking)
# August 的惡意提醒：這是處理「不定長度輸入」的核武器。
# 在 Week 04 解析具有變動參數的指令時，如果不准用 if/else 判斷長度，這招就是救命恩人。

def drop_first_last(grades):
    """示範：去除頭尾，計算中間成績的平均"""
    # *middle 會抓取除了 first 和 last 之外的所有元素到一個列表中
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 抓取前兩項，其餘所有號碼存入 phone_numbers 列表
name, email, *phone_numbers = record

# 也可以抓取末尾
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

print(f"Phones: {phone_numbers}")
print(f"Current: {current}")
