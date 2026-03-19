# R18. namedtuple（1.18）

# 從 collections 模組匯入 namedtuple
# namedtuple 可以建立「具名欄位的 tuple」
# 讓 tuple 不只是用索引存取，也可以用名稱存取（可讀性更高）
from collections import namedtuple

# 建立一個名為 Subscriber 的 namedtuple 類別
# 包含兩個欄位：
# addr：電子郵件地址
# joined：加入日期
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立一個 Subscriber 物件 sub
# 傳入對應欄位的值（順序需與定義一致）
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 透過「屬性名稱」取得資料（比用索引更直觀）
sub.addr

# 印出 Subscriber 物件
print("Subscriber 物件 sub：")
print(sub)

# 印出 addr 欄位（使用名稱存取）
print("sub.addr（電子郵件）：", sub.addr)

# 印出 joined 欄位
print("sub.joined（加入日期）：", sub.joined)

print()  # 空一行，讓輸出結果更清楚

# 建立另一個 namedtuple 類別 Stock
# 包含三個欄位：
# name：股票名稱
# shares：持有股數
# price：價格
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立一個 Stock 物件 s
s = Stock('ACME', 100, 123.45)

# 印出原始的 Stock 物件
print("原始的 Stock 物件 s：")
print(s)

# namedtuple 是「不可變（immutable）」的
# 無法直接修改欄位值
# 需要使用 _replace() 方法來建立一個「新的物件」
# 這裡將 shares 從 100 改成 75
s = s._replace(shares=75)

# 印出修改後的 Stock 物件
print("使用 _replace() 修改 shares 後的 s：")
print(s)

# 分別印出各欄位內容（使用名稱存取）
print("s.name（股票名稱）：", s.name)
print("s.shares（股數）：", s.shares)
print("s.price（價格）：", s.price)