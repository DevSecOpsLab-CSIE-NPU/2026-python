# Understand（理解）- itertools 工具函數
# `itertools` 模組提供了許多高效且記憶體友善的迭代器建構器，它們可以用來建立複雜的迭代模式。
# 這些工具函式通常回傳「迭代器 (iterator)」，這表示它們是「惰性求值 (lazy evaluation)」的，
# 只有在你真正需要值的時候才會計算並產生，這對於處理大量資料或無限序列非常有用。

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations
from itertools import combinations_with_replacement # 稍後會用到

print("--- islice() 切片 ---")

# 核心概念：islice() - 迭代器切片 (Iterator Slicing)
# `islice()` 函式可以像串列切片一樣，從一個迭代器中取出指定範圍的元素。
# 它的優點是，它不會像串列切片那樣一次性將所有元素載入記憶體，而是惰性地產生。
# 『語法』：`islice(可迭代物件, [start,] stop[, step])`
#   - `可迭代物件 (iterable)`：任何可迭代的物件，例如串列、生成器等。
#   - `start` (可選)：切片的起始索引（包含）。如果省略，預設從 0 開始。
#   - `stop`：切片的結束索引（不包含）。 
#   - `step` (可選)：切片的步長。如果省略，預設為 1。
# 『用途』：
#   1. 從一個可能無限的迭代器中取出有限的子序列。
#   2. 在不將整個序列載入記憶體的情況下，對大型序列進行切片操作。
#   3. 模擬串列切片行為，但適用於迭代器。
# 『結果』：
#   `islice()` 會回傳一個迭代器，當你迭代它時，它會產生從原始迭代器中切片出來的元素。
#   執行結果：
#   islice(c, 5, 10): [5, 6, 7, 8, 9]

# 範例資料：一個無限計數的生成器
def count(n):
    i = n
    while True:
        yield i
        i += 1

# 建立一個從 0 開始計數的無限生成器。
c = count(0)
# 使用 `islice` 從生成器 `c` 中取出索引 5 到 9 的元素（不包含 10）。
# `list()` 會將 `islice` 產生的迭代器轉換成串列，以便印出。
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
# 核心概念：dropwhile() - 條件式跳過 (Drop Elements While Condition is True)
# `dropwhile()` 函式會跳過可迭代物件中「開頭」符合指定條件的元素，直到遇到第一個不符合條件的元素為止。
# 一旦遇到第一個不符合條件的元素，它就會開始產生所有後續的元素，無論這些元素是否符合條件。
# 『語法』：`dropwhile(判斷函式, 可迭代物件)`
#   - `判斷函式 (predicate)`：一個接受一個參數並回傳布林值的函式。
#   - `可迭代物件 (iterable)`：要處理的序列。
# 『用途』：
#   1. 從序列的開頭移除符合特定條件的「前導」元素。
#   2. 處理日誌檔或資料流時，跳過開頭的無用資訊。
# 『結果』：
#   `dropwhile()` 會回傳一個迭代器，產生從第一個不符合條件的元素開始的所有後續元素。
#   執行結果：
#   dropwhile(x<5, [1, 3, 5, 2, 4, 6]): [5, 2, 4, 6]

# 範例資料：
nums = [1, 3, 5, 2, 4, 6]
# 使用 `dropwhile` 跳過所有小於 5 的開頭元素。
# `lambda x: x < 5` 是一個匿名函式，判斷元素是否小於 5。
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# 核心概念：takewhile() - 條件式取用 (Take Elements While Condition is True)
# `takewhile()` 函式會從可迭代物件的開頭開始，持續產生符合指定條件的元素，直到遇到第一個不符合條件的元素為止。
# 一旦遇到第一個不符合條件的元素，它就會停止，不再產生任何後續元素。
# 『語法』：`takewhile(判斷函式, 可迭代物件)`
#   - `判斷函式 (predicate)`：一個接受一個參數並回傳布林值的函式。
#   - `可迭代物件 (iterable)`：要處理的序列。
# 『用途』：
#   1. 從序列的開頭取出符合特定條件的「前導」元素。
#   2. 處理資料流時，只取用開頭的有效資訊。
# 『結果』：
#   `takewhile()` 會回傳一個迭代器，產生從開頭開始，直到第一個不符合條件的元素之前的所有元素。
#   執行結果：
#   takewhile(x<5, [1, 3, 5, 2, 4, 6]): [1, 3]

# 範例資料：沿用上面的 `nums` 串列。
# 使用 `takewhile` 取出所有小於 5 的開頭元素。
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
# 核心概念：chain() - 串聯多個可迭代物件 (Chain Multiple Iterables)
# `chain()` 函式可以將多個可迭代物件串聯起來，形成一個單一的迭代器。
# 它會先迭代完第一個可迭代物件的所有元素，然後再迭代第二個，依此類推。
# 『語法』：`chain(*可迭代物件)`
#   - `*可迭代物件`：接受任意數量的可迭代物件作為參數。
# 『用途』：
#   1. 將多個序列合併成一個單一的序列，方便統一處理。
#   2. 避免手動將多個串列 `+` 起來，特別是當序列數量很多或包含生成器時，`chain` 更高效且記憶體友善。
# 『結果』：
#   `chain()` 會回傳一個迭代器，產生所有輸入可迭代物件中的元素，按照它們被傳入的順序。
#   執行結果：
#   chain(a, b, c): [1, 2, 3, 4, 5]

# 範例資料：
a = [1, 2]
b = [3, 4]
c = [5]
# 使用 `chain` 將 `a`, `b`, `c` 三個串列串聯起來。
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
# 核心概念：permutations() - 排列 (Permutations)
# `permutations()` 函式會產生一個可迭代物件中所有可能的「排列 (Permutations)」。
# 排列是指從一組元素中取出指定數量的元素，並考慮其順序的所有可能組合。
# 『語法』：`permutations(可迭代物件, r=None)`
#   - `可迭代物件 (iterable)`：要產生排列的元素集合。
#   - `r` (可選)：每次排列取出的元素數量。如果省略，則 `r` 等於可迭代物件的長度，即產生所有元素的完整排列。
# 『用途』：
#   1. 產生所有可能的順序組合，例如密碼窮舉、排程問題。
#   2. 數學或演算法中需要遍歷所有排列的場景。
# 『結果』：
#   `permutations()` 會回傳一個迭代器，產生由元組組成的所有排列。
#   執行結果：
#   permutations(items):
#     ('a', 'b', 'c')
#     ('a', 'c', 'b')
#     ('b', 'a', 'c')
#     ('b', 'c', 'a')
#     ('c', 'a', 'b')
#     ('c', 'b', 'a')
#   permutations(items, 2):
#     ('a', 'b')
#     ('a', 'c')
#     ('b', 'a')
#     ('b', 'c')
#     ('c', 'a')
#     ('c', 'b')

# 範例資料：
items = ["a", "b", "c"]
print(f"permutations(items):")
# 產生 `items` 中所有元素的完整排列。
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
# 產生從 `items` 中取出 2 個元素的所有排列。
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# 核心概念：combinations() - 組合 (Combinations)
# `combinations()` 函式會產生一個可迭代物件中所有可能的「組合 (Combinations)」。
# 組合是指從一組元素中取出指定數量的元素，但不考慮其順序的所有可能組合。
# 『語法』：`combinations(可迭代物件, r)`
#   - `可迭代物件 (iterable)`：要產生組合的元素集合。
#   - `r`：每次組合取出的元素數量。這是必填參數。
# 『用途』：
#   1. 產生所有可能的元素組合，例如選取團隊成員、抽獎組合。
#   2. 數學或演算法中需要遍歷所有組合的場景。
# 『結果』：
#   `combinations()` 會回傳一個迭代器，產生由元組組成的所有組合。
#   執行結果：
#   combinations(items, 2):
#     ('a', 'b')
#     ('a', 'c')
#     ('b', 'c')

# 範例資料：沿用上面的 `items` 串列。
print(f"combinations(items, 2):")
# 產生從 `items` 中取出 2 個元素的所有組合。
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
# 核心概念：permutations() 應用於密碼窮舉 (Password Brute-forcing with Permutations)
# `permutations()` 可以用來產生所有可能的密碼組合，特別是當密碼長度固定且不允許重複字元時。
# 『用途』：
#   1. 模擬密碼破解過程。
#   2. 測試系統安全性，檢查弱密碼。
# 『結果』：
#   會印出所有由 `chars` 中選取 2 個字元且不重複的所有排列。
#   執行結果：
#   2位數密碼:
#     AB
#     A1
#     BA
#     B1
#     1A
#     1B

# 範例資料：
chars = ["A", "B", "1"]
print("2位數密碼:")
# 產生 `chars` 中取出 2 個字元的所有排列。
for p in permutations(chars, 2):
    # 將元組中的字元連接成字串，代表一個密碼。
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
# 核心概念：combinations_with_replacement() - 帶重複的組合 (Combinations with Replacement)
# `combinations_with_replacement()` 函式會產生一個可迭代物件中所有可能的「帶重複的組合」。
# 這表示從元素中選取時，同一個元素可以被選取多次。
# 『語法』：`combinations_with_replacement(可迭代物件, r)`
#   - `可迭代物件 (iterable)`：要產生組合的元素集合。
#   - `r`：每次組合取出的元素數量。
# 『用途』：
#   1. 產生允許重複字元的密碼組合。
#   2. 數學或演算法中需要遍歷帶重複組合的場景。
# 『結果』：
#   會印出所有由 `chars` 中選取 2 個字元且允許重複的所有組合。
#   執行結果：
#   2位數密碼（可重複）:
#     AA
#     AB
#     A1
#     BB
#     B1
#     11
# 這裡使用 `combinations_with_replacement` 雖然名稱是「組合」，但在密碼窮舉的語境下，
# 如果要考慮重複且順序也重要，通常會用 `product` (笛卡爾積)。
# 但如果只是想展示「允許重複」的概念，`combinations_with_replacement` 也能說明一部分。
# 如果要產生所有帶重複且考慮順序的密碼，應該使用 `itertools.product(chars, repeat=2)`。
# 範例：`product(chars, repeat=2)` 會產生 `AA, AB, A1, BA, BB, B1, 1A, 1B, 11`。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
