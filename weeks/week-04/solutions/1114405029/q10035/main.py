import sys

def solve():
    # 使用 sys.stdin.read 快速讀取所有輸入
    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
            
        carries = 0
        carry_val = 0
        
        # 只要還有數字或還有進位值就繼續運算
        while a > 0 or b > 0:
            # 取出最後一位並加上進位
            a, da = divmod(a, 10)
            b, db = divmod(b, 10)
            
            if da + db + carry_val >= 10:
                carries += 1
                carry_val = 1
            else:
                carry_val = 0
                
        # 格式化輸出
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == "__main__":
    solve()