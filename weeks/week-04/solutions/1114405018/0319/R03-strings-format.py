"""
R03. 字串清理、對齊、拼接與格式化（2.11–2.16）

功能概述：
  - 2.11: 使用 strip/lstrip/rstrip 清理字符
  - 2.13: 使用 ljust/rjust/center/format 進行字串對齋
  - 2.14: 使用 str.join() 進行字串合併
  - 2.15: 使用 format/format_map/f-string 插入變量
  - 2.16: 使用 textwrap 模塊進行文本換行

核心方法：
  - strip() 系列：移除指定字符
  - align() 系列：對齋字符串
  - format() 系列：字符串格式化
  - textwrap：自動換行排版
"""

import textwrap
"""
textwrap 模塊：用於文本包裝和對齋
主要函數：
  - fill(): 自動換行填充
  - wrap(): 返回換行列表
  - dedent(): 移除前導空白
"""

# ════════════════════════════════════════════════════════
# 2.11 清理字元
# ════════════════════════════════════════════════════════

s = "  hello world \n"
"""
測試字符串：包含各種空白
內容分析：
  - 開頭兩個空格
  - 文本 "hello world"
  - 末尾一個空格
  - 末尾一個換行符 \n
"""

print(repr(s.strip()))  # 'hello world'
"""
strip() - 移除兩端指定字符

方法：str.strip([chars])

說明：
  - 默認移除兩端的空白（空格、製表符、換行符等）
  - 從字符串開始和結尾逐個移除指定字符
  - 直到遇到不是指定字符的字符為止
  - 返回新字符串（原字符串不變）

執行過程：
  s = "  hello world \n"
  
  1. 移除左端：
     - 第 1 個 ' ' → 移除
     - 第 2 個 ' ' → 移除
     - 'h' → 不是空白，停止移除
  
  2. 移除右端：
     - '\n' → 移除
     - ' ' → 移除
     - 'd' → 不是空白，停止移除

結果：'hello world'

repr() 的作用：
  - 顯示字符的精確表示（包括空白）
  - 不用 repr() 的話，看不出末尾換行符被移除沒
"""

print(repr(s.lstrip()))  # 'hello world \n'
"""
lstrip() - 只移除左端字符

方法：str.lstrip([chars])

說明：
  - l = left（左）
  - 只移除字符串左端的指定字符
  - 不影響右端

執行過程：
  s = "  hello world \n"
  
  1. 從左端移除空白：
     - 第 1 個 ' ' → 移除
     - 第 2 個 ' ' → 移除
     - 'h' → 停止移除
  
  2. 右端保持不變：' \n'（保留）

結果：'hello world \n'
"""

print("-----hello=====".strip("-="))  # 'hello'
"""
strip() with 自定義字符集

方法：str.strip(chars)

說明：
  - chars 參數：指定要移除的字符集
  - 不是移除子字符串，而是移除集合中的任何字符
  - 處理順序：從兩端逐個移除

執行過程：
  s = "-----hello====="
  chars = "-="（要移除的字符集）
  
  1. 移除左端：
     - '-' (5 個) → 都在 "-=" 中，移除
     - 'h' → 不在 "-=" 中，停止
  
  2. 移除右端：
     - '=' (5 個) → 都在 "-=" 中，移除
     - 'o' → 不在 "-=" 中，停止

結果：'hello'

其他方法：
  lstrip(chars)：只移除左端 → "-----hello====="
  rstrip(chars)：只移除右端 → "-----hello"
"""

# ════════════════════════════════════════════════════════
# 2.13 字串對齋
# ════════════════════════════════════════════════════════

text = "Hello World"
"""
測試字符串：11 個字符
用於演示各種對齋方式
"""

print(text.ljust(20))  # 'Hello World         '
"""
ljust() - 左對齋，右側填充

方法：str.ljust(width, fillchar=' ')

參數說明：
  - width: 目標寬度
  - fillchar: 填充字符（默認空格）

執行過程：
  text = "Hello World"（11 個字符）
  目標寬度：20
  所需填充：20 - 11 = 9 個空格
  
  結果：'Hello World         '（9 個尾隨空格）

說明：
  - 字符串向左對齋
  - 右側填充到指定寬度
  - 原字符串長度 ≥ 寬度時，返回原字符串
"""

print(text.rjust(20))  # '         Hello World'
"""
rjust() - 右對齋，左側填充

方法：str.rjust(width, fillchar=' ')

說明：
  - r = right（右）
  - 字符串向右對齋
  - 左側填充到指定寬度

執行過程：
  text = "Hello World"
  目標寬度：20
  所需填充：9 個空格
  
  結果：'         Hello World'（9 個前導空格）
"""

print(text.center(20, "*"))  # '****Hello World*****'
"""
center() - 居中，兩側填充

方法：str.center(width, fillchar=' ')

說明：
  - 字符串居中
  - 兩側均勻填充指定字符
  - 如果無法均勻分配，左側多填充一個

執行過程：
  text = "Hello World"（11 個字符）
  目標寬度：20
  總填充：20 - 11 = 9 個字符
  左側：9 // 2 = 4 個 *
  右側：9 - 4 = 5 個 *
  
  結果：'****Hello World*****'
"""

print(format(text, "^20"))  # '    Hello World     '
"""
format() - 通用格式化函數（居中）

方法：format(value, format_spec)

格式字符串解析："^20"
  - ^ 表示居中
  - 20 表示寬度
  - 默認填充字符是空格

執行過程：
  format(text, "^20")
  → 居中對齋，寬度 20，空格填充
  
  結果：'    Hello World     '
"""

print(format(1.2345, ">10.2f"))  # '      1.23'
"""
format() - 高級格式化（數字）

方法：format(value, format_spec)

格式字符串解析：">10.2f"
  - > 表示右對齋
  - 10 表示寬度
  - .2 表示 2 位小數
  - f 表示浮點數格式

執行過程：
  format(1.2345, ">10.2f")
  
  1. 格式化浮點數 1.2345
     - .2f → 四捨五入到 2 位小數
     - 結果：1.23
  
  2. 右對齋，寬度 10
     - 字符串 "1.23"（4 個字符）
     - 需要填充：10 - 4 = 6 個空格
     - 左邊填充：'      1.23'
  
  結果：'      1.23'
"""

# ════════════════════════════════════════════════════════
# 2.14 合併拼接
# ════════════════════════════════════════════════════════

parts = ["Is", "Chicago", "Not", "Chicago?"]
"""
測試列表：多個字符串元素
用於演示不同的連接方式
"""

print(" ".join(parts))  # 'Is Chicago Not Chicago?'
"""
str.join() - 用分隔符連接字符串列表

方法：separator.join(iterable)

說明：
  - separator 是分隔符（這裡是空格）
  - iterable 是可迭代序列（通常是列表）
  - 返回連接後的字符串

執行過程：
  separator = " "
  parts = ["Is", "Chicago", "Not", "Chicago?"]
  
  1. 取第一個元素："Is"
  2. 插入分隔符 " "
  3. 取第二個元素："Chicago"
  4. 插入分隔符 " "
  5. 取第三個元素："Not"
  6. 插入分隔符 " "
  7. 取第四個元素："Chicago?"
  
  結果：'Is Chicago Not Chicago?'

性能優勢：
  ✗ 不推薦：多次 + 拼接（低效）
  ✓ 推薦：join() 一次拼接（高效）✓
"""

print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'
"""
join() - 使用逗號分隔

執行結果：'Is,Chicago,Not,Chicago?'

說明：
  - 只改變分隔符
  - 常用於生成 CSV 格式
"""

data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'
"""
join() with 生成器表達式 - 混合類型連接

說明：
  data 包含不同類型：字符串、整數、浮點數
  → str.join() 要求所有元素必須是字符串
  → 使用生成器表達式轉換

執行過程：
  1. str(d) for d in data 生成字符串序列
     - str("ACME") → "ACME"
     - str(50) → "50"
     - str(91.1) → "91.1"
  
  2. ",".join(...) 用逗號連接
     結果：'ACME,50,91.1'

優勢：
  - 邊轉換邊連接，內存占用少 ✓
  - vs 列表推導：先創建臨時列表，占用額外內存
"""

# ════════════════════════════════════════════════════════
# 2.15 插入變量
# ════════════════════════════════════════════════════════

name, n = "Guido", 37
s = "{name} has {n} messages."
"""
準備變量：
  - name = "Guido"
  - n = 37
  - template = "{name} has {n} messages."
"""

print(s.format(name=name, n=n))  # 'Guido has 37 messages.'
"""
format() - 使用關鍵字參數格式化

方法：template.format(**kwargs)

說明：
  - template 包含佔位符 {name} 和 {n}
  - format() 用提供的參數替換佔位符

執行過程：
  s = "{name} has {n} messages."
  
  1. 找到佔位符 {name}
     → 用 name="Guido" 替換
  
  2. 找到佔位符 {n}
     → 用 n=37 替換
  
  結果：'Guido has 37 messages.'

推薦：使用關鍵字參數，代碼更易讀
"""

print(s.format_map(vars()))  # 'Guido has 37 messages.'
"""
format_map() - 使用字典映射格式化

方法：template.format_map(mapping)

說明：
  - format_map() 接收一個字典或類字典對象
  - vars() 返回當前作用域的所有變數字典

vars() 的作用：
  - 無參數時：返回當前作用域的局部變量字典
  - vars() 返回：{'name': 'Guido', 'n': 37, ...}

執行過程：
  1. 找到佔位符 {name}
     → 在字典中查找 'name' → 'Guido'
  
  2. 找到佔位符 {n}
     → 在字典中查找 'n' → 37

format() vs format_map() 的區別：

format(name=name, n=n)：
  - 立即評估所有參數
  - 所有參數必須在調用時提供

format_map(vars())：
  - 延遲查詢（需要時才查字典）
  - 更靈活（可以使用局部變量）
"""

print(f"{name} has {n} messages.")  # f-string（最簡潔）
"""
f-string - Python 3.6+ 推薦方式

語法：f"..." 或 f'...'

說明：
  - f-string（formatted string literal）
  - 直接在字符串中嵌入表達式
  - 用 {} 包含表達式

執行過程：
  f"{name} has {n} messages."
  
  1. 解析 {name}
     → 評估變量 name → "Guido"
  
  2. 解析 {n}
     → 評估變量 n → 37
  
  結果：'Guido has 37 messages.'

f-string 的優勢：

簡潔性：
  format() 版本："{name} has {n} messages".format(name=name, n=n)
  f-string：f"{name} has {n} messages"
  → f-string 更簡潔 ✓

表達式支持：
  f-string 可以包含任何 Python 表達式
  f"{name} has {n*2} messages"  # 支持表達式
  → format() 無法直接在佔位符中計算

性能：
  - f-string 編譯時優化
  - f-string 更快 ✓

推薦：Python 3.6+ 優先使用 f-string ✓✓✓
"""

# ════════════════════════════════════════════════════════
# 2.16 指定列寬 (textwrap)
# ════════════════════════════════════════════════════════

long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
"""
長字符串：76 個字符
用於演示文本換行
"""

print(textwrap.fill(long_s, 40))
"""
textwrap.fill() - 自動換行填充

方法：textwrap.fill(text, width, ...)

參數說明：
  - text: 要換行的文本
  - width: 每行的最大寬度

說明：
  - 將長文本按指定寬度自動換行
  - 優先保持單詞完整（不會在單詞中斷行）
  - 返回多行字符串

執行過程：
  long_s（76 個字符）
  width = 40
  
  1. 第一行：
     "Look into my eyes, look into my" ✗ 超過 40
     "Look into my eyes, look into" → 30 字符 ✓
  
  2. 第二行：
     "my eyes, the eyes, not around " → 31 字符 ✓
  
  3. 第三行：
     "the eyes, look into my eyes," → 28 字符 ✓
  
  4. 第四行：
     "you're under." → 13 字符 ✓

算法特點：
  - 按空格分割單詞
  - 每行盡量填充到接近指定寬度
  - 優先保持完整單詞 ✓

輸出範例：
  Look into my eyes, look into my
  eyes, the eyes, not around the
  eyes, look into my eyes, you're
  under.
"""

print(textwrap.fill(long_s, 40, initial_indent="    "))
"""
textwrap.fill() with initial_indent - 首行縮進

額外參數：
  - initial_indent: 首行前綴
  - subsequent_indent: 後續行前綴

執行過程：
  long_s
  width = 40
  initial_indent = "    "（4 個空格）
  
  1. 第一行添加縮進（4 個空格）：
     "    Look into my eyes, look into"
  
  2. 後續行無縮進：
     "my eyes, the eyes, not around the"
     ...

應用場景：
  - 縮進代碼塊
  - 段落首行縮進
  - 列表項目縮進

進階參數：

break_long_words：
  - True: 必須時在單詞中斷
  - False: 寧願超長也不破壞單詞（默認）✓

replace_whitespace：
  - True:（默認）用一個空格替換所有空白
  - False: 保留原始空白格式

應用場景：
  - 格式化幫助文本
  - 打印多行輸出
  - 代碼生成（縮進）
  - 報告排版
"""
