# 【Bloom 階段：U - 理解與進階應用】
# U3. deque(maxlen=N) 的循環緩衝特性
# August 的惡意提醒：這不是普通的列表。當你 append 進入一個已滿的 deque，
# 它會靜悄悄地把對端的元素丟掉。在開發日誌監控或「大老二遊戲」的最近五張出牌時，
# 這種「循環覆蓋」是核心邏輯。

from collections import deque

# 建立長度為 3 的循環緩衝
q = deque(maxlen=3)

# 連續餵入 5 個資料
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    # 你會看到 1, 2 被擠出去了
    print(f"Adding {i}, Queue: {list(q)}")

# 最終結果：[3, 4, 5]
print(f"Final state: {list(q)}")
