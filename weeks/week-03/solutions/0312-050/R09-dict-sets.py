# R9. 兩字典相同點：keys/items 集合運算（1.9）

# 定義兩個字典 a 和 b。
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
# 顯示原始字典 a 和 b 的內容。
print(f"字典 a: {a}")
print(f"字典 b: {b}\n")

print("--- 進行 keys (鍵) 的集合運算 ---")
# 使用 & 運算符找出兩個字典 keys 的交集 (存在於 a 也存在於 b 的鍵)。
common_keys = a.keys() & b.keys()
print(f"a 和 b 共同的鍵 (a.keys() & b.keys()): {common_keys}")

# 使用 - 運算符找出在 a 但不在 b 的 keys 的差集 (只存在於 a 的鍵)。
diff_keys = a.keys() - b.keys()
print(f"只存在於 a 的鍵 (a.keys() - b.keys()): {diff_keys}\n")

print("--- 進行 items (鍵值對) 的集合運算 ---")
# 使用 & 運算符找出兩個字典 items 的交集 (鍵與值都完全相同的項目)。
# a 的 'y':2 和 b 的 'y':2 完全相同。
common_items = a.items() & b.items()
print(f"a 和 b 完全相同的鍵值對 (a.items() & b.items()): {common_items}\n")

print("--- 利用集合運算過濾字典 ---")
# 建立一個新字典 c。
# a.keys() - {'z', 'w'} 是一個差集運算，會先過濾掉 'z' 和 'w' 鍵，留下要保留的鍵集合。
# 接著利用字典推導式 (dictionary comprehension) 走訪保留的鍵，並取回字典 a 中的對應值組合起來。
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print(f"過濾掉鍵 'z' 和 'w' 後的新字典 c: {c}")
