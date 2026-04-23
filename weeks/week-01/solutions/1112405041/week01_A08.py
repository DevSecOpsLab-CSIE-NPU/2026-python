# 【Bloom 階段：U - 理解與進階應用】
# 8 容器操作與推導式範例
# August 的惡意提醒：推導式 (Comprehensions) 是區分「新生」與「資工系大神」的代碼指紋。
# 學會使用生成器表達式 (n * n for n in nums)，能大幅減少內存佔用。

nums = [1, -2, 3, -4]
# 列表推導式 (List Comprehension)：過濾與轉換一次完成
positives = [n for n in nums if n > 0]

# 字典推導式 (Dict Comprehension)：將 Tuple 清單快速轉為查詢表
pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}

# 生成器表達式 (Generator Expression)
# 與列表推導式的差別：用圓括號，不會立即產生完整清單，而是惰性運算
# 對應主題 10 的 Big-O 優化，這對大數據處理非常重要
squares_sum = sum(n * n for n in nums)

print(f"Positives: {positives}")
print(f"Lookup: {lookup['a']}")
print(f"Squares Sum: {squares_sum}")
