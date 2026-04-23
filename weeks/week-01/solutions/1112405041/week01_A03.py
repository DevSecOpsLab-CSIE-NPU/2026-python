# 【Bloom 階段：R - 記憶與基本操作】
# 3 基本容器型別範例
# August 的惡意提醒：Week 02 的核心是這三種容器。
# 記住：List 保序且可變，Tuple 保序但不可變，Set 不保序且唯一，Dict 鍵值配對。
# 搞錯 Set 的保序性（如 Week 02 Task 1）會導致 0 分。

# 建立一個列表 (List)，這是一個可變的序列
numbers = [1, 2, 3]

# 建立一個元組 (Tuple)，這是一個不可變的序列，常用於座標或固定不變的資料
point = (4, 5)

# 建立一個集合 (Set)，自動去重，適合用來判斷「是否出現過」
unique = {1, 2, 3}

# 建立一個字典 (Dictionary)，存儲鍵值對 (Key-Value)
prices = {'AAPL': 150.0, 'MSFT': 320.5}

# 基本存取
numbers.append(4)     # 修改列表
first = point[0]      # 讀取元組 (不可 numbers[0] = 99)
apple_price = prices['AAPL'] # 字典查詢，時間複雜度 O(1)

print(f"List: {numbers}, Dict: {prices}")
