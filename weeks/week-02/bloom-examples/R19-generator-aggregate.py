# ============================================================================
# R19. 轉換+聚合：生成器表達式的靈活應用（1.19）
# ============================================================================
# 本題展示生成器表達式如何高效連接轉換和聚合操作。
# 生成器優勢：避免建立中間列表，直接傳遞給聚合函式
# ============================================================================

print("【生成器表達式簡介】")
print("=" * 50)
print("""
生成器表達式能將「轉換」和「聚合」優雅地組合：

傳統做法（低效）：
  1. temps = [float(row[1]) for row in data]  # 建立中間列表
  2. avg = sum(temps) / len(temps)             # 聚合

生成器做法（高效）：
  avg = sum(float(row[1]) for row in data) / len(list(data))
  # 無需建立中間列表，直接轉換並聚合
""")

print("\n" + "=" * 50)
print("【範例 1】平方和計算")
print("=" * 50)
print()

nums = [1, 2, 3]
print(f"原始列表: {nums}")
print(f"需求: 計算所有元素的平方和\n")

# 【方法 A】傳統做法（建立中間列表）
print("方法 A：傳統做法")
print("  squared = [x * x for x in nums]  # 建立中間列表")
print("  result = sum(squared)")
squared = [x * x for x in nums]
result_a = sum(squared)
print(f"  中間列表: {squared}")
print(f"  結果: {result_a}")
print()

# 【方法 B】生成器做法（高效）
print("方法 B：生成器做法（推薦）")
print("  result = sum(x * x for x in nums)  # 無需中間列表")
result_b = sum(x * x for x in nums)
print(f"  結果: {result_b}")
print(f"說明：生成器逐個產生 x*x，sum() 直接聚合，無中間列表")
print()

print("效能優勢：")
print(f"  方法 A 語句數：2 次操作")
print(f"  方法 B 語句數：1 次操作")
print(f"  記憶體使用：方法 B 顯著更低")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【範例 2】字符串連接")
print("=" * 50)
print()

s = ('ACME', 50, 123.45)
print(f"原始元組: {s}")
print(f"需求: 用逗號連接所有元素（必須轉換為字符串）\n")

# 【方法 A】列表推導式
print("方法 A：列表推導式")
print("  str_list = [str(x) for x in s]")
print("  result = ','.join(str_list)")
str_list = [str(x) for x in s]
result_a = ','.join(str_list)
print(f"  中間列表: {str_list}")
print(f"  結果: {result_a}")
print()

# 【方法 B】生成器表達式
print("方法 B：生成器表達式（推薦）")
print("  result = ','.join(str(x) for x in s)")
result_b = ','.join(str(x) for x in s)
print(f"  結果: {result_b}")
print(f"說明：生成器直接向 join() 提供轉換後的字符串")
print()

print("【重點】")
print("  str.join() 期望一個可迭代物件，生成器完美匹配")
print("  無需先轉換為列表")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【範例 3】複雜資料結構的聚合")
print("=" * 50)
print()

portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'IBM', 'shares': 50},
]
print(f"投資組合: {portfolio}")
print(f"需求: 找出持股數最少的公司\n")

# ──────────────────────────────────────────────────────────────────────────
print("【方法 1】使用生成器提取 shares，再找最小值")
print()

print("代碼：min(s['shares'] for s in portfolio)")
min_shares = min(s['shares'] for s in portfolio)
print(f"結果: {min_shares}")
print(f"說明：返回最小的 shares 值，但不知道是哪間公司")
print()

# ──────────────────────────────────────────────────────────────────────────
print("【方法 2】直接找最小的字典，並指定鍵作為比較標準")
print()

print("代碼：min(portfolio, key=lambda s: s['shares'])")
min_item = min(portfolio, key=lambda s: s['shares'])
print(f"結果: {min_item}")
print(f"說明：返回整個字典，包含公司名稱")
print()

print("\n【方法對比】")
print("-" * 50)
print("方法 1：")
print("  min(s['shares'] for s in portfolio)")
print("  優點：簡單，只需要值")
print("  缺點：失去了字典的其他資訊")
print()
print("方法 2：")
print("  min(portfolio, key=lambda s: s['shares'])")
print("  優點：保留整個字典，可獲取其他資訊")
print("  缺點：稍微複雜，需要 lambda")
print()

print("\n【結論】")
print("-" * 50)
print("""
選擇取決於需求：
✓ 只需要值 → 使用方法 1（生成器 + 聚合）
✓ 需要整個物件 → 使用方法 2（key 引數）

生成器表達式的關鍵：
✓ 延遲求值，高效處理大資料
✓ 無需建立中間列表
✓ 可直接傳遞給聚合函式（sum, min, max, join 等）
""")
