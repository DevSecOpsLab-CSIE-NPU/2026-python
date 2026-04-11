import sys

def run():
    # 讀取輸入流
    lines = sys.stdin.read().split()
    if not lines:
        return
    
    idx = 0
    num_cases = int(lines[idx])
    idx += 1
    
    for t in range(num_cases):
        n = int(lines[idx]) # 硬幣數
        k = int(lines[idx+1]) # 秤重次數
        idx += 2
        
        # 建立一個清單記錄每個硬幣是否「可能是假的」
        # 索引 0 不用，使用 1 到 n
        is_maybe_fake = [True] * (n + 1)
        
        for _ in range(k):
            p = int(lines[idx])
            idx += 1
            
            # 取得左盤與右盤的硬幣編號
            current_on_scale = []
            for _ in range(2 * p):
                current_on_scale.append(int(lines[idx]))
                idx += 1
            
            # 取得結果符號 (<, >, =)
            result = lines[idx]
            idx += 1
            
            if result == '=':
                # 如果平衡，秤上的硬幣絕對是真的
                for coin in current_on_scale:
                    is_maybe_fake[coin] = False
            else:
                # 如果不平衡，「不在秤上」的硬幣絕對是真的
                on_scale_set = set(current_on_scale)
                for i in range(1, n + 1):
                    if i not in on_scale_set:
                        is_maybe_fake[i] = False
        
        # 最後統計還剩下多少個「可能是假」的硬幣
        ans = []
        for i in range(1, n + 1):
            if is_maybe_fake[i]:
                ans.append(i)
        
        # 剛好只有一個才是答案，否則輸出 0
        if len(ans) == 1:
            print(ans[0])
        else:
            print(0)
            
        # 組間空白列
        if t < num_cases - 1:
            print()

if __name__ == "__main__":
    run()