# -*- coding: utf-8 -*-
import sys

def solve(s, d):
    """
    解題思路：
    使用「二分搜尋法 (Binary Search)」找出答案。
    
    如果我們從 S 開始，加到某個數字 n (S + (S+1) + ... + n)
    這是一個等差數列，總和公式為：(首項 + 末項) * 項數 / 2
    也就是：(s + n) * (n - s + 1) // 2
    
    我們只需要找到一個最小的 n，讓這個總和 >= d 即可。
    因為 D 最大到 10^15，n 大約只會到 4.5 * 10^7，
    用二分搜尋範圍設定 1 到 10^8 綽綽有餘，而且非常快 (O(log N))。
    """
    left = s
    right = 10**8  # 設定一個足夠大的上限
    
    while left < right:
        mid = (left + right) // 2
        # 計算從 S 加到 mid 的總天數
        total_days = (s + mid) * (mid - s + 1) // 2
        
        if total_days >= d:
            # 如果總天數已經達到或超過 d，代表答案可能是 mid 或更小
            right = mid
        else:
            # 如果總天數還不到 d，代表答案一定比 mid 大
            left = mid + 1
            
    return left

if __name__ == '__main__':
    # 處理多筆輸入直到 EOF
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 2:
            s, d = map(int, parts)
            print(solve(s, d))