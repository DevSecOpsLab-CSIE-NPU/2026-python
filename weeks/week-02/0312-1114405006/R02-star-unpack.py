# R2. 解包數量不固定：星號解包（1.2）
#
# 星號 * 可以用來接住「剩下全部的元素」：
# 1. 前後固定，中間數量不確定時很實用。
# 2. 被 * 接住的結果會是 list。
# 3. 可用在函式內，也可直接用在一般指派語句。

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
