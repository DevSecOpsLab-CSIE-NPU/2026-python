# UVA 10055 - Hashmat the Brave Warrior
# easy 版本：使用最直觀方式實作

# 本題沒有提供測試資料組數，
# 需持續讀取輸入直到檔案結束（EOF）

try:
    while True:
        # 讀入一行，包含兩個整數（兩軍隊士兵數）
        a, b = map(int, input().split())

        # 計算並輸出兩數差距的絕對值
        print(abs(a - b))

# 當讀取到輸入結束（EOF）時，正常結束程式
except EOFError:
    pass