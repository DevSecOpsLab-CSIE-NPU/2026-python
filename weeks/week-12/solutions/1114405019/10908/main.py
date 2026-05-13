import sys

# 題目：UVA 10908 - Largest Square
# 題目說明：給定一個 M x N 的字元網格與 Q 個查詢。
# 每個查詢給定中心點 (r, c)，求以該點為中心且所有字元皆相同的最大正方形邊長。
# 正方形邊長必須為奇數。

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    # 讀取測試資料組數 T
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        # M: 行數, N: 列數, Q: 查詢次數
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        q = int(input_data[idx+2])
        idx += 3
        
        # 讀取網格字元
        grid = []
        for i in range(m):
            grid.append(input_data[idx])
            idx += 1
            
        # 輸出網格資訊
        print(f"{m} {n} {q}")
        
        # 處理每個查詢
        for _ in range(q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            # 中心點的字元
            center_char = grid[r][c]
            # 初始邊長為 1 (中心點本身)
            max_side = 1
            
            # k 代表向外擴散的距離 (1, 2, 3...)
            # 對應邊長為 2k + 1
            k = 1
            while True:
                r_start, r_end = r - k, r + k
                c_start, c_end = c - k, c + k
                
                # 檢查邊界
                if r_start < 0 or r_end >= m or c_start < 0 or c_end >= n:
                    break
                
                # 檢查目前這層的所有字元是否與中心點相同
                is_valid = True
                # 檢查上下兩橫排
                for j in range(c_start, c_end + 1):
                    if grid[r_start][j] != center_char or grid[r_end][j] != center_char:
                        is_valid = False
                        break
                if not is_valid: break
                
                # 檢查左右兩直排
                for i in range(r_start, r_end + 1):
                    if grid[i][c_start] != center_char or grid[i][c_end] != center_char:
                        is_valid = False
                        break
                if not is_valid: break
                
                # 若檢查通過，更新最大邊長並繼續下一層
                max_side = 2 * k + 1
                k += 1
            
            print(max_side)

if __name__ == "__main__":
    solve()
