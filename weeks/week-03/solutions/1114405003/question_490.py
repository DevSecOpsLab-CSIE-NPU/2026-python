"""
題目 490：矩陣順時針旋轉 手打版本
最小化實現，適合 CPE 考試臨場

核心思路：
1. 讀取所有行
2. 補充至相同長度
3. 從右往左逐列輸出
"""

import sys

# 讀取輸入
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# 邊界情況
if not lines:
    sys.exit()

# 找最長行
max_len = max(len(line) for line in lines) if lines else 0

# 補充空白
for i in range(len(lines)):
    lines[i] = lines[i].ljust(max_len)

# 旋轉輸出
for col in range(max_len - 1, -1, -1):
    new_line = ''
    for row in range(len(lines)):
        new_line += lines[row][col]
    print(new_line)
