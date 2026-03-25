# ============================================================================
# R20. ChainMap - 多字典層級查詢（1.20）
# ============================================================================
# 本題展示 ChainMap 如何在多個字典中按優先順序進行鍵查詢。
# 應用場景：
# 1. 配置覆寫：基礎配置 + 使用者配置 + 環境變數
# 2. 作用域鏈：本地變數 + 全域變數
# 3. 多層快取：L1 快取 + L2 快取 + 磁盤存儲
# ============================================================================

from collections import ChainMap


print("【ChainMap 基礎概念】")
print("=" * 50)
print("""
ChainMap 建立多個字典的「查詢鏈」：
- 按提供的順序依次查詢字典
- 找到鍵就立即返回，不再查詢後續字典
- 需要更新時，更新的總是第一個字典
""")

print("\n" + "=" * 50)
print("【基本範例】")
print("=" * 50)
print()

# ──────────────────────────────────────────────────────────────────────────
print("【步驟 1】建立两个字典")
print()

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

print(f"字典 a: {a}")
print(f"字典 b: {b}")
print()
print("注意：兩個字典都有鍵 'z'，值分別為 3 和 4")
print()

# ──────────────────────────────────────────────────────────────────────────
print("【步驟 2】使用 ChainMap 連接")
print()

# 【語法】ChainMap(*dicts)
# - 按提供的順序建立查詢鏈
# - a 被視為優先字典，b 是備用字典
c = ChainMap(a, b)
print(f"c = ChainMap(a, b)")
print(f"c.maps = {c.maps}  # 查看內部字典列表")
print()

# ──────────────────────────────────────────────────────────────────────────
print("【步驟 3】查詢鍵")
print("-" * 50)
print()

# 【查詢 1】'x' 只在 a 中
print("查詢 1：c['x']")
result_x = c['x']
print(f"  結果: {result_x}")
print(f"  說明: 'x' 只存在於字典 a，直接返回 a['x'] = 1")
print()

# 【查詢 2】'y' 只在 b 中
print("查詢 2：c['y']")
result_y = c['y']
print(f"  結果: {result_y}")
print(f"  說明: 'y' 不在 a 中，查詢 b，返回 b['y'] = 2")
print()

# 【查詢 3】'z' 在 a 和 b 中都有（優先級問題）
print("查詢 3：c['z']  # 關鍵！")
result_z = c['z']
print(f"  結果: {result_z}")
print(f"  說明: 'z' 在 a 中找到值 3，即使 b 中也有")
print(f"        ChainMap 總是返回第一個字典（a）中的值")
print()

print("【優先級順序】")
print(f"  c = ChainMap(a, b)")
print(f"  查詢順序：a → b → (KeyError)")
print(f"  a 是優先字典，若找不到才查詢 b")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 1】配置覆寫（常見場景）")
print("=" * 50)
print()

print("場景：程式有基礎配置，但使用者可以覆寫")
print()

# 基礎配置
default_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'default'
}

print(f"【基礎配置】")
for k, v in default_config.items():
    print(f"  {k}: {v}")
print()

# 使用者配置（僅覆寫部分）
user_config = {
    'host': '192.168.1.1',
    'port': 5432,
    # 其他使用預設值
}

print(f"【使用者配置】（只指定了 host 和 port）")
for k, v in user_config.items():
    print(f"  {k}: {v}")
print()

# 使用 ChainMap：使用者配置優先，預設配置備用
config = ChainMap(user_config, default_config)
print(f"【合併配置】ChainMap(user_config, default_config)")
print()

print("最終配置：")
for key in set(default_config.keys()) | set(user_config.keys()):
    print(f"  {key}: {config[key]}  # {('✓ 使用者' if key in user_config else '✓ 預設')}")
print()

print("說明：")
print("  - host 和 port 使用使用者值")
print("  - user 和 password 使用預設值")
print("  - 無需手動合併兩個字典")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 2】更新行為")
print("=" * 50)
print()

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}
m = ChainMap(dict1, dict2)

print(f"初始狀態：")
print(f"  dict1: {dict1}")
print(f"  dict2: {dict2}")
print(f"  m['a'] = {m['a']}, m['b'] = {m['b']}, m['c'] = {m['c']}")
print()

print(f"執行：m['a'] = 100  # 更新")
m['a'] = 100
print(f"結果：")
print(f"  dict1: {dict1}  ✓ 改變（優先字典）")
print(f"  dict2: {dict2}  （不改變）")
print()

print(f"執行：m['b'] = 200  # 修改現有鍵")
m['b'] = 200
print(f"結果：")
print(f"  dict1: {dict1}  ✓ dict1['b'] 被設為 200")
print(f"  dict2: {dict2}  （不改變，即使 dict2['b'] 也存在）")
print()

print("【重點】ChainMap.update() 總是更新第一個字典")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 3】多層級查詢（作用域鏈）")
print("=" * 50)
print()

print("場景：類似程式語言的變數作用域")
print()

# 模擬作用域
global_vars = {'x': 1, 'y': 2}
local_vars = {'y': 20, 'z': 3}  # 本地變數覆寫全域

scope = ChainMap(local_vars, global_vars)
print(f"全域變數: {global_vars}")
print(f"本地變數: {local_vars}")
print()

print("查詢順序（本地優先）：")
print(f"  scope['x'] = {scope['x']}  # 全域變數")
print(f"  scope['y'] = {scope['y']}  # 本地變數（覆寫全域）")
print(f"  scope['z'] = {scope['z']}  # 本地變數")
print()

print("這就是程式語言中的作用域解析機制！")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【常用方法】")
print("=" * 50)
print()

print("1. .maps - 獲取字典列表")
print(f"   c.maps = {m.maps}")
print()

print("2. .parents - 獲取除第一個外的 ChainMap")
print(f"   c.parents = {m.parents}")
print()

print("3. keys() / values() / items() - 視圖操作")
print(f"   c.keys() = {list(m.keys())}")
print(f"   c.values() = {list(m.values())}")
print()

print("4. get() / pop() - 標準字典方法")
print(f"   c.get('missing', 'default') = {m.get('missing', 'default')}")
print()

print("\n" + "=" * 50)
print("【ChainMap vs 字典合併】")
print("=" * 50)
print("""
特性              ChainMap           dict 合併
─────────────────────────────────────────────────
視圖              ✓ 透視（動態）     ✗ 靜態副本
記憶體使用        ✓ 低（無複製）      ✗ 高（複製資料）
修改同步          ✓ 自動同步          ✗ 不同步
複雜度            O(n) 查詢           O(1) 查詢

推薦使用：
✓ ChainMap：需要動態層級查詢、配置覆寫
✓ dict 合併：一次性合併多個字典
""")
