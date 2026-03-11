"""
UVA 100 — 3n+1 問題（Collatz 猜想）
AI 教學版本：附繁體中文註解
"""
import sys

# 記憶化字典，儲存已計算過的 cycle-length，避免重複計算
memo = {}

def cycle_length(n):
    """計算數字 n 的 Collatz cycle-length（序列長度）"""
    # 如果已經算過，直接從快取取出
    if n in memo:
        return memo[n]
    # 基底情況：n=1 時序列長度為 1
    if n == 1:
        return 1
    # 奇數：n → 3n+1，長度加 1
    if n % 2 == 1:
        result = 1 + cycle_length(3 * n + 1)
    # 偶數：n → n/2，長度加 1
    else:
        result = 1 + cycle_length(n // 2)
    # 存入快取
    memo[n] = result
    return result

# 主程式：逐行讀取輸入
for line in sys.stdin:
    line = line.strip()
    # 跳過空行
    if not line:
        continue
    # 讀入一對整數 i, j
    i, j = map(int, line.split())
    # 取區間 [start, end]（i 可能大於 j）
    start = min(i, j)
    end = max(i, j)
    # 遍歷區間內每個數，找最大 cycle-length
    max_len = 0
    for n in range(start, end + 1):
        length = cycle_length(n)
        if length > max_len:
            max_len = length
    # 輸出格式：原始的 i j 加上最大 cycle-length
    print(i, j, max_len)
