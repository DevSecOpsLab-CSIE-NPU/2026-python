# R2. 解包數量不固定：星號解包（1.2）

def drop_first_last(grades):
    # first 與 last 取首尾；中間其餘元素全部收進 middle
    first, *middle, last = grades
    # 只計算中間成績的平均
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 前兩欄固定解包，其餘電話號碼由 phone_numbers 接收
name, email, *phone_numbers = record

# 星號也可以放在前面，接住前面所有元素
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
