import sys

def solve():
    # 讀取所有輸入並轉成迭代器
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    S = int(input_data[0])
    idx = 1
    
    for _ in range(S):
        N = int(input_data[idx])      # 玩家總數
        p = float(input_data[idx+1])  # 成功機率
        i = int(input_data[idx+2])    # 目標玩家序號
        idx += 3
        
        # 特殊處理：若 p 為 0，機率必為 0
        if p == 0:
            print(f"{0.0000:.4f}")
            continue
            
        q = 1 - p
        # 分子：首項 p * (q^(i-1))
        # 分母：1 - 公比 (q^N)
        ans = (p * (q**(i-1))) / (1 - (q**N))
        
        print(f"{ans:.4f}")

if __name__ == "__main__":
    solve()