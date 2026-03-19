# R19. 轉換+聚合：生成器表達式（1.19）

# 建立一個串列 nums
# 裡面放的是數字 1、2、3
nums = [1, 2, 3]

# 使用 sum() 搭配生成器表達式
# 會先把 nums 中的每個元素 x 逐一取出
# 再計算 x * x，也就是每個數字的平方
# 最後將所有平方值加總起來
sum_result = sum(x * x for x in nums)

# 印出原始串列 nums
print("原始數字串列 nums：", nums)

# 印出每個元素平方後再加總的結果
print("nums 中每個元素平方後的總和：", sum_result)

print()  # 空一行，讓輸出結果更清楚

# 建立一個 tuple（元組）s
# 元組中的資料型態可以不同
# 這裡包含字串、整數、浮點數
s = ('ACME', 50, 123.45)

# 使用 join() 搭配生成器表達式
# 由於 join() 只能串接字串，因此需要先用 str(x)
# 把元組中的每個元素都轉成字串
# 再用逗號 ',' 把它們連接成一個字串
join_result = ','.join(str(x) for x in s)

# 印出原始元組 s
print("原始元組 s：", s)

# 印出使用逗號連接後的字串結果
print("將元組中的元素轉成字串後，用逗號串接的結果：", join_result)

print()  # 空一行，讓輸出結果更清楚

# 建立一個串列 portfolio
# 串列中的每個元素都是字典(dict)
# 每個字典代表一筆股票資料
# name 表示股票名稱
# shares 表示持有股數
portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75}
]

# 使用 min() 搭配生成器表達式
# 從 portfolio 中逐一取出每個字典 s
# 再取出其中的 s['shares']
# 最後找出最小的 shares 數值
min_shares = min(s['shares'] for s in portfolio)

# 使用 min() 搭配 key 參數
# 這次不是只回傳最小的股數值
# 而是回傳「整筆 shares 最小的字典資料」
min_stock = min(portfolio, key=lambda s: s['shares'])

# 印出原始股票資料
print("原始股票資料 portfolio：")
print(portfolio)

print()  # 空一行，讓輸出結果更清楚

# 印出最小的 shares 數值
print("portfolio 中最小的 shares 數值：", min_shares)

# 印出 shares 最小的整筆股票資料
print("portfolio 中 shares 最小的整筆資料：", min_stock)