# 9 比較、排序與 key 函式範例
# 排序和比較是演算法的基礎，幾乎所有進階題都需要

# 比較運算（tuple 逐一比較）
# 為什麼重要？
# 1. Python tuple 的比較是「逐個元素」比較的（字典序比較）
# 2. (1, 2) < (1, 3)：先比第一位都是 1，相等，再比第二位 2<3 所以为真
# 3. 後續題目會用 (priority, index, item) 的 tuple 來自動排序優先級
a = (1, 2)
b = (1, 3)
result = a < b  # 結果：True（因為 2 < 3）

# key 排序（根據指定的「鑰匙」排序）
# 為什麼需要 key？
# 1. 資料結構複雜時：dict 或 object 不能直接比較，需要指定排序的欄位
# 2. 自訂排序邏輯：可以按任意規則排序（如按字元長度、按數值大小）
# 3. 避免複雜的資料轉換：不需要提取欄位再排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])  # 按 uid 排序：[{'uid': 1}, {'uid': 2}, {'uid': 3}]

# min/max 搭配 key
# 為什麼需要？Top-N 問題的核心工具
# 1. 無需排序整個列表，直接找最小/最大元素
# 2. 效能：O(N) vs sorted() 的 O(N log N)
# 3. 實用：尋找最優先的項目、最小成本的方案
smallest = min(rows, key=lambda r: r['uid'])  # 結果：{'uid': 1}（uid 最小的）
