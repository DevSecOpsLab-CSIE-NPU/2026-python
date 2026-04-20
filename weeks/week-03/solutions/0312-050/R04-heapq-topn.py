# 導入 heapq 模組，它提供了堆積佇列演算法的實作，常用於高效地找到序列中的最大或最小 N 個元素。
import heapq

# 定義一個數字列表 nums。
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 顯示原始數字列表。
print(f"原始數字列表 nums: {nums}")

# 使用 heapq.nlargest() 找到列表中最大的 3 個元素。
# 這個函式會回傳一個包含最大 N 個元素的新列表，而不會改變原始列表。
largest_3 = heapq.nlargest(3, nums)
print(f"最大的 3 個元素 (nlargest): {largest_3}")

# 使用 heapq.nsmallest() 找到列表中最小的 3 個元素。
# 這個函式會回傳一個包含最小 N 個元素的新列表。
smallest_3 = heapq.nsmallest(3, nums)
print(f"最小的 3 個元素 (nsmallest): {smallest_3}\n")

# 定義一個股票投資組合列表 portfolio，每個元素是一個字典，包含股票名稱、數量和價格。
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 10.75},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
]
# 顯示原始投資組合。
print(f"原始投資組合 portfolio: {portfolio}")

# 使用 heapq.nsmallest() 找到投資組合中價格最低的 1 支股票。
# key 參數接受一個函式，用於從每個元素中提取用於比較的鍵。
# lambda s: s['price'] 表示以每個字典的 'price' 鍵的值進行比較。
cheapest_stock = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f"價格最低的 1 支股票: {cheapest_stock}\n")

print("--- 堆積操作示範 ---")
# 將 nums 列表複製一份，用於堆積操作，因為 heapq.heapify 會原地修改列表。
heap = list(nums)
# 顯示轉換前的列表。
print(f"轉換為堆積前的列表 heap: {heap}")

# 使用 heapq.heapify() 將列表轉換為一個最小堆積 (min-heap)。
# 最小堆積的特性是，根元素 (索引 0) 總是最小的。
heapq.heapify(heap)
print(f"heapify 後的堆積: {heap}")

# 使用 heapq.heappop() 從堆積中移除並回傳最小的元素。
# 每次 heappop 都會重新調整堆積，確保下一個彈出的仍然是最小的元素。
min_element = heapq.heappop(heap)
print(f"heappop 彈出最小元素 {min_element} 後的堆積: {heap}")
min_element_2 = heapq.heappop(heap)
print(f"再次 heappop 彈出最小元素 {min_element_2} 後的堆積: {heap}")
