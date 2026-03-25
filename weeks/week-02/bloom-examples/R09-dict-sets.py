# ============================================================================
# R9. 字典集合運算 - 尋找相同和差異（1.9）
# ============================================================================
# 本題展示如何使用字典的 keys() 和 items() 進行集合運算。
# ============================================================================

print("【場景】比較兩個用戶的屬性\n")

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print(f"用戶 A 的屬性：{a}")
print(f"用戶 B 的屬性：{b}\n")

print("=" * 50)
print("【運算 1】keys() 交集 - 兩者都有的鍵")
print("=" * 50)
print()

common_keys = a.keys() & b.keys()
print(f"a.keys() & b.keys() = {common_keys}")
print()
print("說明：")
print("  - 交集符號 & 找出共同鍵")
print("  - 結果：{'x', 'y'}\n")

print("=" * 50)
print("【運算 2】keys() 差集 - A 有但 B 沒有的鍵")
print("=" * 50)
print()

unique_a = a.keys() - b.keys()
print(f"a.keys() - b.keys() = {unique_a}")
print()
print("說明：")
print("  - 差集符號 - 找出獨有的鍵")
print("  - A 有的 z，B 沒有\n")

print("=" * 50)
print("【運算 3】items() 交集 - 完全相同的鍵值對")
print("=" * 50)
print()

common_items = a.items() & b.items()
print(f"a.items() & b.items() = {common_items}")
print()
print("說明：")
print("  - 交集需要鍵和值都相同")
print("  - ('x', 1) 在 a 中，但在 b 中是 ('x', 11)")
print("  - 只有 ('y', 2) 完全相同\n")

print("=" * 50)
print("【實戰應用】字典推導過濾")
print("=" * 50)
print()

print("需求：保留 a 中在 b 中也有的鍵\n")

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print(f"代碼：c = {{k: a[k] for k in a.keys() - {{'z', 'w'}}}}")
print(f"結果：{c}")
print()
print("說明：")
print("  - 從 a 的鍵中移除 z 和 w")
print("  - 保留 x 和 y 對應的值\n")

print("=" * 50)
print("【字典集合運算完整參考】")
print("=" * 50)
print("""
運算          語法                    結果      說明
─────────────────────────────────────────────────────────
交集          a.keys() & b.keys()     set      兩者都有
差集          a.keys() - b.keys()     set      a 獨有
並集          a.keys() | b.keys()     set      任一有
對稱差        a.keys() ^ b.keys()     set      只有一個有

交集(項目)   a.items() & b.items()   set      鍵值都相同

適用場景：
  ✓ 用戶比較
  ✓ 資料合併
  ✓ 尋找缺失字段
  ✓ 檢測配置差異
""")

print("\n" + "=" * 50)
print("【實用範例】")
print("=" * 50)
print()

print("例 1：尋找新增的鍵")
old_config = {'host': 'localhost', 'port': 5432}
new_config = {'host': 'localhost', 'port': 5432, 'ssl': True}
added = new_config.keys() - old_config.keys()
print(f"  新增鍵：{added}  # 增加了 ssl 選項\n")

print("例 2：清理配置")
required_keys = {'host', 'port', 'user', 'password'}
config = {'host': 'localhost', 'port': 5432, 'ssl': True, 'timeout': 30}
cleaned = {k: config[k] for k in config.keys() & required_keys}
print(f"  原配置：{config}")
print(f"  清理後：{cleaned}  # 只保留必需鍵\n")
