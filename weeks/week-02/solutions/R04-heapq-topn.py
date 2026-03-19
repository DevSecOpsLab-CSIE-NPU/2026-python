# R4. heapq 取 Top-N（1.4）
# heapq 是 Python 標準庫中的堆積佇列模組，
# 提供了一種高效的方式來處理優先佇列和尋找最大/最小值。
# 特別適合用於從大量資料中快速取得前 N 個最大或最小元素。

# 匯入 heapq 模組
import heapq

# 創建一個包含數值的列表
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 使用 nlargest 函數取得列表中最大的 3 個元素
# 這個函數返回一個新的列表，包含最大的 N 個元素，不會修改原列表
heapq.nlargest(3, nums)

# 使用 nsmallest 函數取得列表中最小的 3 個元素
# 同樣返回一個新的列表，包含最小的 N 個元素
heapq.nsmallest(3, nums)

# 創建一個投資組合列表，每個元素是一個字典，包含股票名稱、股份數和價格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 使用 nsmallest 從投資組合中找到價格最低的 1 支股票
# key 參數指定比較的鍵，這裡使用 lambda 函數來提取 'price' 欄位
# 返回價格最低的股票字典
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 將 nums 列表轉換為堆積（heap）
# heapify 會將列表原地修改為一個有效的堆積結構
heap = list(nums)
heapq.heapify(heap)

# 從堆積中彈出並返回最小的元素
# heappop 會移除並返回堆積中的最小元素，保持堆積的性質
heapq.heappop(heap)
