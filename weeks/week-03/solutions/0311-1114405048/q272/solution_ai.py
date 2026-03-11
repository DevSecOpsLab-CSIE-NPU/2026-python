"""
UVA 272 — TeX 引號替換
AI 教學版本：附繁體中文註解
"""
import sys

# 用布林值記錄下一個遇到的 " 是開引號還是閉引號
# True 表示下一個是開引號（用 `` 替換）
opening = True

# 逐行讀取輸入
for line in sys.stdin:
    out = []
    # 逐字元掃描每一行
    for ch in line:
        if ch == '"':
            if opening:
                # 開引號：替換為兩個左單引號 ``
                out.append('``')
            else:
                # 閉引號：替換為兩個右單引號 ''
                out.append("''")
            # 翻轉狀態：開 ↔ 閉
            opening = not opening
        else:
            # 非引號字元：原樣保留
            out.append(ch)
    # 輸出轉換後的行（line 本身含換行符，故用 end=''）
    print(''.join(out), end='')
