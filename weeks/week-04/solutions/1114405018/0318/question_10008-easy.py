"""UVA 10008 - easy 版本

題目要求：
1. 讀入 n 行文字。
2. 只統計英文字母（A~Z / a~z），大小寫視為相同。
3. 輸出時顯示大寫字母與其出現次數。
4. 排序規則：
   - 先依次數由大到小
   - 次數相同時依字母由小到大

這份程式用 Counter 做字母計數，邏輯短、好記。
"""

import sys
from collections import Counter

# 第一行是接下來要分析的文字行數
n = int(sys.stdin.readline())

# Counter 用來記錄每個字母出現次數
cnt = Counter()

# 逐行讀入並統計字母
for _ in range(n):
    for ch in sys.stdin.readline():
        # 只統計英文字母，忽略空白、數字與符號
        if ch.isalpha():
            # 轉成大寫後再統計，讓 a 和 A 算同一類
            cnt[ch.upper()] += 1

# 依題目規則排序後輸出：
# key = (-次數, 字母)
# -次數：讓次數大的排前面
# 字母：同次數時照字母順序
for ch, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
    print(ch, c)
