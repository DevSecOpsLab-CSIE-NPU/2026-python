import sys

def solve():
    """
    UVA 11349 Symmetric Matrix (手打/白板解題版)
    特點：
    1. 不依賴 re (正規表達式) 模組，完全使用最基礎的字串處理，考場上更容易默寫出來。
    2. 依然保留 Pythonic 的一維陣列反轉檢查法，程式碼極簡。
    """
    # 讀取全部輸入，利用空白或換行切割成一個個字串 (Token)
    # 這樣的結果會包含像 '2', 'N', '=', '3', '5', '1' 等等
    raw_tokens = sys.stdin.read().split()
    
    # 考場手打最直觀的過濾法：
    # 如果這個 token 不是 'N' 也不是 '='，那就一定是數字
    nums = []
    for t in raw_tokens:
        if t != 'N' and t != '=':
            nums.append(int(t))
            
    if not nums:
        return

    # 第一個數字是測資筆數 T
    T = nums[0]
    idx = 1
    
    for t in range(1, T + 1):
        if idx >= len(nums):
            break
            
        # 取得矩陣大小 n
        n = nums[idx]
        idx += 1
        
        # 透過切片一口氣抓取 n*n 個元素變成一維陣列
        elements = nums[idx : idx + n*n]
        idx += n * n
        
        # 核心判斷：
        # 1. 陣列中所有的值都要 >= 0 (沒有負數)
        # 2. 陣列正著看跟反著看要一模一樣 (elements == elements[::-1])
        if all(x >= 0 for x in elements) and elements == elements[::-1]:
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

if __name__ == '__main__':
    solve()
