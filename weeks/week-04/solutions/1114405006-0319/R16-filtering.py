# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 原始整數資料，包含正數與負數。
mylist = [1, 4, -5, 10]

# 方式 1：List 推導式（會立即建立完整清單）
# 只保留 n > 0 的元素，結果會是 [1, 4, 10]。
# 適合：資料量不大，且後續會重複使用結果。
[n for n in mylist if n > 0]

# 方式 2：Generator expression（惰性計算）
# pos 是一個生成器，只有在迭代時才會逐筆產生結果，
# 記憶體使用通常比直接建立清單更省。
# 適合：資料量大或只需要走訪一次結果。
pos = (n for n in mylist if n > 0)

# 字串資料：有些可以轉成整數，有些不行（例如 '-'、'N/A'）。
values = ['1', '2', '-3', '-', 'N/A']

# 自訂判斷函式：檢查字串是否可安全轉成 int。
# 回傳 True 代表可轉換；回傳 False 代表不可轉換。
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# 方式 3：filter(函式, 可迭代物件)
# filter 會保留使函式回傳 True 的元素。
# list(...) 用來把 filter 物件轉成實際清單。
# 結果會是 ['1', '2', '-3']。
print(list(filter(is_int, values)))
[n for n in values if is_int(n)]

# compress(data, selectors) 會依照 selectors 中對應位置的布林值
# 決定是否保留 data 的元素。
from itertools import compress

# 欲篩選的主資料。
addresses = ['a1', 'a2', 'a3']

# 對應的數值資料，常見情境是「地址對應筆數、權重或分數」。
counts = [0, 3, 10]

# 方式 4：先建立布林選擇器（條件為 > 5）
# counts 對應結果為 [False, False, True]。
more5 = [n > 5 for n in counts]

# 只有 selector 為 True 的資料會被保留，
# 因此結果會是 ['a3']。
print(list(compress(addresses, more5))
