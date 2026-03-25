# ============================================================================
# R3. 雙端佇列 (deque) - 保留最後 N 筆記錄（1.3）
# ============================================================================
# 本題展示 deque 的高效雙端操作，特別是 maxlen 參數的自動淘汰機制。
# ============================================================================

from collections import deque

print("【deque 基本用法】")
print("=" * 50)
print()

print("場景：維護最近 3 條系統日誌\n")

# 建立最大容量為 3 的 deque
q = deque(maxlen=3)
print(f"q = deque(maxlen=3)")
print(f"初始狀態：{list(q)}\n")

print("逐步添加元素：")
q.append(1)
print(f"q.append(1)  →  {list(q)}")
q.append(2)
print(f"q.append(2)  →  {list(q)}")
q.append(3)
print(f"q.append(3)  →  {list(q)}")
q.append(4)
print(f"q.append(4)  →  {list(q)}  （自動丟掉最舊的 1）\n")

print("說明：")
print("  - 當 deque 滿了（3 個元素）")
print("  - 添加新元素會自動刪除最舊的元素")
print("  - 始終保持最新的 3 個元素\n")

print("=" * 50)
print("【deque 的雙端操作】")
print("=" * 50)
print()

q = deque()
print("建立空 deque\n")

print("操作序列：")
q.append(1)
print(f"q.append(1)     →  {list(q)}")
q.appendleft(2)
print(f"q.appendleft(2) →  {list(q)}")
q.pop()
print(f"q.pop()         →  {list(q)}  （移除右端）")
q.popleft()
print(f"q.popleft()     →  {list(q)}  （移除左端）\n")

print("deque 的方法：")
print("  - append(x)：右端添加元素")
print("  - appendleft(x)：左端添加元素")
print("  - pop()：右端移除元素")
print(f"  - popleft()：左端移除元素")
print("  - maxlen：固定最大容量（自動淘汰舊元素）\n")

print("=" * 50)
print("【deque vs list：效能對比】")
print("=" * 50)
print("""
operation    list      deque
─────────────────────────────
append()     O(1)      O(1)       ✓ 兩者相同
pop()        O(1)      O(1)       ✓ 兩者相同
appendleft   N/A       O(1)       ✓ deque 高效
popleft()    O(n)      O(1)       ✓ deque 快 n 倍！

結論：
  - 需要雙端操作 → deque（左端操作很快）
  - 只需右端操作 → list（更簡單）
  - maxlen 自動淘汰 → deque（維護固定窗口）
""")

print("\n" + "=" * 50)
print("【實戰應用】")
print("=" * 50)
print()

print("應用 1：最近浏覽歷史（保留最新 5 條）")
history = deque(maxlen=5)
history.append('首頁')
history.append('搜索結果')
history.append('商品詳情')
history.append('購物車')
history.append('結算')
history.append('支付')  # 自動移除「首頁」
print(f"最近訪問：{list(history)}\n")

print("應用 2：生產者-消費者隊列")
queue = deque(maxlen=10)
print("處理任務隊列（隊長不超過 10）\n")
