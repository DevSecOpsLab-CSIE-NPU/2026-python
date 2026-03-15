n = int(input())  # 步驟 1：輸入整數 n

while True:
    print(n)          # 步驟 2：印出目前的 n
    if n == 1:        # 步驟 3：如果 n 等於 1，結束
        break
    if n % 2 == 1:    # 步驟 4：如果 n 是奇數
        n = 3 * n + 1 #          則 n = 3n + 1
    else:             # 步驟 5：否則（n 是偶數）
        n = n // 2    #          則 n = n / 2
    # 步驟 6：回到步驟 2（while 迴圈自動回頭）
