# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 星號（*）解包是 Python 處理「數量不確定」資料的強大機制。
# 它會自動捕捉「不符合左側其他變數」的所有剩餘元素。

# 範例資料：tuple 只有 2 個元素。
record = ('Dave', 'dave@example.com')

# 星號解包：
# - name 接收第一個元素 'Dave'
# - email 接收第二個元素 'dave@example.com'
# - *phones 接收「剩餘的所有元素」
#
# 此例中沒有剩餘元素，所以 phones 是空列表 []。
# 注意：即使沒有元素可捕捉，phones 仍然是 list 型態！
name, email, *phones = record

# phones 此時為 []（空列表，不是空 tuple）
# 這遵循星號解包的一致規則：*變數 永遠產生 list。
# phones == []  仍是 list
print(name, email, phones)

# 為什麼結果一定是 list？
# - 因為 Python 需要統一的型態回傳，list 提供動態長度的彈性
# - 若資料中有 3 個以上的元素，phones 就會包含 [第3元素, 第4元素, ...]
#
# 進階例子（說明用）：
# record2 = ('Alice', 'alice@ex.com', '555-1234', '555-5678')
# name2, email2, *phones2 = record2
# # 此時 phones2 會是 ['555-1234', '555-5678']
#
# 星號解包也可用在列表動作中：
# first, *middle, last = [1, 2, 3, 4, 5]
# # first = 1, middle = [2, 3, 4], last = 5
