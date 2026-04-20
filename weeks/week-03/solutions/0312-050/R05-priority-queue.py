# 導入 heapq 模組，用於實現堆積佇列，這是構建優先佇列的基礎。
import heapq

# 定義一個 PriorityQueue 類別，用於實現一個優先佇列。
# 優先佇列是一種特殊的佇列，其中每個元素都帶有優先級，較高優先級的元素會先被取出。
class PriorityQueue:
    # 初始化方法，在創建 PriorityQueue 物件時被呼叫。
    def __init__(self):
        # _queue 是一個列表，用於儲存堆積中的元素。
        # 每個元素是一個元組：(-priority, index, item)。
        # 優先級取負值是為了讓 heapq 模組實現的最小堆積 (min-heap) 能夠模擬最大優先級佇列。
        # 也就是說，負值越小（絕對值越大），優先級越高，在最小堆積中會排在前面。
        self._queue = []
        # _index 用於處理相同優先級的元素。
        # 它確保即使優先級相同，元素的插入順序也能被保留，避免比較兩個實際項目時可能發生的錯誤。
        self._index = 0

    # push 方法用於將一個項目 (item) 及其優先級 (priority) 添加到佇列中。
    def push(self, item, priority):
        # heapq.heappush() 函式將一個元素添加到堆積中，並保持堆積的特性。
        # 這裡添加的元素是一個元組：(-priority, self._index, item)。
        # -priority: 確保高優先級的項目（數字較大）在最小堆積中排在前面。
        # self._index: 作為第二個比較鍵，用於打破相同優先級的平局，保證穩定性。
        # item: 實際儲存的項目。
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 每次添加元素後，_index 遞增，確保每個元素的索引都是唯一的。
        self._index += 1
        print(f"  推入 '{item}' (優先級: {priority})，佇列狀態: {self._queue}") # 顯示推入後的佇列狀態。

    # pop 方法用於從佇列中取出並回傳優先級最高的項目。
    def pop(self):
        # heapq.heappop() 函式從堆積中移除並回傳最小的元素。
        # 由於我們儲存的是 (-priority, index, item)，最小的元素實際上是優先級最高的項目。
        # 我們只關心實際的項目，所以取回傳元組的最後一個元素 ([-1])。
        popped_tuple = heapq.heappop(self._queue)
        item = popped_tuple[-1]
        print(f"  彈出 '{item}' (優先級: {-popped_tuple[0]})，佇列狀態: {self._queue}") # 顯示彈出後的佇列狀態。
        return item

# 創建一個 PriorityQueue 物件。
pq = PriorityQueue()
print("初始化優先佇列。\n")

# 向優先佇列中添加一些項目，並指定它們的優先級。
pq.push('task1', 3) # 優先級 3
pq.push('task2', 1) # 優先級 1
pq.push('task3', 2) # 優先級 2
pq.push('task4', 3) # 優先級 3 (與 task1 優先級相同，但會因為 index 較大而後取出)
print("\n所有項目推入完成。\n")

# 從優先佇列中彈出項目，觀察它們的取出順序。
print("開始彈出項目:")
print(f"取出: {pq.pop()}") # 應該是 task1 (優先級最高，且先於 task4 插入)
print(f"取出: {pq.pop()}") # 應該是 task3
print(f"取出: {pq.pop()}") # 應該是 task4
print(f"取出: {pq.pop()}") # 應該是 task2
print("\n所有項目彈出完成。")
