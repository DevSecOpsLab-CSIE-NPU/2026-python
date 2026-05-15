import sys

# AI 建議的簡單版本 - 10908 Largest Square
# 繁體中文註解說明

def solve():
    """
    主要解題函數
    """
    # 讀取標準輸入中的所有資料並切分成字串列表
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    # 讀取測試資料組數 T
    T = int(input_data[idx])
    idx += 1
    
    for _ in range(T):
        # 讀取網格大小 M, N 以及查詢次數 Q
        M = int(input_data[idx])
        N = int(input_data[idx+1])
        Q = int(input_data[idx+2])
        idx += 3
        
        # 讀取網格內容
        grid = []
        for i in range(M):
            grid.append(input_data[idx])
            idx += 1
        
        # 依照題目要求，先輸出 M N Q
        print(f"{M} {N} {Q}")
        
        # 處理每個查詢 (r, c)
        for _ in range(Q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            # 中心點字元
            target = grid[r][c]
            # 最小邊長一定是 1
            max_len = 1
            
            # k 為中心點向外擴張的距離，邊長為 2*k + 1
            k = 1
            while True:
                # 檢查正方形四個邊界是否超出網格範圍
                if r - k < 0 or r + k >= M or c - k < 0 or c + k >= N:
                    break
                
                # 檢查擴張後的正方形邊界字元是否都符合 target
                is_valid = True
                
                # 檢查上方與下方的水平線
                for j in range(c - k, c + k + 1):
                    if grid[r - k][j] != target or grid[r + k][j] != target:
                        is_valid = False
                        break
                if not is_valid:
                    break
                
                # 檢查左方與右方的垂直線
                for i in range(r - k, r + k + 1):
                    if grid[i][c - k] != target or grid[i][c + k] != target:
                        is_valid = False
                        break
                if not is_valid:
                    break
                
                # 若檢查通過，更新最大邊長，繼續向外擴展
                max_len = 2 * k + 1
                k += 1
            
            # 輸出該查詢的最大邊長
            print(max_len)

if __name__ == "__main__":
    solve()
