# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
# 展示 deque 使用固定大小上限（maxlen）的滑動窗口特性

# 從 collections 模組導入 deque（雙端隊列）
from collections import deque

# 建立最大長度為 3 的 deque
q = deque(maxlen=3)

# 添加 5 個元素
for i in [1, 2, 3, 4, 5]:
    q.append(i) 
    print(f"append({i}) -> {list(q)}")
    # 添加步驟：
    # append(1) -> [1]
    # append(2) -> [1, 2]
    # append(3) -> [1, 2, 3]，已滿
    # append(4) -> [2, 3, 4]，自動移除最左邊的 1
    # append(5) -> [3, 4, 5]，自動移除最左邊的 2

print(f"\n最終結果: {list(q)}")
# 結果只剩最後 3 個元素 [3, 4, 5]
# 這個特性很適合用於實現「滑動窗口」或「移動平均」
