"""UVA 10019 - easy 版本

題目重點（依目前題目敘述）：
1. 每一行輸入兩個整數。
2. 對每一組輸入輸出兩者差值的絕對值。
3. 需要處理直到 EOF（檔案結束）為止的多行資料。

這份 easy 版採用最直觀寫法：
- 逐行讀入
- 拆成兩個整數
- 印出 abs(a - b)
"""

import sys

# sys.stdin 代表標準輸入，for line in sys.stdin 可逐行讀到 EOF
for line in sys.stdin:
    # 去掉行首尾空白（包含換行符）
    line = line.strip()

    # 若該行是空行，就略過
    if not line:
        continue

    # 把這一行拆成兩個整數
    a, b = map(int, line.split())

    # 輸出兩者差值的絕對值（永遠非負）
    print(abs(a - b))
