# R12. Counter 統計 + most_common（1.12）

# 從 collections 模組導入 Counter 類別，它是一個字典的子類別，專門用來計算可雜湊 (hashable) 物件的數量。
from collections import Counter

print("--- 建立 Counter 物件 ---")
# 定義一個字串列表 words，包含多個單字，其中 'look' 出現了兩次。
words = ['look', 'into', 'my', 'eyes', 'look']
# 顯示原始的字串列表。
print(f"原始單字列表 words: {words}")

# 使用 Counter 將列表轉換為計數器字典，它會自動計算每個元素出現的次數。
word_counts = Counter(words)
# 顯示建立後的 Counter 物件內容。可以看到 'look' 的計數為 2，其他為 1。
print(f"Counter 統計結果 word_counts: {word_counts}\n")

print("--- 使用 most_common() 找出最常出現的元素 ---")
# 使用 most_common(n) 方法找出出現次數最多的前 n 個元素。
# 它會回傳一個包含 (元素, 計數) 元組的列表，並依照計數由大到小排序。
top_3_words = word_counts.most_common(3)
# 顯示最常出現的前 3 個單字及其計數。
print(f"出現次數最多的前 3 個單字 (most_common(3)): {top_3_words}\n")

print("--- 使用 update() 更新計數 ---")
# 使用 update() 方法可以增加現有元素的計數，或者加入新的元素並計算次數。
# 這裡我們傳入一個包含兩個 'eyes' 的列表，這會讓 'eyes' 的計數增加 2。
print("準備將 ['eyes', 'eyes'] 加入 Counter 中進行更新...")
word_counts.update(['eyes', 'eyes'])
# 顯示更新後的 Counter 物件內容。可以看到 'eyes' 的計數從 1 變成了 3。
print(f"更新後的 Counter 統計結果 word_counts: {word_counts}")
