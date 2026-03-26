# UVA 10041 - Vito's Family
# easy 版本：使用最直觀方式實作


# 讀入測試資料組數
t = int(input())

# 逐組處理
for _ in range(t):
    # 讀入一整行資料
    # 格式為：r a1 a2 a3 ... ar
    data = list(map(int, input().split()))

    # 第一個數字是親戚人數
    r = data[0]

    # 取出後面 r 個地址
    addresses = data[1:1 + r]

    # 將地址排序（為了找中位數）
    addresses.sort()

    # 找中位數位置
    # 若為奇數筆，中位數唯一
    # 若為偶數筆，取中間任一個都能得到最小總距離
    median = addresses[r // 2]

    # 計算所有地址到中位數的總距離
    total = 0
    for address in addresses:
        total += abs(address - median)

    # 輸出結果
    print(total)