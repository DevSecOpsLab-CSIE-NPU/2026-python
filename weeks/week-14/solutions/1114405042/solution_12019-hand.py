import sys
import datetime

def solve():
    
    # 讀取全部輸入，利用空白或換行切割成一個個數字字串 (Token)
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    # 第一個數字是測資組數 T
    T = int(tokens[0])
    idx = 1
    
    for _ in range(T):
        if idx >= len(tokens):
            break
            
        m = int(tokens[idx])
        d = int(tokens[idx+1])
        idx += 2
        
        # 核心邏輯：直接丟進 datetime，然後印出來，省去組裝字串的麻煩
        ans = datetime.date(2011, m, d).strftime("%A")
        print(ans)

if __name__ == '__main__':
    solve()
