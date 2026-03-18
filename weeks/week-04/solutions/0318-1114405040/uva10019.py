"""
UVA 10019: 士兵數目差

計算 Hashmat 與敵方士兵數目的差（絕對值）。
"""

try:
    while True:
        line = input().strip()
        if not line:
            continue
        
        a, b = map(int, line.split())
        
        # 兩邊都是 0 表示輸入結束
        if a == 0 and b == 0:
            break
        
        # 輸出正數差
        print(abs(a - b))
except EOFError:
    pass
