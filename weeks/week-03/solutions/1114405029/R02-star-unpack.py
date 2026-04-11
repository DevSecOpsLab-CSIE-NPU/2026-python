# R2. 解包數量不固定：星號解包（1.2）

# ── 案例 1：計算扣除首尾後的平均值 ────────────────────
def drop_first_last(grades):
    """
    接收一個成績序列，移除最高與最低（或第一與最後一個），計算中間項的平均。
    """
    # *middle 會收集除了第一個 (first) 和最後一個 (last) 之外的所有元素
    # 無論中間有 1 個還是 100 個元素，都會被裝進一個名為 middle 的 list 中
    first, *middle, last = grades
    
    # 回傳中間部分的總和除以數量（平均值）
    return sum(middle) / len(middle)

# ── 案例 2：處理長度不定的欄位 ────────────────────────
# 假設一筆紀錄中，電話號碼的數量是不固定的（可能沒有，也可能很多個）
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

# 使用星號解包：
# name 匹配 'Dave'，email 匹配 'dave@example.com'
# *phone_numbers 會收集剩餘所有的字串內容
name, email, *phone_numbers = record
# 此時 phone_numbers 為 ['773-555-1212', '847-555-1212']

# ── 案例 3：獲取最後一個元素與其餘部分 ────────────────
# 星號變數不一定要放在中間，也可以放在開頭
# 這會將最後一個元素分配給 current，其餘前面的所有元素收集進 trailing 列表
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# 此時 trailing 為 [10, 8, 7, 1, 9, 5, 10]，current 為 3