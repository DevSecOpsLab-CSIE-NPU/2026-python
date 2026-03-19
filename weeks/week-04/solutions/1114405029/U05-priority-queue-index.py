# U5. 優先佇列為何要加 index（1.5）

# 匯入 heapq 模組
# heapq 可以用來實作 heap（堆積）結構，
# 也常用來做優先佇列（priority queue）
import heapq

# 定義一個類別 Item
# 這個類別只有一個屬性 name，用來記錄物件名稱
class Item:
    def __init__(self, name):
        self.name = name

# 建立一個空串列 pq
# 之後會把它當成優先佇列來使用
pq = []

# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 上面註解掉的錯誤示範代表：
# 如果 heapq 中放入的是 (priority, item)
# 當兩筆資料的 priority 相同時，
# Python 會繼續比較第二個元素，也就是 item 本身
# 但是 Item 類別沒有定義大小比較（例如 <）
# 因此會發生 TypeError 錯誤

# 正解：加 index 避免比較 item
# 建立一個索引值 idx，初始為 0
# 這個 idx 會在每次加入資料時遞增
# 作用是：當 priority 一樣時，就比較 index，
# 這樣就不需要直接比較 Item 物件本身
idx = 0

# 將第一筆資料放入優先佇列
# 放入的格式為 (priority, index, item)
# priority = -1
# index = 0
# item = Item('a')
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1

# 將第二筆資料放入優先佇列
# 這筆資料的 priority 也同樣是 -1
# 但因為 index 不同，所以 heapq 可以順利比較
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1

# 印出目前優先佇列的原始內容
# 因為裡面有 Item 物件，所以直接印出時會看到物件位址資訊
print("目前 pq 的原始內容：")
print(pq)

print()  # 空一行，讓輸出結果更清楚

# 為了讓輸出更容易閱讀，
# 這裡逐筆取出 pq 中的資料並印出各欄位內容
print("pq 中每筆資料的詳細內容：")
for priority, index, item in pq:
    print("priority =", priority, ", index =", index, ", item.name =", item.name)

print()  # 空一行，讓輸出結果更清楚

# 使用 heappop() 取出優先佇列中優先順序最高的元素
# 因為 heapq 是最小堆積，所以數值較小者會先被取出
# 這裡使用 -1 是常見技巧，模擬較高優先權
first = heapq.heappop(pq)

# 印出第一筆被取出的資料
print("使用 heappop() 取出的第一筆資料：")
print("priority =", first[0], ", index =", first[1], ", item.name =", first[2].name)

print()  # 空一行，讓輸出結果更清楚

# 印出取出一筆之後，pq 剩下的資料
print("取出一筆後，pq 剩下的資料：")
for priority, index, item in pq:
    print("priority =", priority, ", index =", index, ", item.name =", item.name)

print()  # 空一行，讓輸出結果更清楚

# 說明為什麼要加 index
print("說明：當 priority 相同時，heapq 會繼續比較下一個元素。")
print("如果下一個元素是 Item 物件，因為 Item 不支援大小比較，程式就會發生 TypeError。")
print("加入 index 後，就能在 priority 相同時改比較 index，避免直接比較 Item 物件。")