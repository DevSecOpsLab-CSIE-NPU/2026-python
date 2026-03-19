# R18. namedtuple（1.18）
# 此示例演示如何使用 namedtuple 建立具有命名欄位的輕量級不可變數據結構
# namedtuple 是一個工廠函數，用來建立具有命名欄位的元組子類

# 導入 namedtuple 函數，位於 collections 模組
from collections import namedtuple

# ===== 範例 1：訂閱者結構 =====
# 使用 namedtuple 建立 Subscriber 類
# namedtuple('類名', ['欄位1', '欄位2', ...])
# 返回一個新的類，該類是 tuple 的子類，具有命名欄位
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立 Subscriber 實例
# 可以像普通函數一樣呼叫，傳入各欄位的值
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
# 結果：Subscriber(addr='jonesy@example.com', joined='2012-10-19')

# 訪問 namedtuple 的欄位有兩種方式：
# 方式 1：使用點記號（推薦，更可讀）
sub.addr  # 結果：'jonesy@example.com'
print(sub.addr)
# 方式 2（未顯示但也支持）：使用索引記號
# sub[0]  # 結果：'jonesy@example.com'
# sub[1]  # 結果：'2012-10-19'

# ===== 範例 2：股票結構 =====
# 建立 Stock 類，包含股票名稱、股數和價格三個欄位
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立 Stock 實例
s = Stock('ACME', 100, 123.45)
# 結果：Stock(name='ACME', shares=100, price=123.45)

# namedtuple 是不可變的，無法直接修改其欄位
# 如需修改，使用 _replace() 方法返回一個新的實例（原實例保持不變）
s = s._replace(shares=75)
print(s)
# 結果：Stock(name='ACME', shares=75, price=123.45)
# 注意：_replace() 是 namedtuple 提供的特殊方法，傳入要修改的欄位

# ===== namedtuple 的優點 =====
# 1. 比字典（dict）內存效率更高
# 2. 比普通類簡潔，不需要定義 __init__ 和 __repr__
# 3. 提供 .name 的點記號訪問，比 dict['key'] 更可讀
# 4. 是不可變的，可以用作字典的鍵或集合的元素
# 5. 支持拆包返回多個值
