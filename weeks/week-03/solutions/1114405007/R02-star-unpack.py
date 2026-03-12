# R2: 星號解包（Star Unpacking）
# 觀念：使用 * 讓某一個變數接收「不定長度」的中間或前段資料。


def drop_first_last(grades):
    # first 取第一個成績、last 取最後一個成績、middle 收集中間所有成績（list）
    first, *middle, last = grades
    # 題意通常是去頭去尾後取平均
    return sum(middle) / len(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 前兩個欄位固定，剩下所有電話交給 phone_numbers
name, email, *phone_numbers = record

# 也可以把最後一個元素單獨拿出來，其餘收集在前面
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
