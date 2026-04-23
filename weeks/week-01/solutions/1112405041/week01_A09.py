# 【Bloom 階段：U - 理解與進階應用】
# 9 比較、排序與 key 函式範例
# August 的惡意提醒：Python 的 Tuple 比較是「逐項比較」。
# 記住這個特性，Week 02 Task 2 的多重排序（分數降序、年齡升序）就能用一組 Tuple 搞定。

# 比較運算（Tuple 逐一比較特性）
a = (1, 2)
b = (1, 3)
# 比較規則：先比第一項，若相同再比第二項
result = a < b  # 1 == 1, 但 2 < 3, 所以 True

# 複雜對象排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
# 指定排序規則為 uid
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
# 找出 uid 最小的那筆資料
smallest = min(rows, key=lambda r: r['uid'])

print(f"Tuple compare (1,2) < (1,3): {result}")
print(f"Sorted rows: {rows_sorted}")
print(f"Smallest uid row: {smallest}")
# 老師秘訣：要在 lambda 實作降序，數值可以加個負號 -
rows_desc = sorted(rows, key=lambda r: -r['uid'])
print(f"Descending uid: {rows_desc}")
