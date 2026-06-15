# 【Bloom 階段：R - 記憶與基本操作】
# 5 索引與切片範例
# August 的惡意提醒：切片（Slicing）是 CPE 解題的利器。
# 記住 [start:stop:step] 語法，尤其是負數索引的使用。

text = 'abcdefg'
first = text[0]    # 取得第一個字元
mid = text[2:5]    # 取得索引 2 到 4 的字元（不含 5）

nums = [10, 20, 30, 40, 50]
# 取得最後兩個元素（常用的「尾部採樣」）
last_two = nums[-2:]

print(f"Mid: {mid}, Last Two: {last_two}")
# 老師私藏技：反轉字串的寫法
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")
