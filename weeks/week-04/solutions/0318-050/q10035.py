import sys

def solve_carries(a, b):
    """
    計算兩個數字相加時，總共會產生幾次進位。
    回傳格式化後的字串，並處理單複數與零次的文法差異。
    """
    # 確保傳入的 a, b 為整數型態
    a, b = int(a), int(b)
    carry_count = 0  # 總進位次數
    current_carry = 0  # 記錄當下這個位數相加後，是否有進位留給下一個位數 (0 或 1)
    
    # 只要 a 還有數字、b 還有數字，或是「還有進位還沒處理完」，就繼續算
    while a > 0 or b > 0 or current_carry > 0:
        # 透過 % 10 取得個位數
        digit_a = a % 10
        digit_b = b % 10
        
        # 將目前的兩個位數加上「前一位傳過來的進位」
        total = digit_a + digit_b + current_carry
        
        if total >= 10:
            carry_count += 1
            current_carry = 1  # 產生進位，留給下一回合
        else:
            current_carry = 0  # 沒有產生進位，歸零
            
        # 將 a 和 b 透過整數除法 (// 10) 砍掉最後一位，相當於整體往右平移
        a //= 10
        b //= 10
        
    # 根據進位次數組合回傳字串 (注意單複數和開頭大小寫)
    if carry_count == 0:
        return "No carry operation."
    elif carry_count == 1:
        return "1 carry operation."
    else:
        return f"{carry_count} carry operations."

if __name__ == '__main__':
    # 讀取標準輸入
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 2:
            a, b = parts
            # 遇到 0 0 時終止程式
            if a == '0' and b == '0':
                break
            print(solve_carries(a, b))