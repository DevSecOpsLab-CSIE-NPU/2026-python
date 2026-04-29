# -*- coding: utf-8 -*-
"""
UVA 10268 - 10265 - Handles on Bags 簡化版
經典蛋糕測試問題（Egg Drop Problem）
k 個蛋，n 層建築，求最少測試次數
"""

def solve(inp):
    lines = inp.strip().split('\n')
    
    results = []
    
    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        k, n = map(int, parts)
        
        if k == 0:
            break
        
        # DP: dp[i][j] = 用 i 個蛋測 j 層需要的最少次數
        # 簡化版本：若蛋足夠（k >= log2(n)），可用二分搜尋
        # 否則需要更複雜的 DP
        
        if k >= 64:
            # 蛋足夠，可用二分
            trials = 0
            temp = n
            while temp > 1:
                temp //= 2
                trials += 1
            if trials > 63:
                results.append("More than 63 trials needed.")
            else:
                results.append(str(trials))
        else:
            # 用 DP 計算
            # dp[e][t] = 用 e 個蛋，t 次試驗可以測的最多層數
            dp = [[0] * 64 for _ in range(k + 1)]
            
            trials = 0
            while dp[k][trials] < n:
                trials += 1
                if trials > 63:
                    break
                for e in range(1, k + 1):
                    dp[e][trials] = dp[e][trials - 1] + dp[e - 1][trials - 1] + 1
            
            if trials > 63:
                results.append("More than 63 trials needed.")
            else:
                results.append(str(trials))
    
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read()))
