# R2. 解包數量不固定：星號解包（1.2）
# 使用 * 可捕捉任意長度的子序列。

def drop_first_last(grades):
    first, *middle, last = grades
    print("first", first, "middle", middle, "last", last)
    return sum(middle) / len(middle)

print("平均成績(忽略頭尾):", drop_first_last([10, 5, 7, 9, 8]))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print("name", name, "email", email, "phones", phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing", trailing, "current", current)

