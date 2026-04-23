# 【Bloom 階段：R - 記憶與基本操作】
# R9. 尋找兩個字典的共通點
# August 的惡意提醒：字典的 .keys() 與 .items() 支持集合運算 (&, -, |)。
# 識破這點，你在處理資料差異比對（如 Week 09 的編碼差異）時，效能會從 O(N^2) 降到 O(N)。

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 找出共通的鍵 (Common Keys)
common_keys = a.keys() & b.keys()

# 找出 a 裡面有但 b 沒有的鍵 (Keys in a but not b)
diff_keys = a.keys() - b.keys()

# 找出完全相同的鍵值對 (Common Items)
common_items = a.items() & b.items()

# 字典推導式：快速過濾字典
c = {k: a[k] for k in a.keys() - {'z', 'w'}}

print(f"Common Keys: {common_keys}")
print(f"Common Items: {common_items}")
