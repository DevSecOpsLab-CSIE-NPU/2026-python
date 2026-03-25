# ============================================================================
# U3. deque 的 maxlen：自動維護滑動窗口（1.3）
# ============================================================================
# 本題展示 deque(maxlen=N) 如何自動保留最新的 N 個元素。
# 
# 核心機制：
# 當 deque 滿了時，新元素進來會自動移除舊端的元素
# 類似一個固定大小的「滑動窗口」
# ============================================================================

from collections import deque


print("【deque 與 list 的對比】")
print("=" * 50)
print("""
list 在兩端操作時效能差：
  - list[0] 移除元素 — O(n)（需要重新索引所有後續元素）
  - list.pop() 移除最後元素 — O(1)（很快）

deque 兩端操作都高效：
  - deque.popleft() — O(1)
  - deque.pop() — O(1)
  - deque.appendleft() — O(1)
  - deque.append() — O(1)
""")

print("\n" + "=" * 50)
print("【deque(maxlen=N) 演示】")
print("=" * 50)
print()

print("場景：記錄最新的 N 個瀏覽歷史、日誌、傳感器數據等")
print()

print("【步驟 1】建立一個最大容量為 3 的 deque")
print()

q = deque(maxlen=3)
print(f"q = deque(maxlen=3)")
print(f"初始狀態：q = {list(q)}")
print()

print("【步驟 2】逐個添加 5 個元素")
print("-" * 50)
print()

data = [1, 2, 3, 4, 5]

for i, val in enumerate(data):
    print(f"第 {i+1} 步：q.append({val})")
    q.append(val)
    print(f"  結果：q = {list(q)}")
    
    if len(q) == 3:  # deque 滿了
        print(f"  ⚠️ deque 已滿（maxlen=3）")
    
    print()

print("【說明】")
print()
print("當 deque 已滿時：")
print("  - 第 4 步添加 4：最左邊的 1 被移除，變成 [2, 3, 4]")
print("  - 第 5 步添加 5：最左邊的 2 被移除，變成 [3, 4, 5]")
print()
print("最終只保留最新的 3 個元素：[3, 4, 5]")
print()

print("【最終結果】")
print(f"q = {list(q)}")
print(f"長度 = {len(q)}")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 1】最近登入用戶名")
print("=" * 50)
print()

recent_users = deque(maxlen=5)  # 記錄最近 5 個登入用戶

users = ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', 'Frank']

print(f"依次登入的用戶：{users}")
print(f"ystem 記錄最近 5 個登入\n")

for user in users:
    recent_users.append(user)
    print(f"用戶 {user} 登入 → 最近登入：{list(recent_users)}")

print()
print("最終結果：最近登入的 5 個用戶（可能重複）")
print(f"  {list(recent_users)}")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 2】滑動平均（Moving Average）")
print("=" * 50)
print()

print("場景：計算傳感器數據的滑動平均（平滑噪聲）")
print()

from itertools import islice

# 傳感器原始數據（含噪聲）
sensor_data = [10.2, 10.5, 9.8, 10.1, 10.3, 9.9, 10.4, 10.0, 10.2]
print(f"傳感器數據：{sensor_data}")
print(f"視窗大小：3 個數據點\n")

window = deque(maxlen=3)
moving_avgs = []

for val in sensor_data:
    window.append(val)
    if len(window) == 3:  # 等待視窗填滿
        avg = sum(window) / len(window)
        moving_avgs.append(avg)
        print(f"數據 {val} 進入 → 視窗 {list(window):.1f} → 平均 {avg:.2f}")

print()
print(f"滑動平均結果：")
for i, avg in enumerate(moving_avgs):
    print(f"  位置 {i}: {avg:.2f}")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【與 list 的效能對比】")
print("=" * 50)
print()

print("移除最舊元素的效能：")
print()
print("✓ deque（高效）:")
print("  q = deque([1, 2, 3, 4], maxlen=4)")
print("  q.append(5)  # 自動移除 1，時間 O(1)")
print()
print("✗ list（低效）:")
print("  lst = [1, 2, 3, 4]")
print("  lst.pop(0)  # 移除第一個，時間 O(n)")
print()

print("\n" + "=" * 50)
print("【deque 的其他操作】")
print("=" * 50)
print()

q = deque([1, 2, 3], maxlen=5)

print(f"初始：q = {list(q)}\n")

print("1. appendleft(0)  # 左端添加")
q.appendleft(0)
print(f"   結果：{list(q)}\n")

print("2. pop()  # 右端移除")
val = q.pop()
print(f"   移除：{val}, 結果：{list(q)}\n")

print("3. popleft()  # 左端移除")
val = q.popleft()
print(f"   移除：{val}, 結果：{list(q)}\n")

print("4. rotate(1)  # 右旋轉")
q.rotate(1)
print(f"   結果：{list(q)}\n")

print("5. rotate(-1)  # 左旋轉")
q.rotate(-1)
print(f"   結果：{list(q)}\n")

print("\n" + "=" * 50)
print("【總結】")
print("=" * 50)
print("""
deque(maxlen=N) 的優勢：
✓ 自動管理滑動窗口，無需手動移除
✓ 兩端操作都是 O(1)
✓ 適合實時數據流處理
✓ 節省記憶體（只保留最新 N 個元素）

適用場景：
✓ 瀏覽歷史、最近操作
✓ 日誌緩衝、固定大小隊列
✓ 滑動窗口聚合（平均、匹配等）
""")
