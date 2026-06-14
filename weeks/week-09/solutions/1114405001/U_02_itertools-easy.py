# U_02-easy. itertools 工具函數 - 簡化版
# 記住 5 個常用函數就夠了

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("=== 1. islice：從無窮序列取部分 ===")
# 建立無窮序列（0, 1, 2, 3, ...）
def count_from(n):
    while True:
        yield n
        n += 1

# 取第 5 到 10 個
c = count_from(0)
result = list(islice(c, 5, 10))
print(f"islice(count, 5, 10) → {result}")

print("\n=== 2. dropwhile + takewhile：條件篩選 ===")
nums = [1, 3, 5, 2, 4, 6]

# dropwhile：跳過小於 5 的，從 5 開始取
drop_result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x < 5) → {drop_result}")

# takewhile：只取小於 5 的
take_result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x < 5) → {take_result}")

print("\n=== 3. chain：多個序列串聯 ===")
a = [1, 2]
b = [3, 4]
c = [5]
result = list(chain(a, b, c))
print(f"chain([1,2], [3,4], [5]) → {result}")

print("\n=== 4. permutations：排列（順序重要） ===")
items = ["a", "b", "c"]

# 3 個全排列 = 3 × 2 × 1 = 6 種
all_perms = list(permutations(items))
print(f"排列 3 個：{len(all_perms)} 種")
for p in all_perms:
    print(f"  {''.join(p)}")

# 只排列 2 個
two_perms = list(permutations(items, 2))
print(f"\n排列 2 個：{len(two_perms)} 種")
for p in two_perms[:6]:
    print(f"  {''.join(p)}")

print("\n=== 5. combinations：組合（順序不重要） ===")
# 3 個取 2 個 = C(3,2) = 3 種
combos = list(combinations(items, 2))
print(f"組合 2 個：{len(combos)} 種")
for c in combos:
    print(f"  {''.join(c)}")

print("\n=== 實用例子：密碼窮舉 ===")
chars = ["A", "B", "1"]

# 2 位數密碼（不可重複）
print("不重複密碼：")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("\n=== 記憶重點 ===")
print("""
5 個必記函數：
1. islice(iter, start, stop) → 切片
2. dropwhile(cond, iter) → 跳過符合條件
3. takewhile(cond, iter) → 只取符合條件
4. chain(a, b, c) → 串聯多個
5. permutations(items, r) → 排列（順序重要）
6. combinations(items, r) → 組合（順序不重要）

何時用排列 vs 組合：
- 排列：密碼（AB ≠ BA）
- 組合：選擇（{A,B} = {B,A}）
""")