# 【Bloom 階段：R - 記憶與基本操作】
# R03. 字串清理與輸出排版
# August 的惡意提醒：CPE 題目對輸出的空白 (Whitespace) 有極其嚴苛的要求。
# 多一個空格或少一個空格就是「Presentation Error (PE)」。
# 掌握 strip() 與對齊技巧，是你從 CPE 地獄生還的關鍵。

import textwrap

# 1. 字串清理
s = "  hello world \n"
print(f"Cleaned: '{s.strip()}'") # 移除頭尾空白與換行

# 2. 格式化對齊 (重要！)
text = "Hello World"
print(text.ljust(20))   # 左對齊
print(text.rjust(20))   # 右對齊
print(text.center(20, '*')) # 置中並用 * 填充

# 3. 變數與字串映射
# 使用 vars() 快速將當前範疇內的變數填入模板
name, n = "Guido", 37
template = "{name} has {n} messages."
print(template.format_map(vars()))

# 4. 長文本換行 (Text Wrap)
# 在輸出說明文字或長段日誌時很有用
long_s = "Look into my eyes, look into my eyes, the eyes, not around the eyes."
print("\nFormatted Block:")
print(textwrap.fill(long_s, 40))
