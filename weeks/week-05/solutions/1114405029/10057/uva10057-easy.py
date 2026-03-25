# UVA 10057 - A mid-summer night's dream
# easy 版本：使用最直觀方式實作

try:
    while True:
        # 讀入資料筆數
        n = int(input())

        # 依照資料筆數讀入所有整數資料
        numbers = []
        for _ in range(n):
            numbers.append(int(input()))

        # 將資料排序，方便找中間位置
        numbers.sort()

        # 若為奇數筆資料
        if n % 2 == 1:
            # 正中間的值就是唯一可行中位數
            median = numbers[n // 2]

            # 統計該值在資料中出現幾次
            count = 0
            for value in numbers:
                if value == median:
                    count += 1

            # 奇數筆時，可行中位數只有一個
            print(median, count, 1)

        # 若為偶數筆資料
        else:
            # 找出排序後中間兩個值
            low = numbers[n // 2 - 1]
            high = numbers[n // 2]

            # 統計原資料中有多少數值落在 [low, high] 範圍內
            count = 0
            for value in numbers:
                if low <= value <= high:
                    count += 1

            # 輸出：
            # 1. 最小可行中位數 low
            # 2. 落在可行範圍內的資料個數 count
            # 3. 可作為中位數的整數個數 high - low + 1
            print(low, count, high - low + 1)

# 當讀到輸入結束（EOF）時，正常結束程式
except EOFError:
    pass