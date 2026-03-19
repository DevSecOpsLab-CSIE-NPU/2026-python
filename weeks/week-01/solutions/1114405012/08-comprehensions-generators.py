# 8 容器操作與推導式範例

# 原始數列，同時包含正數與負數
nums = [1, -2, 3, -4]
# 串列推導式：只保留大於 0 的元素
positives = [n for n in nums if n > 0]

# 鍵值配對（tuple）清單
pairs = [('a', 1), ('b', 2)]
# 字典推導式：把配對清單轉成 dict
lookup = {k: v for k, v in pairs}

# 生成器表達式：逐一產生平方值並交給 sum 加總
# 優點是不用先建立整個中間串列
squares_sum = sum(n * n for n in nums)
