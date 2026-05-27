import sys
import math
import itertools

def solve():
    """
    UVA 11417 - GCD (手打/白板解題版)
    特點：
    1. 捨棄繁瑣的字串切割 (split) 與結果陣列 (output.append)，在考場上直接「邊讀邊印」(print)，大幅減少行數。
    2. 利用 for line in sys.stdin 自動處理每一行輸入，遇到 0 直接 break，是最不會出錯的輸入法。
    3. 保留 easy 版的核心：itertools.combinations 搭配 sum() 一行算完答案。
    """
    # 考場上最直觀的讀取方式：一行一行讀
    for line in sys.stdin:
        n = int(line)
        
        if n == 0:
            break
            
        # 核心邏輯：使用 generator 與 combinations 一行搞定
        # 直接 print 出來，不用考慮組裝字串的問題
        ans = sum(math.gcd(i, j) for i, j in itertools.combinations(range(1, n + 1), 2))
        print(ans)

if __name__ == '__main__':
    solve()
