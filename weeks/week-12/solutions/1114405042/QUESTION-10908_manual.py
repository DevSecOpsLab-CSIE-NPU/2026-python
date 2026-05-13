def get_largest_square_easy(grid, M, N, r, c):
    """
    用最直覺、最容易記憶的方式：直接檢查整個正方形範圍內的字元是否都相同。
    
    :param grid: 網格字串陣列
    :param M: 總行數
    :param N: 總列數
    :param r: 中心點 X (row)
    :param c: 中心點 Y (col)
    """
    center_char = grid[r][c]
    ans_length = 1 # 最小邊長一定是 1 (只有中心點自己)
    
    # 從半徑 k = 1 開始向外擴大 (邊長 = 3, 5, 7...)
    k = 1
    while True:
        # 1. 檢查這個正方形是否超出邊界
        if r - k < 0 or r + k >= M or c - k < 0 or c + k >= N:
            break
            
        # 2. 暴力檢查這個區塊內所有的字元
        all_same = True
        for i in range(r - k, r + k + 1):
            for j in range(c - k, c + k + 1):
                if grid[i][j] != center_char:
                    all_same = False
                    break # 只要發現一個不一樣，就提早結束這層迴圈
            if not all_same:
                break # 繼續跳出外層迴圈
                
        # 3. 根據檢查結果決定是否繼續擴大
        if all_same:
            ans_length = 2 * k + 1 # 更新目前找到的最大邊長
            k += 1 # 繼續嘗試更大的正方形
        else:
            break # 發現不符合，直接結束尋找
            
    return ans_length

def solve_easy():
    import sys
    # 讀取所有標準輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        M = int(input_data[idx])
        N = int(input_data[idx+1])
        Q = int(input_data[idx+2])
        idx += 3
        
        print(f"{M} {N} {Q}")
        
        grid = []
        for _ in range(M):
            grid.append(input_data[idx])
            idx += 1
            
        for _ in range(Q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2
            
            print(get_largest_square_easy(grid, M, N, r, c))

if __name__ == '__main__':
    solve_easy()
