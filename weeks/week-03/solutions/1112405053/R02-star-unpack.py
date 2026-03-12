# R2. 解包數量不固定：星號解包（1.2）

def drop_first_last(grades):
    # 取出第一個與最後一個，剩下的全部放到 middle
    first, *middle, last = grades
    # 計算中間成績平均
    return sum(middle) / len(middle)

# 星號可接收不固定數量的電話號碼
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# 也可把最後一個值單獨取出，前面全部收進 trailing
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
