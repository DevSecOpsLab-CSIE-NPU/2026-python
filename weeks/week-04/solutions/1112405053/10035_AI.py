# 持續讀取資料直到遇到 0 0
while True:
    line = input().split()
    a, b = int(line[0]), int(line[1])
    # 0 0 為結束條件，不處理
    if a == 0 and b == 0:
        break
    
    # carry 表示當前位是否進位，count 記錄進位次數
    carry = 0
    count = 0
    # 模擬直式加法，逐位相加
    while a > 0 or b > 0 or carry > 0:
        digit_a = a % 10
        digit_b = b % 10
        total = digit_a + digit_b + carry
        # 本位和 >= 10 代表產生一次進位
        if total >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    
    # 依題目要求輸出對應文字格式
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")
