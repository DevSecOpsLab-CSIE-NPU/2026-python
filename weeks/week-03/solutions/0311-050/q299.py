import sys

def count_swaps(carriages):
    """
    計算將串列由小到大排序所需的最少「相鄰交換」次數。
    採用氣泡排序法 (Bubble Sort) 的概念，每次交換就將計數器 +1。
    """
    swaps = 0
    n = len(carriages)
    # 複製一份陣列，避免改動到原始傳入的資料 (對單元測試較友善)
    arr = carriages[:]
    
    for i in range(n):
        for j in range(n - 1 - i):
            # 如果前面的數字比後面的數字大，就進行交換 (逆序對)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                
    return swaps

if __name__ == '__main__':
    # 一次性讀取所有輸入，並以空白/換行進行分割
    input_data = sys.stdin.read().split()
    
    if input_data:
        # 第一個數字是測試案例的數量 N
        num_test_cases = int(input_data[0])
        idx = 1
        
        for _ in range(num_test_cases):
            # 讀取每台火車的長度 L
            l = int(input_data[idx])
            idx += 1
            
            # 根據長度 L 讀取接下來的 L 個車廂編號
            carriages = [int(x) for x in input_data[idx : idx+l]]
            idx += l
            
            ans = count_swaps(carriages)
            print(f"Optimal train swapping takes {ans} swaps.")