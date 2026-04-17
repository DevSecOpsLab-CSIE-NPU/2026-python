# R2. 解包數量不固定：星號解包（1.2）
# =========================================================
# 星號表達式（Starred Expression）允許在解包時捕获剩餘的所有元素
# 適用於不知道序列有多少元素的情況
# 左側帶 * 的變數會成為一個列表，包含剩餘的元素
# =========================================================

# 實用範例：計算平均分數（拋棄第一個和最後一個成績）
# 使用星號解包：first 取得第一個，last 取得最後一個
# middle 會是列表，包含中間所有的成績
def drop_first_last(grades):
    first, *middle, last = grades
    # 計算中間分數的平均值
    return sum(middle) / len(middle)

# 電話號碼解包：記錄中前兩個是必填欄位，後面的電話號碼數量不固定
# 使用星號表達式將剩餘的元素都收集到 phone_numbers 列表
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name = 'Dave', email = 'dave@example.com'
# phone_numbers = ['773-555-1212', '847-555-1212']
name, email, *phone_numbers = record

# 也可以放在開頭或中間位置
# 收集前面的元素作為歷史記錄，最後一個是當前值
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# trailing = [10, 8, 7, 1, 9, 5, 10], current = 3
