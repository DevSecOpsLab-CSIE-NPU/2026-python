# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 建立一個 tuple（元組）record
# 這筆資料中有 2 個元素：
# 第 1 個元素是姓名
# 第 2 個元素是電子郵件
record = ('Dave', 'dave@example.com')

# 使用解包（unpacking）將 record 中的資料分別取出
# name 會接收第 1 個元素
# email 會接收第 2 個元素
# *phones 代表「把剩下的所有元素都收集起來」
# 即使後面沒有剩下任何元素，phones 也不會出錯，
# 而是會得到一個空的 list
name, email, *phones = record

# phones == []  仍是 list

# 印出原始的 record
print("原始元組 record：", record)

print()  # 空一行，讓輸出結果更清楚

# 印出解包後的姓名
print("name 的值：", name)

# 印出解包後的電子郵件
print("email 的值：", email)

# 印出 phones 的值
# 因為 record 中除了 name 與 email 之外，後面已經沒有其他元素，
# 所以 phones 會是一個空的串列 []
print("phones 的值：", phones)

print()  # 空一行，讓輸出結果更清楚

# 驗證 phones 是否為空串列
print("phones 是否等於 []：", phones == [])

# 驗證 phones 的資料型態是否為 list
print("phones 的資料型態：", type(phones))

print()  # 空一行，讓輸出結果更清楚

# 說明星號解包的重要觀念
print("說明：使用 * 進行星號解包時，可以接收不固定數量的元素。")
print("即使沒有多餘元素，接收到的結果仍然會是 list，只是內容為空。")