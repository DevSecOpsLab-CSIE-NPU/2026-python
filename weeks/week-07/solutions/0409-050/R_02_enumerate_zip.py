# Remember（記憶）- enumerate() 和 zip()
# 本範例介紹 Python 中兩個非常實用且常見的內建函式：`enumerate()` 和 `zip()`，它們能讓你在處理序列資料時更有效率。

# 範例資料：
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# 核心概念：enumerate() 基本用法 (Basic Usage of enumerate())
# `enumerate()` 函式會將一個「可迭代物件 (Iterable)」轉換成一個「索引-值」對的序列。它會自動為可迭代物件中的每個元素產生一個計數器（索引），並將索引和元素打包成一個元組 (tuple)。
# 『語法』：`enumerate(可迭代物件)`
#   - `可迭代物件 (Iterable)`：任何可以被 `for` 迴圈一個一個走訪的資料集合，例如串列 (list)、元組 (tuple)、字串 (string) 等。
# 『用途』：
#   1. 在迭代序列時，同時取得元素的「索引 (index)」和「值 (value)」，而不需要手動維護一個計數器變數。
#   2. 讓程式碼更簡潔、更具可讀性。
# 『結果』：
#   `enumerate(colors)` 會產生一個迭代器 (iterator)，每次迭代會回傳一個元組 `(索引, 值)`。
#   執行結果：
#   0: red
#   1: green
#   2: blue
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 核心概念：enumerate() 指定起始索引 (Specifying Start Index for enumerate())
# `enumerate()` 函式可以接受一個 `start` 參數，讓你指定索引的起始值，而不是預設的 0。
# 『語法』：`enumerate(可迭代物件, start=起始值)`
#   - `start`：一個整數，指定索引從哪個數字開始計數。預設值為 0。
# 『用途』：
#   1. 當你需要從非 0 的索引開始計數時，例如從 1 開始編號，這在顯示給使用者看的清單或報告中特別有用。
#   2. 避免在迴圈內部手動調整索引值。
# 『結果』：
#   `enumerate(colors, 1)` 會產生一個迭代器，每次迭代會回傳一個元組 `(索引, 值)`，但索引會從 1 開始。
#   執行結果：
#   第1個: red
#   第2個: green
#   第3個: blue
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 核心概念：enumerate() 應用於檔案處理 (enumerate() with File Handling)
# `enumerate()` 函式非常適合用來處理檔案，因為檔案物件本身就是一個可迭代物件，會逐行迭代。
# 範例資料：
lines = ["line1", "line2", "line3"]
# 『語法』：`enumerate(檔案物件或模擬檔案的序列, start=起始行號)`
#   - 這裡 `lines` 是一個字串串列，模擬了從檔案中讀取到的每一行。
# 『用途』：
#   1. 讀取檔案時，同時取得每一行的內容和行號。
#   2. 在日誌處理、程式碼分析等場景中，標記出問題發生的行數，方便追蹤。
# 『結果』：
#   `enumerate(lines, 1)` 會走訪 `lines` 串列中的每一行，並為其加上從 1 開始的行號。
#   執行結果：
#   行 1: line1
#   行 2: line2
#   行 3: line3
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# 核心概念：zip() 基本用法 (Basic Usage of zip())
# `zip()` 函式會將多個「可迭代物件 (Iterable)」中對應位置的元素打包成一個個元組 (tuple)，然後回傳一個迭代器。它就像拉鍊一樣，將多個序列「拉」在一起。
# 範例資料：
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# 『語法』：`zip(可迭代物件1, 可迭代物件2, ...)`
#   - `可迭代物件`：任意數量的可迭代物件。
# 『用途』：
#   1. 將多個相關的序列資料「配對 (pair)」起來，方便同時處理。
#   2. 在需要同時迭代多個串列或元組時，簡化程式碼，避免使用索引。
# 『結果』：
#   `zip(names, scores)` 會產生一個迭代器，每次迭代會回傳一個元組 `(name, score)`。
#   執行結果：
#   Alice: 90
#   Bob: 85
#   Carol: 92
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# 核心概念：zip() 處理多個序列 (zip() with Multiple Sequences)
# `zip()` 不僅限於兩個序列，它可以同時處理任意數量的可迭代物件。
# 範例資料：
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# 『語法』：`zip(可迭代物件1, 可迭代物件2, 可迭代物件3, ...)`
# 『用途』：
#   1. 同時處理三個或更多相關的序列資料。
#   2. 進行多個序列的元素級聯運算，例如將多個串列的對應元素相加。
# 『結果』：
#   `zip(a, b, c)` 會產生一個迭代器，每次迭代會回傳一個元組 `(x, y, z)`，其中 `x` 來自 `a`，`y` 來自 `b`，`z` 來自 `c`。
#   執行結果：
#   1 + 10 + 100 = 111
#   2 + 20 + 200 = 222
#   3 + 30 + 300 = 333
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 核心概念：zip() 處理長度不同的序列 (zip() with Unequal Length Sequences)
# 當 `zip()` 處理長度不同的序列時，它會以「最短」的那個序列為準。一旦最短的序列被耗盡，`zip()` 就會停止，忽略較長序列中剩餘的元素。
# 範例資料：
x = [1, 2]
y = ["a", "b", "c"]
# 『語法』：`zip(短序列, 長序列)`
# 『用途』：
#   1. 當你只需要處理所有序列中「共同」的部分時。
#   2. 了解 `zip()` 的預設行為，避免在處理資料時意外遺失資訊。
# 『結果』：
#   `zip(x, y)` 會將 `x` 和 `y` 中的元素配對，但因為 `x` 只有兩個元素，所以 `y` 中的 `'c'` 會被忽略。
#   執行結果：
#   list(zip(x, y)): [(1, 'a'), (2, 'b')]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")
# 核心概念：zip_longest() 處理長度不同的序列 (補齊) (zip_longest() for Unequal Length Sequences with Padding)
# `itertools.zip_longest()` 函式可以處理長度不同的序列，它會用一個指定的 `fillvalue` (填充值) 來補齊較短的序列，直到所有序列都耗盡。
# 『語法』：`zip_longest(可迭代物件1, 可迭代物件2, ..., fillvalue=填充值)`
#   - `fillvalue`：當某個序列的元素已經用完時，用來填充的預設值。如果沒有指定 `fillvalue`，預設會使用 `None`。
# 『用途』：
#   1. 當你需要確保所有序列的元素都被處理到，即使它們長度不同。
#   2. 在合併資料時，需要對缺失值進行預設填充，以保持資料完整性。
# 『結果』：
#   `zip_longest(x, y, fillvalue=0)` 會將 `x` 和 `y` 中的元素配對。因為 `x` 較短，所以會用 `fillvalue=0` 來補齊 `x` 的第三個位置。
#   執行結果：
#   zip_longest: [(1, 'a'), (2, 'b'), (0, 'c')]

print("\n--- 建立字典 ---")
# 核心概念：使用 zip() 快速建立字典 (Creating Dictionary Quickly with zip())
# `zip()` 函式非常適合用來將兩個串列（一個作為鍵，一個作為值）快速組合成一個字典。
# 範例資料：
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# 『語法』：`dict(zip(鍵序列, 值序列))`
#   - `dict()` 函式：接受一個由 `(鍵, 值)` 元組組成的序列，並將其轉換為字典。`zip()` 的輸出正好符合這個格式。
# 『用途』：
#   1. 從兩個相關的串列中快速建立字典，例如從表頭和資料列建立字典。
#   2. 簡化字典的初始化過程，特別是當鍵和值已經分別存在於兩個串列中時。
# 『結果』：
#   `zip(keys, values)` 會產生 `('name', 'John')`, `('age', '30')`, `('city', 'NYC')` 這樣的元組序列，然後 `dict()` 函式會將其轉換為一個字典。
#   執行結果：
#   dict: {'name': 'John', 'age': '30', 'city': 'NYC'}
d = dict(zip(keys, values))
print(f"dict: {d}")
