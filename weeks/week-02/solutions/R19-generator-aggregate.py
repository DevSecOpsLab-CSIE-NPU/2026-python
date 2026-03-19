# R19. 轉換+聚合：生成器表達式（1.19）
# 生成器表達式（Generator Expressions）是一種記憶體高效的迭代器，
# 類似於列表推導式，但不會立即創建整個列表。
# 在處理大型資料或鏈式操作時特別有用。

# 創建一個數值列表
nums = [1, 2, 3]

# 使用生成器表達式計算平方和
# 生成器表達式使用圓括號 () 而不是方括號 []
# 它返回一個生成器物件，而不是列表
sum_of_squares = sum(x * x for x in nums)

# 創建一個包含不同型別元素的元組
s = ('ACME', 50, 123.45)

# 使用生成器表達式將所有元素轉換為字串，然後用逗號連接
# str(x) 將每個元素轉換為字串
# ','.join() 使用逗號將字串連接起來
joined_string = ','.join(str(x) for x in s)

# 創建一個投資組合列表，每個元素是一個字典
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 使用生成器表達式找到股份數最少的股票
# min() 函數接受一個生成器表達式作為參數
# key 參數指定比較的依據
min_shares = min(s['shares'] for s in portfolio)

# 也可以直接使用 min() 函數，傳入整個列表和 key 函數
# 這種方式更直觀，但對於大型資料集，生成器表達式更高效
min_shares_alt = min(portfolio, key=lambda s: s['shares'])

# 生成器表達式的優勢：
# 1. 記憶體高效：不會創建中間列表
# 2. 適合鏈式操作
# 3. 可以處理無限序列（理論上）

# 例如，計算檔案中的行數（如果檔案很大）
# line_count = sum(1 for line in open('large_file.txt'))

# 或者過濾和轉換的組合
# result = sum(x**2 for x in nums if x > 0)
