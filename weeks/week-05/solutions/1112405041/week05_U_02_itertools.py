# 【Bloom 階段：U - 理解與進階應用】
# U02. Itertools 效能工具組
# August 的惡意提醒：itertools 能幫你快速解決「排列組合」類型的題目。
# 但是！！注意 Week 10 (10226) 的 N=15 地雷。
# 直接呼叫 permutations(15) 會產生 1,307,674,368,000 個結果，100% TLE！
# 了解內建函式的上限，是區分「腳本小子」與「工程師」的分水嶺。

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

# 1. 切片無限流 (islice)
def count_forever():
    n = 0
    while True:
        yield n; n += 1

# 只取第 5 到第 10 項，而不需要生成前 5 項或無限生成
print(f"islice (5-10): {list(islice(count_forever(), 5, 10))}")

# 2. 條件式過濾 (dropwhile/takewhile)
nums = [1, 3, 5, 2, 4, 6]
# 只要小於 5 就丟掉 (直到遇到第一個 >= 5)
print(f"dropwhile (<5): {list(dropwhile(lambda x: x < 5, nums))}") # [5, 2, 4, 6]

# 3. 排列與組合 (CPE 常客)
items = ["A", "B", "C"]
# 排列 (考慮順序)
print(f"Permutations: {list(permutations(items, 2))}") # (A,B), (A,C)...
# 組合 (不論順序)
print(f"Combinations: {list(combinations(items, 2))}") # (A,B), (A,C)...

# August 惡意筆記：在面對 10226 的「剪枝」需求時，
# 內建的 permutations 常因不支援中途判斷而失效，屆時你必須親手寫 DFS。
# 對應 Week 10 的身分還原大手術。
