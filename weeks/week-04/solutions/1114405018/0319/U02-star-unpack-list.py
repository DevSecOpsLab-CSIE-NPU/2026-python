"""
U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

功能：展示 * 星號解包的核心特性

核心概念：
  - * 解包：「蒼捕」未指定的所有元素
  - 結果類型固定：總是 list，無論輸入是什麼
  - 靈活應對不同長度的序列

關鍵特徵：
  1. 可以接收 0 個或多個元素 ✓
  2. 無需提前知道序列有多少元素
  3. 結果總是列表（即使是 0 個元素）
  4. 只能在解包中出現一次星號
"""

record = ('Dave', 'dave@example.com')
"""
定義一個元組：包含 2 個元素
  record = ('Dave', 'dave@example.com')
  
元素列表：
  - 元素 0: 'Dave'（名稱）
  - 元素 1: 'dave@example.com'（郵箱）
  - 總計：2 個元素

場景說明：
  記錄可能包含：姓名、郵箱、以及可能的電話號碼
  但這個記錄中沒有電話號碼
"""

name, email, *phones = record
"""
使用星號解包處理不定長序列

解包語法分析：name, email, *phones = record

參與者：
  - name：接收第 1 個元素
  - email：接收第 2 個元素
  - *phones：接收其餘所有元素
  - record：有 2 個元素的元組

執行過程：
  1. Python 從左到右分配：
     - name 得到 record[0] = 'Dave'
     - email 得到 record[1] = 'dave@example.com'
  
  2. 星號的作用：
     - *phones 捕獲剩餘的所有元素
     - 剩餘元素 = record[2:] = []（空）
     - 注意：結果是列表，不是元組！ ✓
  
  3. 最終結果：
     - name = 'Dave'（字符串）
     - email = 'dave@example.com'（字符串）
     - phones = []（空列表）

關鍵點：phones == []（空列表而非空元組）

為什麼結果是 list 而不是 tuple？

Python 設計決定：
  - * 解包的結果 ALWAYS 是 list
  - 不管輸入是什麼類型（list、tuple、str 等）
  - 這確保一致性和可預測性

示例對比：

情況1：輸入是元組
  name, *rest = ('A', 'B', 'C')
  → rest = ['B', 'C']（列表，不是元組）

情況2：輸入是列表
  name, *rest = ['A', 'B', 'C']
  → rest = ['B', 'C']（仍是列表）

情況3：輸入是字符串
  first, *rest = 'ABC'
  → rest = ['B', 'C']（列表）

情況4：無剩餘元素
  a, b, *rest = (1, 2)
  → rest = []（空列表，不是空元組）✓
  → 這正是當前示例！

星號解包的工作原理：

1. 普通變數（固定位置）
   name, email, *phones = record
   ↑      ↑      ↑
   第1個  第2個  其餘

2. 順序很重要
   - 星號必須被第一個固定變數「滿足」後
   - 剩下的都歸星號變數

3. 只能一個星號
   x, *y, *z = [1,2,3,4]  # SyntaxError! ✗
   → 不能有多個星號

多個星號的正確用法（在 Python 3 中）：
   x, *middle, z = [1, 2, 3, 4, 5]
   → x = 1
   → middle = [2, 3, 4]（星號在中間！）
   → z = 5

星號解包 vs 普通解包：

普通解包（必須精確匹配）：
  x, y, z = [1, 2, 3]  # ✓ 成功（3 個變數 = 3 個元素）
  x, y, z = [1, 2]     # ✗ 失敗（3 個變數 > 2 個元素）

星號解包（靈活適應）：
  x, y, *z = [1, 2]    # ✓ 成功（z = []）
  x, y, *z = [1, 2, 3] # ✓ 成功（z = [3]）
  x, y, *z = [1]       # ✗ 失敗（x 和 y 無法都得到值）

星號解包的常見用途：

用途1：跳過中間的值
  first, *_, last = [1, 2, 3, 4, 5]
  → first = 1
  → _ = [2, 3, 4]（約定：_ 表示不關心）
  → last = 5

用途2：處理可選參數
  user_data = ('Alice', 'admin@example.com', '+1234567890', '+9876543210')
  
  name, email, *phones = user_data
  → name = 'Alice'
  → email = 'admin@example.com'
  → phones = ['+1234567890', '+9876543210']
  
  之後可以這樣檢查：
  if phones:
      print(f"聯絡電話：{', '.join(phones)}")

用途3：分離頭尾
  *head, tail = [1, 2, 3, 4, 5]
  → head = [1, 2, 3, 4]
  → tail = 5

用途4：函數參數收集
  def print_items(first, *rest):
      print(f"第一項：{first}")
      if rest:
          print(f"其餘項：{rest}")
  
  print_items('A', 'B', 'C')
  → 第一項：A
  → 其餘項：('B', 'C')

重要區別：函數參數 vs 解包

函數 *args：
  def func(*args):
      pass
  func(1, 2, 3)  # args = (1, 2, 3)（元組）

解包 *rest：
  a, *rest = (1, 2, 3)  # rest = [2, 3]（列表）

為什麼有區別？
  - 函數 *args 歷史上就是元組
  - 解包 * 為了返回一致類型而使用列表
  - 設計不同，目的也不同

邊界情況處理：

情況1：星號獲得 0 個元素（當前示例）
  name, email, *phones = ('Dave', 'dave@example.com')
  → phones = []（空列表）✓

情況2：星號獲得所有元素
  first, *rest = [1]
  → first = 1
  → rest = []（無剩餘）

情況3：星號只能匹配必要的元素
  a, *b, c = [1, 2, 3, 4]
  → a = 1（第一個）
  → b = [2, 3]（中間的）
  → c = 4（最後一個）
  
  a, *b, c, d = [1, 2]
  → 失敗！✗ 無法同時滿足 a、b、c、d
  → ValueError: not enough values to unpack

最佳實踐：

✓ 推薦做法
  # 明確表示期望的結構
  name, email, *phones = record
  
  # 使用 _ 表示不關心的值
  first, *_, last = sequence
  
  # 檢查前再使用
  if phones:
      send_sms(phones)

✗ 避免做法
  # 不清楚 * 會得到什麼
  a, *b, *c = data
  # SyntaxError: multiple starred expressions!

✗ 易出錯的做法
  # 期望 b 是元組，但實際是列表
  x, *b = [1, 2, 3]
  print(type(b))  # <class 'list'> 而非 tuple!

除錯技巧：

技巧1：檢查星號變數的內容
  name, email, *phones = record
  print(f"phones 的內容：{phones}")
  print(f"phones 的類型：{type(phones)}")
  print(f"phones 的長度：{len(phones)}")

技巧2：使用 len() 驗證
  name, email, *phones = record
  assert len(phones) >= 0, "星號解包總是產生列表"

技巧3：利用列表特性
  name, email, *phones = record
  
  # 安全地訪問
  first_phone = phones[0] if phones else None
  
  # 或者使用迭代
  for phone in phones:
      print(f"電話：{phone}")

相關主題預告：

- 1.3：不定位置的星號解包（中間的星號）
- 1.4：雙星號 ** 在字典中的用法
- 2.1：*args 和 **kwargs 在函數定義中的應用
"""
