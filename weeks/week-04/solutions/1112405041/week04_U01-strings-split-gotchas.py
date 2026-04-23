# 【Bloom 階段：U - 理解與進階應用】
# U01. 字串分割與匹配的隱藏陷阱
# August 的惡意提醒：這是指紋與細節的區別。

import re

# 1. re.split 捕獲分組地雷
line = "asdf fjdk; afed"
# 如果括號 ( ) 包圍正則表達式，分隔符也會被保留在結果清單中！
fields = re.split(r"(;|\s)\s*", line)
print(f"Captured groups: {fields}") # ['asdf', ' ', 'fjdk', ';', 'afed']

# 2. startswith 必須使用 Tuple
url = "http://python.org"
# try: url.startswith(["http:", "ftp:"]) # ❌ 這會噴 TypeError
# 修正：必須轉為 tuple
print(f"Correct startswith: {url.startswith(tuple(['http:', 'ftp:']))}")

# 3. strip() 不是移除子字串
s = "  hello world  "
print(f"strip only ends: '{s.strip()}'")
# 若要移除中間所有空格，必須用 replace 或 re.sub
print(f"Internal space removed: {re.sub(r'\s+', ' ', s.strip())}")
