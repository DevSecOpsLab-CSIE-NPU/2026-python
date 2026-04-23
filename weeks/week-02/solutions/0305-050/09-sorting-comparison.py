# 9 比較、排序與 key 函式範例 (Comparisons, Sorting, and Key Functions Examples)

# --- 比較運算 (Tuple 逐一比較) ---
# 在 Python 中，元組 (Tuple) 或串列 (List) 等序列型別的比較是「逐項 (element-by-element)」進行的。
# 它會先比較第一個元素，如果相等分不出大小，就會繼續比較第二個元素，依此類推。
# 定義兩個元組 a 和 b
a = (1, 2)
b = (1, 3)
# 這裡比較 a 和 b 的大小：
# 1. 先比較第一項：a 的 1 和 b 的 1 相等，無法決定結果。
# 2. 接著比較第二項：a 的 2 小於 b 的 3，因此整個 a < b 的結果判定為 True。
# 這種特性在多重排序 (例如先排分數，再排名字) 時非常有用。
result = a < b

# --- key 排序 ---
# 定義一個包含多個字典的串列 rows。每個字典代表一筆獨立的資料，裡面有一個 'uid' 鍵。
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]

# 使用內建函式 sorted() 來對串列進行排序。
# 預設情況下，Python 不知道如何直接比較兩個字典大小 (會拋出 TypeError)。
# 為了讓它知道怎麼排，我們加入 `key=lambda r: r['uid']` 參數：
# 這個 lambda (匿名函式) 告訴 sorted()：「對於串列中的每一個元素 (在這裡稱作 r)，請抽出 r['uid'] 的值，並用這個整數值來進行排序比較」。
# 執行結果 rows_sorted 將會產生新串列：[{'uid': 1}, {'uid': 2}, {'uid': 3}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# --- min/max 搭配 key ---
# min() 與 max() 函式的機制與 sorted() 中的 key 非常相似。
# 這裡使用相同的 key 參數，告訴 min()：「請幫我找出 'uid' 數值最小的那一筆資料」。
# 它會遍歷比較所有的 'uid'，最後回傳找到的「整個原始字典物件」，而不僅僅是數字而已。
# 執行結果 smallest 將會是：{'uid': 1}
smallest = min(rows, key=lambda r: r['uid'])
