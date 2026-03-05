# 8 容器操作與推導式範例
# 推導式是 Python 最重要的語法糖，能讓代碼更簡潔、可讀性強、效能更好

nums = [1, -2, 3, -4]

# List Comprehension (列表推導式)
# 為什麼用推導式？
# 1. 比迴圈更簡潔：[n for n in nums if n > 0] vs for 迴圈
# 2. 更快：使用 C 層級的優化，比 append() 迴圈快
# 3. 易於閱讀：一行代碼表達完整的篩選邏輯
positives = [n for n in nums if n > 0]  # 結果：[1, 3]

pairs = [('a', 1), ('b', 2)]

# Dict Comprehension (字典推導式)
# 為什麼用推導式？
# 1. 快速轉換資料結構（tuple list → dict）
# 2. 節省寫迴圈的時間
# 3. 在資料轉換中常用（後續會頻繁使用）
lookup = {k: v for k, v in pairs}  # 結果：{'a': 1, 'b': 2}

# 生成器表達式 (Generator Expression)
# 為什麼用生成器而不是 List Comprehension？
# 1. 節省記憶體：不一次性建立整個列表
# 2. 適合大資料：如果你只需要計算，不需要保存所有值
# 3. 效能更好：sum() 接收生成器，邊走邊算
squares_sum = sum(n * n for n in nums)  # 結果：30 (1*1 + 2*2 + 3*3 + 4*4)
