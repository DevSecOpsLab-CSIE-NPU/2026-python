# 299_ai_easy.py
# UVA 299：火車車廂排序 - 簡單版，附詳細繁體中文註解
# 功能：計算將車廂排序到 1 到 L 所需的最小相鄰交換次數

def count_swaps(cars):
    """
    計算排序所需的最小交換次數（反序數）。
    
    參數：
    cars (list): 車廂排列
    
    返回：
    int: 交換次數
    """
    swaps = 0
    n = len(cars)
    
    # 使用簡單的氣泡排序計數交換
    for i in range(n):
        for j in range(i+1, n):
            if cars[i] > cars[j]:
                swaps += 1
    
    return swaps

# 主程式：讀取輸入
if __name__ == "__main__":
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    
    N = int(input_lines[0])  # 測資數量
    line_index = 1
    
    for _ in range(N):
        L = int(input_lines[line_index])  # 車廂長度
        line_index += 1
        cars = list(map(int, input_lines[line_index].split()))
        line_index += 1
        
        # 計算交換次數
        swaps = count_swaps(cars)
        
        # 輸出
        print(f"Optimal train swapping takes {swaps} swaps.")