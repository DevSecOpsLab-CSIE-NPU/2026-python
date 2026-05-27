import sys

def solve():
    """
    UVA 11461 - Square Numbers (手打/白板解題版)
    特點：
    1. 捨棄繁雜的字串處理與結果陣列儲存，直接在迴圈中「邊讀邊印」(print)，行數極少。
    2. for line in sys.stdin 寫法簡潔，自動讀取多行，是最適合手寫的輸入方式。
    3. 保留 easy 版的核心：利用前綴和與指數運算 ( ** 0.5 )，連 import math 都不需要！
    """
    # 考場上最直觀的讀取方式：一行一行讀
    for line in sys.stdin:
        # 預防不小心的空行
        if not line.strip():
            continue
            
        a, b = map(int, line.split())
        
        # 遇到 0 0 直接結束程式
        if a == 0 and b == 0:
            break
            
        # 核心邏輯：前綴和相減 ( 1~b 的數量 減掉 1~(a-1) 的數量 )
        # X ** 0.5 是開根號，int() 會自動無條件捨去
        # 直接印出答案，省去組裝字串的麻煩
        ans = int(b ** 0.5) - int((a - 1) ** 0.5)
        print(ans)

if __name__ == '__main__':
    solve()
