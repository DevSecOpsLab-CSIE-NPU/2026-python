import sys

# AI 建議的簡單版本 - 10929 You can say 11
# 繁體中文註解說明

def solve():
    # 逐行讀取標準輸入
    for line in sys.stdin:
        # 去除前後空白與換行符號
        n_str = line.strip()
        
        # 若輸入為 "0"，代表結束輸入
        if n_str == '0':
            break
            
        if not n_str:
            continue
            
        # 在 Python 中，可以直接將字串轉為整數進行大數運算
        n_val = int(n_str)
        
        # 判斷是否能被 11 整除
        if n_val % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
