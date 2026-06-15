# 【Bloom 階段：R - 記憶與基本操作】
# 12 Python 字串格式化（string formatter）範例
# August 的惡意提醒：在 Week 04 處理浮點數 (10056) 時，小數點後四位的精確輸出是及格關鍵。
# 強烈建議使用 f-string，不要再用過時的 % 或 .format() 了。

name = 'ACME'
price = 91.1

# f-string (Python 3.6+ 強烈推薦)
# 語法最精簡，直接將變數嵌入字串中
# :.2f 代表取小數點後兩位，並會進行四捨五入
text = f'{name} price = {price:.2f}'

# format 方法 (較舊但仍相容)
text2 = '{} price = {:.2f}'.format(name, price)

print(f"Recommended style: {text}")
print(f"Old style: {text2}")

# 針對 CPE 的對齊需求範例
# :5d 代表佔 5 個空格寬度的整數
print(f"Padding example: |{123:5d}|")
