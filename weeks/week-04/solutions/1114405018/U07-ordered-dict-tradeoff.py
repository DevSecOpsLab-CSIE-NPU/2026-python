"""
【U7】OrderedDict 的取捨：保序但更吃記憶體

核心概念：
=========

OrderedDict 是一種特殊的字典實現，它 ★保證★ 會按照插入順序成「迭代順序」。
相比之下，在 Python 3.7 之前，普通 dict 的反覆順序是「未保証的」（取決於 hash 值）。

但是，為了實現這種順序保証，OrderedDict 內部維護了一個「雙向鏈結串列」，
這導致 OrderedDict 需要額外的記憶體空間來存儲鏈結。

➤ 主要取捨：
  📌 優點：確保迭代順序 = 插入順序
  📌 優點：提供 move_to_end() 方法，可以動態改變排列順序
  ❌ 缺點：耗記憶體（每個 key-value 對需要額外的前後指標）
  ❌ 缺點：查詢、插入、刪除的速度略較慢（需要維護鏈結）

➤ 歷史背景（重要）：
  • Python 3.7 開始：普通 dict 也保証插入順序了！
  • 因此，OrderedDict 的核心用途已大幅降低
  • 現在 OrderedDict 主要用於：
    - 與舊程式碼的相容性
    - 需要 move_to_end() 方法時
    - 明確顯示「重視順序」的意圖

"""

from collections import OrderedDict
import sys
from typing import Dict

# ================================================================================
# 【方案1】普通 dict vs OrderedDict：在 Python 3.7+ 中的表現
# ================================================================================

print("\n" + "="*80)
print("【方案1】普通 dict vs OrderedDict 的外觀對比")
print("="*80)

# 普通的 dict（Python 3.7+ 已保証順序）
regular_dict = {}
regular_dict['foo'] = 1
regular_dict['bar'] = 2
regular_dict['baz'] = 3

# OrderedDict 版本
ordered_dict = OrderedDict()
ordered_dict['foo'] = 1
ordered_dict['bar'] = 2
ordered_dict['baz'] = 3

print("\n【執行01】在 Python 3.7+ 中，兩者的迭代順序幾乎相同：")
print(f"regular_dict 的 keys()：{list(regular_dict.keys())}")
print(f"ordered_dict 的 keys()：{list(ordered_dict.keys())}")

print("\n【執行02】兩者看起來相同，但內部結構完全不同")
print(f"regular_dict 的型別：{type(regular_dict)}")
print(f"ordered_dict 的型別：{type(ordered_dict)}")


# ================================================================================
# 【方案2】記憶體佔用量：OrderedDict 的隱藏成本
# ================================================================================

print("\n" + "="*80)
print("【方案2】記憶體佔用量對比")
print("="*80)

# 建立相同內容的兩個字典
test_dict = {}
test_ordered = OrderedDict()

for i in range(3):
    test_dict[f'key_{i}'] = i
    test_ordered[f'key_{i}'] = i

dict_size = sys.getsizeof(test_dict)
ordered_size = sys.getsizeof(test_ordered)

print("\n【執行03】同樣 3 個元素，記憶體佔用：")
print(f"普通 dict 的大小：{dict_size} bytes")
print(f"OrderedDict 的大小：{ordered_size} bytes")
print(f"額外記憶體開銷：{ordered_size - dict_size} bytes ({((ordered_size - dict_size) / dict_size * 100):.1f}% 增加)")

# 測試更大的字典
print("\n【執行04】用大量元素測試，額外開銷的百分比會更明顯：")
large_dict = {f'k_{i}': i for i in range(100)}
large_ordered = OrderedDict((f'k_{i}', i) for i in range(100))

large_dict_size = sys.getsizeof(large_dict)
large_ordered_size = sys.getsizeof(large_ordered)

print(f"普通 dict (100 個元素)：{large_dict_size} bytes")
print(f"OrderedDict (100 個元素)：{large_ordered_size} bytes")
print(f"額外開銷：{large_ordered_size - large_dict_size} bytes ({((large_ordered_size - large_dict_size) / large_dict_size * 100):.1f}% 增加)")


# ================================================================================
# 【方案3】move_to_end()：OrderedDict 的獨特功能
# ================================================================================

print("\n" + "="*80)
print("【方案3】move_to_end()：OrderedDict 的獨特功能")
print("="*80)

# 普通 dict 做不到的功能
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print("\n【執行05】move_to_end()：將某個元素移到隊尾（最後迭代位置）")
print(f"原始順序：{list(ordered.keys())}")

ordered.move_to_end('b')  # 把 'b' 移到隊尾
print(f"執行 move_to_end('b') 後：{list(ordered.keys())}")

print("\n【執行06】move_to_end(last=False)：將某個元素移到隊首")
ordered.move_to_end('d', last=False)  # 把 'd' 移到隊首
print(f"執行 move_to_end('d', last=False) 後：{list(ordered.keys())}")

print("\n【執行07】普通 dict 無法做到！")
try:
    regular = {'a': 1, 'b': 2, 'c': 3}
    # regular.move_to_end('a')  # ← 會報 AttributeError
    print("❌ 普通 dict 沒有 move_to_end() 方法")
except AttributeError as e:
    print(f"錯誤：{e}")


# ================================================================================
# 【方案4】Python 3.6 與 3.7+ 的時代背景
# ================================================================================

print("\n" + "="*80)
print("【方案4】為什麼 OrderedDict 現在不如以前重要？")
print("="*80)

print("""
【歷史演變】：

✓ Python 3.6 之前：
  • 普通 dict 的迭代順序「不保証」（因為 hash 函數）
  • 兩次執行同一個程式，dict 的順序可能不同
  • OrderedDict 因此成為重要工具（如果需要穩定順序）
  
✓ Python 3.6：
  • CPython 實現細節：dict 開始「非正式地」保持插入順序
  • 但官方還沒正式保証（規範上仍然不保証）
  
✓ Python 3.7+：
  • 官方正式保証：普通 dict 保持插入順序
  • dict 內部實現改進，也減少了記憶體開銷
  • OrderedDict 的需求大幅下降
  
【現代判斷】：
  ✓ 需要普通字典功能 + 想要順序 → 用普通 dict
  ✓ 需要 move_to_end() 或明確顯示「重視順序」→ 用 OrderedDict
  ✓ 需要支援 Python 3.6 以下 → 必須用 OrderedDict
""")


# ================================================================================
# 【方案5】實際用例：LRU 緩存（Least Recently Used）
# ================================================================================

print("\n" + "="*80)
print("【方案5】實戰：用 OrderedDict 實作簡易 LRU 緩存")
print("="*80)

class SimpleLRUCache:
    """
    一個簡易的 LRU 緩存實現。
    當容量滿時，移除最久未使用的項目（最舊的項目）。
    """
    def __init__(self, capacity: int):
        self.cache: OrderedDict = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        """取得值，並將該項目標記為「最近使用」」"""
        if key not in self.cache:
            return None
        
        # 移動到隊尾（表示最近使用）
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """儲存值，超過容量時移除舊項目"""
        if key in self.cache:
            self.cache.move_to_end(key)  # 如果已存在，更新為最近使用
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            oldest_key, _ = self.cache.popitem(last=False)  # 移除最舊的（隊首）
            print(f"  → 容量滿，移除最久未使用的項目：{oldest_key}")

print("\n【執行08】模擬 LRU 緩存的運作流程：")
lru = SimpleLRUCache(capacity=3)

print("\n步驟1：插入 3 個元素")
lru.put('user1', 'Alice')
lru.put('user2', 'Bob')
lru.put('user3', 'Charlie')
print(f"  當前快取順序（從舊到新）：{list(lru.cache.keys())}")

print("\n步驟2：插入第 4 個元素，超出容量")
lru.put('user4', 'David')
print(f"  當前快取順序（從舊到新）：{list(lru.cache.keys())}")

print("\n步驟3：存取 'user2'，將其標記為最近使用")
value = lru.get('user2')
print(f"  取得的值：{value}")
print(f"  當前快取順序（從舊到新）：{list(lru.cache.keys())}")

print("\n步驟4：插入 'user5'，'user3' 是最久未使用的")
lru.put('user5', 'Eve')
print(f"  當前快取順序（從舊到新）：{list(lru.cache.keys())}")


# ================================================================================
# 【方案6】OrderedDict.popitem()：移除順序的控制
# ================================================================================

print("\n" + "="*80)
print("【方案6】popitem() 的行為對比")
print("="*80)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
regular = {'a': 1, 'b': 2, 'c': 3}

print("\n【執行09】OrderedDict.popitem()：預設移除最後插入的")
od_copy = od.copy()
removed = od_copy.popitem()
print(f"移除的元素：{removed}")
print(f"剩餘元素：{list(od_copy.keys())}")

print("\n【執行10】OrderedDict.popitem(last=False)：移除最先插入的")
od_copy = od.copy()
removed = od_copy.popitem(last=False)
print(f"移除的元素（從隊首）：{removed}")
print(f"剩餘元素：{list(od_copy.keys())}")

print("\n【執行11】普通 dict.popitem()：Python 3.7+ 會移除最後插入的")
regular_copy = regular.copy()
removed = regular_copy.popitem()
print(f"移除的元素：{removed}")
print(f"剩餘元素：{list(regular_copy.keys())}")

print("\n【解說】：
  • OrderedDict.popitem(last=False) ← 普通 dict 沒有這個選項！
  • 這是 OrderedDict 的另一個獨特功能
""")


# ================================================================================
# 【方案7】何時使用 OrderedDict vs 普通 dict
# ================================================================================

print("\n" + "="*80)
print("【方案7】決策指南：何時使用 OrderedDict？")
print("="*80)

decision_tree = """
你問：「我應該用 OrderedDict 還是普通 dict？」

答案取決於以下問題：

❓ 問題1：你的 Python 版本是什麼？
    → Python 3.7+ ：通常用普通 dict（✓ 已保証順序）
    → Python 3.6- ：必須用 OrderedDict（✓ 唯一方式）

❓ 問題2：你需要 move_to_end() 或 popitem(last=False) 嗎？
    → 需要 ：必須用 OrderedDict（✓ 普通 dict 沒有）
    → 不需要 ：用普通 dict（✓ 更輕量、更快）

❓ 問題3：代碼意圖的可讀性重要嗎？
    → 「明確表達本程式重視順序」：用 OrderedDict（✓ 自文件化）
    → 順序只是一個特性：用普通 dict（✓ 避免過度設計）

【最終建議】：
  ✓ 簡單應用 → 普通 dict
  ✓ LRU/緩存/順序很重要 → OrderedDict
  ✓ 舊程式碼相容性 → OrderedDict
  ✓ 需要動態調整順序 → OrderedDict
"""

print(decision_tree)


# ================================================================================
# 【方案8】常見誤解與陷阱
# ================================================================================

print("\n" + "="*80)
print("【方案8】常見誤解與陷阱")
print("="*80)

print("\n❌ 陷阱1：以為普通 dict 在 Python 3.6 一定不保序")
print("""
  實際上：Python 3.6 的 CPython 實現已經保序（雖然官方沒正式保証）
  風險：依賴這個會在其他實現（如 PyPy）上出問題
  解決方案：如果一定要支援 3.6 以下 → 用 OrderedDict
""")

print("\n❌ 陷阱2：認為 OrderedDict 會自動排序值")
print("""
  實際上：OrderedDict 只保證 「插入順序」，不排序鍵或值
""")

od = OrderedDict()
od[3] = 'three'
od[1] = 'one'
od[2] = 'two'
print(f"  按照插入順序 [3, 1, 2]：{list(od.keys())}")
print(f"  （不是按數值排序的 [1, 2, 3]）")

print("\n❌ 陷阱3：期待 move_to_end() 會改變值")
print("""
  實際上：move_to_end() 只改變 「迭代位置」，不改變鍵或值
""")

od = OrderedDict([('a', 1), ('b', 2)])
od.move_to_end('a')
print(f"  move_to_end('a') 後：{dict(od)}")
print(f"  值完全相同，只是迭代順序變了：{list(od.keys())}")

print("\n❌ 陷阱4：忘記 OrderedDict(iter) 的初始化順序")
print("""
  實際上：初始化順序決定了插入順序，後面無法改變
""")

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(f"  OrderedDict([('a', 1), ('b', 2)])：{list(od1.keys())}")
print(f"  OrderedDict([('b', 2), ('a', 1)])：{list(od2.keys())}")
print(f"  初始化順序不同，結果不同")


# ================================================================================
# 【方案9】性能對比：序列化與反序列化
# ================================================================================

print("\n" + "="*80)
print("【方案9】性能對比：JSON 序列化")
print("="*80)

import json
import time

# 建立測試資料
data_regular = {f'key_{i}': i for i in range(1000)}
data_ordered = OrderedDict((f'key_{i}', i) for i in range(1000))

print("\n【執行12】JSON 序列化速度對比：")

# 取時 1000 次
start = time.time()
for _ in range(1000):
    json.dumps(data_regular)
regular_time = time.time() - start

start = time.time()
for _ in range(1000):
    json.dumps(data_ordered)
ordered_time = time.time() - start

print(f"普通 dict 序列化 1000 次：{regular_time:.4f} 秒")
print(f"OrderedDict 序列化 1000 次：{ordered_time:.4f} 秒")
print(f"差異：{abs(regular_time - ordered_time):.4f} 秒（約 {(abs(regular_time - ordered_time) / min(regular_time, ordered_time) * 100):.1f}%）")


# ================================================================================
# 【總結】OrderedDict 的取捨
# ================================================================================

print("\n" + "="*80)
print("【總結】OrderedDict 的取捨")
print("="*80)

summary = """
┌─────────────────────────────────────────────────────────────────────────────┐
│ OrderedDict 的本質                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 【優點】                                                                    │
│   ✓ 給保証「迭代順序 = 插入順序」（即使在舊版 Python）                   │
│   ✓ 提供 move_to_end() 方法（LRU 快取/排隊等應用）                     │
│   ✓ 提供 popitem(last=False) 方法（可選擇從頭或尾移除）                │
│   ✓ 明確表達代碼意圖：「這個字典的順序很重要」                          │
│                                                                             │
│ 【缺點】                                                                    │
│   ✗ 記憶體開銷更大（內部維護雙向鏈結）                                  │
│   ✗ 各種操作略微較慢（需要維護鏈結結構）                                │
│   ✗ 在 Python 3.7+ 中，大多數情況下不再必須                             │
│                                                                             │
│ 【決定因素】                                                                │
│                                                                             │
│  ┌─ Python 3.7+ 且不需要 move_to_end()                                    │
│  ├─ → 用普通 dict ✓                                                        │
│  │                                                                         │
│  ├─ 需要 move_to_end() 或特殊操作                                         │
│  ├─ → 用 OrderedDict ✓                                                     │
│  │                                                                         │
│  ├─ Python 3.6 以下                                                       │
│  ├─ → 用 OrderedDict ✓（為保險起見）                                     │
│  │                                                                         │
│  └─ 代碼明確性很重要                                                      │
│    └─ → 用 OrderedDict ✓（自文件化意圖）                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

【核心啟示】：
  「OrderedDict 不是『更好的字典』，
   而是『不同權衡的字典』。
   在現代 Python 中，使用它需要有充分的理由。」
"""

print(summary)
