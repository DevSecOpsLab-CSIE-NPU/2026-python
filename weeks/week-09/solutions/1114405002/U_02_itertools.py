# Understand（理解）- itertools 工具函數
# ============================================================================
# itertools 是 Python 標準庫中用於高效迭代操作的模組
# 提供多種工具來處理迭代器，可進行切片、過濾、排列、組合等操作
# 相比普通迴圈，itertools 函數通常更快、更省記憶體（因使用惰性求值）
# ============================================================================

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")
# islice(iterable, start, stop, step) 用於對迭代器進行切片操作
# 與列表切片不同，islice 支援無限迭代器（如生成器）
# 參數說明：
#   - start: 起始索引（不提供則為 0）
#   - stop: 結束索引（不含該位置）
#   - step: 步長（可選）

def count(n):
    """
    無限計數生成器
    持續產生從 n 開始的遞增整數，永不停止（除非手動中止）
    這種無限生成器特別適合搭配 islice 來提取部分結果
    """
    i = n
    while True:
        yield i
        i += 1


c = count(0)  # 建立一個從 0 開始的無限計數器
result = list(islice(c, 5, 10))  # 切取第 5-9 個元素（共 5 個）
print(f"islice(c, 5, 10): {result}")  # 輸出: [5, 6, 7, 8, 9]

print("\n--- dropwhile() 條件跳過 ---")
# dropwhile(predicate, iterable) 從迭代器開頭開始跳過元素，直到條件不滿足
# 第一個不符合條件的元素開始，之後的所有元素都會被保留
# 注意：只在開頭進行跳過，一旦出現不符合的元素，就停止跳過

nums = [1, 3, 5, 2, 4, 6]  # 測試列表
result = list(dropwhile(lambda x: x < 5, nums))  # 跳過所有小於 5 的元素（從前往後）
print(f"dropwhile(x<5, {nums}): {result}")  # 輸出: [5, 2, 4, 6]

print("\n--- takewhile() 條件取用 ---")
# takewhile(predicate, iterable) 與 dropwhile 相反
# 從迭代器開頭開始收集元素，直到條件第一次不滿足（停止收集）
# 應用場景：取得日誌檔中的某一段特定級別的訊息

result = list(takewhile(lambda x: x < 5, nums))  # 收集小於 5 的元素（從前往後）
print(f"takewhile(x<5, {nums}): {result}")  # 輸出: [1, 3]（遇到 5 就停止）

print("\n--- chain() 串聯 ---")
# chain(*iterables) 將多個迭代器的元素依序連接成一個長序列
# 相比 a + b + c（建立新列表），chain 是惰性求值，更省記憶體

a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")  # 輸出: [1, 2, 3, 4, 5]

print("\n--- permutations() 排列 ---")
# permutations(iterable, r=None) 返回所有長度為 r 的排列
# 排列考慮順序，(a,b) 與 (b,a) 被視為不同的排列
# 如果 r 未指定，則 r 預設為 iterable 的長度

items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):  # 所有元素的排列（共 3! = 6 種）
    print(f"  {p}")

print(f"permutations(items, 2):")
for p in permutations(items, 2):  # 選 2 個元素的排列（共 3P2 = 6 種）
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations(iterable, r) 返回所有長度為 r 的組合
# 組合不考慮順序，(a,b) 與 (b,a) 被視為相同的組合
# 組合數量 = C(n,r) = n! / (r! * (n-r)!)

print(f"combinations(items, 2):")
for c in combinations(items, 2):  # 從 3 個中選 2 個（共 C(3,2) = 3 種）
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
# 實際應用：暴力破解密碼時需考慮
# 1. 排列：密碼考慮順序（如 "AB" ≠ "BA"）
# 2. 組合（可重複）：允許重複字元

chars = ["A", "B", "1"]
print("2位數密碼（排列，無重複）:")
for p in permutations(chars, 2):  # 排列：ABC, ACB, BAC, BCA, CAB, CBA（6 種）
    print(f"  {''.join(p)}")

print("2位數密碼（組合，可重複）:")
from itertools import combinations_with_replacement

for p in combinations_with_replacement(chars, 2):  # 可重複組合
    print(f"  {''.join(p)}")
