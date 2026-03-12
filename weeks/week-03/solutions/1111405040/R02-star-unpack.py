"""
R02: 星號拆封（Star Unpacking）

這個範例示範使用 * 接住「可變長度」的中間區段。
常見於資料筆數不固定，但前後欄位固定的情境。
"""


def drop_first_last(grades):
    """移除首尾分數後，回傳中間分數的平均值。"""
    # first 與 last 各接一個元素；middle 會接住剩餘所有元素（型別為 list）。
    first, *middle, last = grades
    return sum(middle) / len(middle)


# 前兩個欄位固定是姓名與 email，其餘電話數量不固定，全部交給 phone_numbers。
record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
name, email, *phone_numbers = record

# 反向用法：保留最後一個元素 current，前面全部由 trailing 接住。
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
