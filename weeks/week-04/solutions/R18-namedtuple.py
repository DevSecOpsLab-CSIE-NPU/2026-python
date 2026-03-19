# R18. namedtuple（1.18）
# namedtuple 是 Python collections 模組中的一個工廠函數，用於創建具有命名字段的元組子類。
# 它允許通過名稱訪問元組的元素，而不是通過索引，使代碼更具可讀性。
# namedtuple 是不可變的，類似於元組，但提供了屬性訪問。

from collections import namedtuple  # 從 collections 模組導入 namedtuple 函數

# 創建一個名為 Subscriber 的 namedtuple，具有 'addr' 和 'joined' 兩個字段
# namedtuple 的第一個參數是類型名稱，第二個參數是字段名稱的列表
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 創建 Subscriber 的實例，傳入對應的字段值
# 這裡創建了一個訂閱者，地址為 'jonesy@example.com'，加入日期為 '2012-10-19'
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 訪問 namedtuple 實例的屬性，可以通過點號訪問字段
# 這裡訪問 sub 的 addr 屬性，返回 'jonesy@example.com'
sub.addr

# 創建一個名為 Stock 的 namedtuple，具有 'name', 'shares', 'price' 三個字段
# 用於表示股票信息：名稱、股數、價格
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 創建 Stock 的實例，傳入股票名稱 'ACME'、股數 100、價格 123.45
s = Stock('ACME', 100, 123.45)

# 使用 _replace 方法創建一個新的 namedtuple 實例，修改指定的字段
# 這裡將 shares 從 100 改為 75，其他字段保持不變
# 注意：namedtuple 是不可變的，所以 _replace 返回一個新實例
s = s._replace(shares=75)
