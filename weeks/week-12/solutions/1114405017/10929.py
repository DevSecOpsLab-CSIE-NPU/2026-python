# UVA 10929 — 判斷 11 的倍數
# 這個程式判斷輸入的正整數是否為 11 的倍數，使用奇數位與偶數位數字和的差來檢查。

import sys  # 匯入 sys 模組，用於讀取標準輸入

for line in sys.stdin:  # 讀取每一行輸入
    num = line.strip()  # 去除空白
    if num == '0':  # 如果是 0，結束
        break
    odd_sum = 0  # 奇數位總和
    even_sum = 0  # 偶數位總和
    for i in range(len(num)):  # 對於每一位
        d = int(num[-(i+1)])  # 從右邊開始取數字
        if i % 2 == 0:  # 如果是奇數位（從右邊算）
            odd_sum += d  # 加到奇數位總和
        else:  # 偶數位
            even_sum += d  # 加到偶數位總和
    diff = abs(odd_sum - even_sum)  # 計算差的絕對值
    if diff % 11 == 0:  # 如果差是 11 的倍數
        print(f"{num} is a multiple of 11.")  # 輸出是
    else:  # 否則
        print(f"{num} is not a multiple of 11.")  # 輸出不是