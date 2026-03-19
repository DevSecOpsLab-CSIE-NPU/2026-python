"""
R18. namedtuple（1.18）

功能：創建具有命名字段的輕量級不可變對象
本質：是普通元組的升級版，提供字段名訪問
場景：數據記錄、API 響應、配置對象等
優點：內存占用少，性能高，代碼可讀性好
"""

from collections import namedtuple
"""
namedtuple 是 Python 內置的重要工具類

說明：
  - 由 collections 模塊提供
  - 用於創建有命名字段的不可變序列類型
  - 結合了元組的效率和類的可讀性
"""

# ════════════════════════════════════════════════════════
# 示例1：創建 Subscriber（訂閱者）對象
# ════════════════════════════════════════════════════════

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
"""
namedtuple 定義語法：namedtuple(typename, fieldnames)

參數說明：
  - 'Subscriber': 類的名稱（用於repr和type）
  - ['addr', 'joined']: 字段名列表（也可以是空格/逗號分隔的字符串）
  
返回值：
  - 返回一個新的類（不是對象）
  - Subscriber 現在是一個類，可以用來創建對象
  
字段定義等價形式：
  Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
  Subscriber = namedtuple('Subscriber', 'addr joined')
  Subscriber = namedtuple('Subscriber', 'addr, joined')
  （三種形式結果相同）

重要特性：
  1. 不可變：創建後無法修改字段值
  2. 輕量級：占用內存少，性能高
  3. 像元組：支持索引、迭代等元組操作
  4. 像類：支持命名字段訪問
"""

sub = Subscriber('jonesy@example.com', '2012-10-19')
"""
創建 Subscriber 實例

語法：ClassName(field1, field2, ...)

說明：
  - 傳入位置參數，依次對應各字段
  - Subscriber('jonesy@example.com', '2012-10-19')
  - → addr = 'jonesy@example.com'
  - → joined = '2012-10-19'

創建結果：
  sub = Subscriber(addr='jonesy@example.com', joined='2012-10-19')
  
repr 表示：
  str(sub) = "Subscriber(addr='jonesy@example.com', joined='2012-10-19')"
"""

sub.addr
"""
訪問命名字段

方法1：使用屬性訪問（推薦）
  sub.addr = 'jonesy@example.com'
  sub.joined = '2012-10-19'
  
方法2：使用索引訪問（像元組）
  sub[0] = 'jonesy@example.com'
  sub[1] = '2012-10-19'

說明：
  - 屬性訪問（sub.addr）比索引訪問更可讀
  - 索引訪問保持了元組的特性
  - 兩種方式都支持
"""


# ════════════════════════════════════════════════════════
# 示例2：使用 _replace() 方法修改字段
# ════════════════════════════════════════════════════════

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
"""
創建 Stock（股票）namedtuple 類

字段說明：
  - name: 股票代碼
  - shares: 持股數量
  - price: 股票價格
"""

s = Stock('ACME', 100, 123.45)
"""
創建股票對象

內容：
  - name = 'ACME'
  - shares = 100
  - price = 123.45
"""

s = s._replace(shares=75)
"""
使用 _replace() 方法修改字段值

namedtuple 提供的方法：
  _replace(**kwargs) - 返回一個新的對象，指定字段被替換
  
執行過程：
  1. 原對象 s: Stock(name='ACME', shares=100, price=123.45)
  2. 調用 s._replace(shares=75)
  3. 返回新對象：Stock(name='ACME', shares=75, price=123.45)
  4. 原對象 s 保持不變
  5. 將新對象賦值給 s

重要特性：
  - namedtuple 是不可變的，無法直接修改字段
  - _replace() 創建新對象而不是修改原對象
  - 這種設計確保了數據的安全性和一致性

與普通對象的區別：
  普通類：obj.shares = 75 (直接修改)
  namedtuple：s = s._replace(shares=75) (返回新對象)

示例對比：
  # 不可能～無法直接賦值
  # s.shares = 75 → AttributeError
  
  # 正確方式～創建新對象
  s = s._replace(shares=75)
"""


# ════════════════════════════════════════════════════════
# namedtuple 的常用方法
# ════════════════════════════════════════════════════════

"""
namedtuple 除了 _replace() 外，還提供其他有用的方法：

1. _asdict() - 轉換為字典
   s._asdict() = OrderedDict([('name', 'ACME'), ('shares', 75), ('price', 123.45)])
   
   用途：
   - 序列化為 JSON
   - 與字典相關的操作
   - 數據轉換

2. _fields - 查看所有字段名
   Stock._fields = ('name', 'shares', 'price')
   
   用途：
   - 動態訪問字段名
   - 通用處理 namedtuple

3. _make(iterable) - 從可迭代對象創建實例
   Stock._make(['ACME', 100, 123.45])
   = Stock(name='ACME', shares=100, price=123.45)
   
   用途：
   - 從列表或元組創建對象
   - 批量創建對象

4. 訪問方式總結
   - sub.addr          # 屬性訪問
   - sub[0]            # 索引訪問（元組風格）
   - sub._asdict()     # 轉換為字典
   - Stock._fields     # 查看字段名
"""


# ════════════════════════════════════════════════════════
# namedtuple vs 普通類 vs 字典
# ════════════════════════════════════════════════════════

"""
使用場景對比：

1. namedtuple - 推薦用於 ✓
   ✓ 簡單的數據結構
   ✓ 不需要方法的對象
   ✓ 需要不可變性的場景
   ✓ 性能要求高、內存占用少
   ✗ 需要複雜的邏輯

示例應用：
   - 二維坐標：Point = namedtuple('Point', ['x', 'y'])
   - 數據庫記錄：Row = namedtuple('Row', ['id', 'name', 'date'])
   - API 結果：User = namedtuple('User', ['id', 'email', 'name'])
   - 配置對象：Config = namedtuple('Config', ['host', 'port', 'debug'])

2. 普通類（class）- 推薦用於 ✓
   ✓ 複雜的業務邏輯
   ✓ 需要方法和操作
   ✓ 需要可變的對象
   ✗ 簡單數據結構（過度設計）

3. 字典 - 推薦用於 ✓
   ✓ 動態字段（運行時決定）
   ✓ 需要靈活性
   ✓ 字段數量不確定
   ✗ 性能要求高時不推薦

典型對比：
  # 字典方式（可變，靈活但不夠類型安全）
  sub = {'addr': 'jonesy@example.com', 'joined': '2012-10-19'}
  
  # namedtuple 方式（不可變，高效，類型安全，可讀性好）
  sub = Subscriber('jonesy@example.com', '2012-10-19')
  
  # 普通類方式（可變，功能豐富但冗長）
  class Subscriber:
      def __init__(self, addr, joined):
          self.addr = addr
          self.joined = joined
"""


# ════════════════════════════════════════════════════════
# 實踐建議
# ════════════════════════════════════════════════════════

"""
最佳實踐：

1. 命名約定
   - 類名使用大寫開頭（SubscriberInfo, User, Point）
   - 字段名使用小寫（addr, joined, name）

2. 字段名定義
   - 使用有意義的名稱，避免單字母
   - 使用 'email' 而非 'e'
   - 使用 'joined_date' 而非 'jd'

3. 文檔化
   __doc__ = 'Represents a subscriber record'
   
   或使用類型註解（Python 3.6+）
   from typing import NamedTuple
   class Subscriber(NamedTuple):
       addr: str
       joined: str

4. 大數據量時的性能優勢
   - namedtuple 比字典快 20-30%
   - 內存占用大約只有字典的 1/3
   - 對於百萬級數據量效果明顯
"""
