# ============================================================================
# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# ============================================================================
# 本題展示五個重要的字串處理技巧：
# 1. strip() / lstrip() / rstrip() - 清理字符串頭尾的多餘字元
# 2. ljust() / rjust() / center() - 字串對齐和填充
# 3. join() - 高效地合並多個字串
# 4. format() / format_map() - 格式化和插入變量
# 5. textwrap.fill() - 自動換行處理長文本
# ============================================================================

import textwrap


# ── 2.11 清理字元（String Cleaning） ──────────────────────────────────────
print("【2.11 清理字元】")
print("-" * 50)

# 原始字符串：包含頭尾空白和換行符
s = "  hello world \n"
print(f"原始字符串（repr）: {repr(s)}\n")

# 【方法 1】strip() - 移除頭尾的空白和換行符
print("【方法 1】strip() - 移除頭尾空白")
stripped = s.strip()
print(f"s.strip() = {repr(stripped)}")  # 'hello world'（頭尾空白都去除）
print()

# 【方法 2】lstrip() - 只移除左邊（開頭）的空白
print("【方法 2】lstrip() - 只移除左邊空白")
lstripped = s.lstrip()
print(f"s.lstrip() = {repr(lstripped)}")  # 'hello world \n'（只去除左邊空白）
print()

# 【方法 3】自訂要移除的字符集合
print("【方法 3】自訂移除字符集")
s2 = "-----hello====="
cleaned = s2.strip("-=")
print(f"'-----hello====='strip('-=') = {repr(cleaned)}")  # 'hello'（移除 - 和 =）
print()


# ── 2.13 字串對齐（String Alignment） ──────────────────────────────────────
print("【2.13 字串對齐】")
print("-" * 50)

# 原始字符串
text = "Hello World"
print(f"原始字符串: '{text}'（長度 11）\n")

# 【方法 1】ljust(width) - 左對齐，用空白填充至指定寬度
print("【方法 1】ljust(width) - 左對齐")
left_aligned = text.ljust(20)
print(f"text.ljust(20) = '{left_aligned}|'")  # 'Hello World         |'（右邊補空白）
print()

# 【方法 2】rjust(width) - 右對齐，用空白填充至指定寬度
print("【方法 2】rjust(width) - 右對齐")
right_aligned = text.rjust(20)
print(f"text.rjust(20) = '|{right_aligned}'")  # '|         Hello World'（左邊補空白）
print()

# 【方法 3】center(width, fillchar) - 居中對齐，用指定字符填充
print("【方法 3】center(width, fillchar) - 居中")
centered = text.center(20, "*")
print(f"text.center(20, '*') = '{centered}'")  # '****Hello World*****'
print()

# 【方法 4】使用 format() 進行對齐
print("【方法 4】使用 format() - 更靈活的對齐")
# 格式說明：^20 表示置中、寬度 20；>10.2f 表示右對齐、寬度 10、小數 2 位
centered_format = format(text, "^20")
print(f"format(text, '^20') = '{centered_format}'")  # '    Hello World     '

# 數字格式化（右對齐，寬度 10，保留 2 位小數）
num_formatted = format(1.2345, ">10.2f")
print(f"format(1.2345, '>10.2f') = '{num_formatted}'")  # '      1.23'
print()


# ── 2.14 合併拼接（String Joining） ───────────────────────────────────────
print("【2.14 合併拼接】")
print("-" * 50)

# 原始列表
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(f"列表: {parts}\n")

# 【方法 1】用空白拼接
print("【方法 1】用空白拼接")
space_joined = " ".join(parts)
print(f"' '.join(parts) = '{space_joined}'")  # 'Is Chicago Not Chicago?'
print()

# 【方法 2】用逗號拼接
print("【方法 2】用逗號拼接")
comma_joined = ",".join(parts)
print(f"','.join(parts) = '{comma_joined}'")  # 'Is,Chicago,Not,Chicago?'
print()

# 【方法 3】混合型別資料需先轉成字符串
print("【方法 3】混合型別資料")
data = ["ACME", 50, 91.1]
print(f"資料: {data}")
# join() 只接受字符串，需用生成器表達式轉換
mixed_joined = ",".join(str(d) for d in data)
print(f"','.join(str(d) for d in data) = '{mixed_joined}'")  # 'ACME,50,91.1'
print()


# ── 2.15 插入變量（String Formatting） ───────────────────────────────────
print("【2.15 插入變量】")
print("-" * 50)

# 定義變量
name, n = "Guido", 37
print(f"變量: name='{name}', n={n}\n")

# 模板字符串
s = "{name} has {n} messages."
print(f"模板: '{s}'\n")

# 【方法 1】format(name=..., n=...) - 按名稱傳入參數
print("【方法 1】format(name=..., n=...)")
result1 = s.format(name=name, n=n)
print(f"結果: '{result1}'")  # 'Guido has 37 messages.'
print()

# 【方法 2】format_map(vars()) - 從本地變量字典取值
print("【方法 2】format_map(vars())")
result2 = s.format_map(vars())
print(f"結果: '{result2}'")  # 'Guido has 37 messages.'
# vars() 返回當前局部變量的字典，非常方便
print()

# 【方法 3】f-string（f"..."） - 最現代和簡潔的方式
print("【方法 3】f-string（推薦）")
result3 = f"{name} has {n} messages."
print(f"結果: '{result3}'")  # 'Guido has 37 messages.'
# f-string 支援完整的 Python 表達式，例如計算、函數呼叫等
print()


# ── 2.16 指定列寬（Text Wrapping） ───────────────────────────────────────
print("【2.16 指定列寬】")
print("-" * 50)

# 長文本（沒有換行符）
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(f"原始長文本（{len(long_s)} 字符）:")
print(long_s)
print()

# 【方法 1】textwrap.fill() - 自動按寬度換行
print("【方法 1】自動按寬度換行（width=40）:")
wrapped = textwrap.fill(long_s, 40)
print(wrapped)
print()

# 【方法 2】加入首行縮進
print("【方法 2】加入首行四格縮進:")
wrapped_indent = textwrap.fill(long_s, 40, initial_indent="    ")
print(wrapped_indent)
print()
