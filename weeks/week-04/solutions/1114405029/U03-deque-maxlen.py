# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

# 從 collections 模組匯入 deque
# deque 是 double-ended queue（雙向佇列）的意思
# 它可以在左邊或右邊快速加入或移除元素
from collections import deque

# 建立一個 deque 物件 q
# maxlen=3 表示這個 deque 最多只能保存 3 個元素
# 一旦超過 3 個，新資料加入時，最舊的資料會自動被移除
q = deque(maxlen=3)

# 使用 for 迴圈，依序將串列中的元素加入 q
for i in [1, 2, 3, 4, 5]:
    # 將目前的元素 i 加到 deque 的右邊
    q.append(i)

    # 印出每次加入新元素後的 q 內容
    # 這樣可以清楚觀察 deque 如何在超過最大長度時，自動刪除最舊資料
    print("加入", i, "之後，q 的內容是：", list(q))

# 結果只剩 [3, 4, 5]

print()  # 空一行，讓輸出結果更清楚

# 最後印出 q 的完整內容
# 因為 maxlen=3，所以最後只會保留最後加入的 3 筆資料
print("最終 q 的內容：", list(q))

# 印出 q 的最大長度設定
print("q 的最大長度 maxlen：", q.maxlen)

print()  # 空一行，讓輸出結果更清楚

# 說明為什麼最後只剩下 [3, 4, 5]
print("說明：因為 q 的最大長度是 3，所以當加入第 4、5 個元素時，")
print("前面最早加入的元素會自動被移除，因此最後只保留最後 3 筆資料 [3, 4, 5]。")