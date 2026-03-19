# R2. 解包數量不固定：星號解包（1.2）
# 星號解包（Star Unpacking）允許我們在解包序列時，
# 使用星號 * 來收集剩餘的元素到一個列表中。
# 這對於處理長度不固定的序列非常有用。

# 定義一個函數來計算成績的平均值，但排除最高分和最低分
# 參數 grades 是一個包含成績的序列
def drop_first_last(grades):
    # 使用星號解包：first 獲取第一個元素，
    # *middle 收集中間的所有元素到一個列表，
    # last 獲取最後一個元素
    first, *middle, last = grades
    # 返回中間成績的平均值
    return sum(middle) / len(middle)

# 創建一個包含個人資訊的元組：姓名、電子郵件、多個電話號碼
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

# 解包記錄：name 獲取姓名，email 獲取電子郵件，
# *phone_numbers 收集所有剩餘的電話號碼到一個列表中
name, email, *phone_numbers = record

# 創建一個包含數值的列表
# 使用星號解包：*trailing 收集除了最後一個元素外的所有元素到列表，
# current 獲取最後一個元素
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
