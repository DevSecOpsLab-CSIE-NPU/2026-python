"""
UVA 10035: 進位次數

計算兩數相加時產生的進位次數。
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
        
        # 將兩數反向變成陣列，最低位優先
        a_digits = []
        b_digits = []
        
        temp_a = a
        temp_b = b
        
        # 提取數字
        while temp_a > 0:
            a_digits.append(temp_a % 10)
            temp_a //= 10
        
        while temp_b > 0:
            b_digits.append(temp_b % 10)
            temp_b //= 10
        
        # 補足長度
        max_len = max(len(a_digits), len(b_digits))
        a_digits += [0] * (max_len - len(a_digits))
        b_digits += [0] * (max_len - len(b_digits))
        
        # 計算進位
        carry_count = 0
        carry = 0
        
        for i in range(max_len):
            digit_sum = a_digits[i] + b_digits[i] + carry
            if digit_sum >= 10:
                carry_count += 1
                carry = 1
            else:
                carry = 0
        
        if carry_count == 1:
            print(f"{carry_count} carry operation.")
        elif carry_count == 0:
            print("No carry operation.")
        else:
            print(f"{carry_count} carry operations.")
except EOFError:
    pass
