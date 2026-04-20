# 從 collections 模組導入 deque 類別。
from collections import deque

# 創建一個 deque 物件 q，並設定其最大長度為 3 (maxlen=3)。
# 當元素數量超過 maxlen 時，最舊的元素會自動從另一端被移除。
q = deque(maxlen=3)
# 顯示初始化後的 deque。
print(f"初始化 deque q (maxlen=3): {q}")
# 向 deque 的右端添加元素。
q.append(1)
print(f"append(1) 後: {q}")
q.append(2)
print(f"append(2) 後: {q}")
q.append(3)
print(f"append(3) 後: {q}")

# 當添加第四個元素時，由於 maxlen=3，最舊的元素 (1) 會自動被移除。
q.append(4)  # 自動丟掉最舊的 1
print(f"append(4) 後 (自動移除最舊的 1): {q}") # 顯示添加 4 後的 deque，並說明舊元素被移除。

print("\n--- 無限制長度的 deque 示範 ---")
# 創建一個沒有設定最大長度的 deque 物件 q。
# 這種情況下，deque 的長度是無限的，不會自動移除元素。
q = deque()
# 顯示初始化後的 deque。
print(f"初始化 deque q (無 maxlen 限制): {q}")
# 向 deque 的右端添加元素 1。
q.append(1)
print(f"append(1) 後: {q}")
# 向 deque 的左端添加元素 2。
q.appendleft(2)
print(f"appendleft(2) 後: {q}")

# 從 deque 的右端移除並回傳一個元素。
popped_right = q.pop()
print(f"pop() 移除右端元素 {popped_right} 後: {q}")
# 從 deque 的左端移除並回傳一個元素。
popped_left = q.popleft()
print(f"popleft() 移除左端元素 {popped_left} 後: {q}")
