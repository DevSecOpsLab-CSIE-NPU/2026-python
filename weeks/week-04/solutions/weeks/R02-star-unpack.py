# R2. 解包數量不固定：星號解包（1.2）

def drop_first_last(grades):
    # 使用星號解包：first 取得第一個元素，last 取得最後一個元素
    # *middle 會接收中間所有剩餘的元素，形成一個列表
    first, *middle, last = grades
    # 回傳中間成績的平均值
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name 取得第一個元素，email 取得第二個
# *phone_numbers 會接收後面所有電話號碼，形成列表
name, email, *phone_numbers = record

# *trailing 接收前面所有元素，current 取得最後一個元素
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]