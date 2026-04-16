"""R2. 解包數量不固定：星號解包（Star Unpacking）

星號解包的用途：
1. 當你不知道中間有多少元素時，可以用 * 來接收剩下的值。
2. 常見於資料前後固定、中間長度不固定的情境。
3. 也可以用在前面或後面，視需求收集剩餘元素。
"""

def drop_first_last(grades):
    """丟掉第一個和最後一個成績，只計算中間部分的平均。"""
    # first 接第一個，last 接最後一個，中間全部交給 middle
    first, *middle, last = grades
    # middle 會是一個 list，即使原本 grades 是 tuple 也一樣
    return sum(middle) / len(middle)

# record 中前兩個欄位是固定的，後面可能有多個電話號碼
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

# name 接姓名，email 接電子郵件，剩下的電話號碼全部交給 phone_numbers
name, email, *phone_numbers = record

# 星號也可以放在前面，表示把前面的資料全部收集起來
# trailing 會得到前 7 個元素，current 會得到最後一個元素 3
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
