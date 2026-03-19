"""
U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

功能：演示當解包時變數與元素數量不匹配會發生什麼

核心概念：
  - 解包（Unpacking）：將序列中的元素賦值給多個變數
  - 失敗情況：變數個數 ≠ 序列元素個數
  - 錯誤類型：ValueError（值錯誤）

關鍵點：
  - Python 要求解包時必須精確匹配
  - 左邊變數數 = 右邊元素數
"""

p = (4, 5)
"""
定義一個元組：包含 2 個元素
  p = (4, 5)
  
元素計數：
  - 元素 1: 4
  - 元素 2: 5
  - 總計：2 個元素
"""

# x, y, z = p  # ValueError：元素只有 2 個但變數要 3 個
"""
為什麼這行會失敗？

嘗試操作：x, y, z = p

問題分析：
  1. 右邊（p）：2 個元素
     - 元素數 = 2
  
  2. 左邊（x, y, z）：3 個變數
     - 變數數 = 3
  
  3. 對比結果：2 ≠ 3
     → 數量不匹配！

錯誤發生的時刻：
  - Python 試圖將 p 的元素分配給 x, y, z
  - 分配到 x = 4
  - 分配到 y = 5
  - 現在還剩下一個變數 z，但已經沒有元素了
  - Python 拋出 ValueError

拋出的錯誤信息：
  ValueError: not enough values to unpack (expected 3, got 2)
  
  含義：
    - 期望 3 個值（3 個變數）
    - 但只得到 2 個值（2 個元素）
    - 不足的值無法分配！

解包的規則：

成功的解包 ✓
  x, y = (4, 5)
  → 2 個變數 = 2 個元素 ✓ 成功
  → x = 4, y = 5

失敗的解包案例：

情況1：變數太多
  x, y, z = (4, 5)
  → 3 個變數 > 2 個元素 ✗ 失敗
  → ValueError: not enough values to unpack (expected 3, got 2)

情況2：變數太少
  x, y = (4, 5, 6)
  → 2 個變數 < 3 個元素 ✗ 失敗
  → ValueError: too many values to unpack (expected 2)

情況3：解包列表（也會失敗）
  x, y, z = [4, 5]
  → 3 個變數 > 2 個元素 ✗ 失敗
  → ValueError: not enough values to unpack (expected 3, got 2)

情況4：解包字符串（字符計數）
  x, y, z = "ab"
  → 3 個變數 > 2 個字符 ✗ 失敗
  → ValueError: not enough values to unpack (expected 3, got 2)

為什麼 Python 會這樣設計？

好處1：防止數據丟失
  - 如果允許變數太少，會丟失元素
  - 明確要求匹配，保護數據完整性

好處2：防止邏輯錯誤
  - 預期 3 個變數卻只得 2 個，明顯是 bug
  - 馬上報錯，便於調試

好處3：代碼清晰
  - 檢查一下變數數和元素數是否匹配
  - 代碼意圖一目瞭然

如何修復？

方法1：調整變數數量（最常見）
  x, y = (4, 5)
  → 改為 2 個變數 ✓

方法2：調整元素數量
  p = (4, 5, 6)
  x, y, z = p
  → 改為 3 個元素 ✓

方法3：使用 * 進行靈活解包（1.8 章會講）
  x, *rest = (4, 5, 6)
  → x = 4, rest = [5, 6]
  → 允許不同數量 ✓

常見錯誤場景：

場景1：函數返回值數量錯估
  def get_coordinates():
      return (10, 20)  # 只返回 2 個值
  
  x, y, z = get_coordinates()  # 期望 3 個值
  → ValueError ✗

場景2：列表元素意外變化
  data = [1, 2]
  while len(data) < 3:
      data.append(0)
  
  x, y, z = data  # 現在有 3 個元素 ✓

場景3：API 響應格式改變
  # API 從返回 [name, age] 改為 [name, age, email]
  name, age = api.get_user()  # 原來的代碼
  → ValueError（元素數改變了） ✗

學習重點：

1. 解包必須數量匹配
   variable_count == element_count ✓

2. 常見錯誤類型
   - ValueError: not enough values to unpack
   - ValueError: too many values to unpack

3. 調試方法
   - 數一下左邊的變數個數
   - 數一下右邊的元素個數
   - 確保相等

4. 防禦性編程
   推薦：檢查序列長度
   assert len(p) == 3, f"期望 3 個元素，得到 {len(p)} 個"
   x, y, z = p

最佳實踐：

✓ 推薦做法
  # 明確表示期望 2 個值
  x, y = get_coordinates()
  
  # 使用類型提示（Python 3.5+）
  def unpack_pair(data: tuple) -> tuple:
      x, y = data
      return (x + 1, y + 1)

✗ 避免做法
  # 隻是希望有 2 個值？不清楚！
  x = data[0] if len(data) > 0 else None
  y = data[1] if len(data) > 1 else None
"""
