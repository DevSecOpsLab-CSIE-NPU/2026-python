# 【Bloom 階段：R - 記憶與基本操作】
# R11. 命名切片 (Naming a Slice)
# August 的惡意提醒：在 Week 03 處理固定格式的日誌文件時，
# 不要直接在代碼裡寫 s[20:23]，那是魔術數字，會被助教在 Code Style 扣分。
# 使用 slice() 物件能賦予代碼生命力與可維護性。

record = '....................100 .......513.25 ..........'
# 命名切片：清楚定義「這段區間代表什麼」
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 使用切片物件讀取，邏輯清晰可見
cost = int(record[SHARES]) * float(record[PRICE])

print(f"Cost calculated via named slices: {cost}")

# August 小撇步：slice 物件還有 .start, .stop, .step 屬性，
# 在開發更複雜的掃描器（如 Week 09）時很有幫助。
