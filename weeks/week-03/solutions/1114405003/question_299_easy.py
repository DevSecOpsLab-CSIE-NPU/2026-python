"""
題目 299：火車車廂置換 簡單版本
檔名：question_299_easy.py

最簡單、最容易記憶的解法
使用樸素 O(n²) 計數法，適合臨場編寫

核心思想：逆序對個數 = 最少交換次數
逆序對：當 i < j 但 arr[i] > arr[j] 時，(i,j) 就是一個逆序對
"""


def count_swaps(train):
    """
    計算最少交換次數（合併排序版本）
    
    使用合併排序的思想計算逆序對
    時間複雜度更優秀 O(n log n)
    
    Args:
        train: 火車車廂的排列
        
    Returns:
        最少交換次數
    """
    
    def merge_count(arr, temp, left, mid, right):
        """合併並計算逆序對"""
        i = left      # 左邊子陣列起點
        j = mid + 1   # 右邊子陣列起點
        k = left      # 臨時陣列指針
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                # 右邊元素更小，計算逆序對
                temp[k] = arr[j]
                inv_count += mid - i + 1
                j += 1
            k += 1
        
        # 複製剩餘元素
        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1
        
        while j <= right:
            temp[k] = arr[j]
            k += 1
            j += 1
        
        # 複製回原陣列
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        """遞迴進行合併排序並計數"""
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            # 分別計算左邊和右邊
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            
            # 合併並計算交叉的逆序對
            inv_count += merge_count(arr, temp, left, mid, right)
        
        return inv_count
    
    if len(train) <= 1:
        return 0
    
    # 建立工作陣列
    arr = train[:]
    temp = [0] * len(train)
    
    return merge_sort_count(arr, temp, 0, len(train) - 1)


def solve(train_order):
    """求解火車車廂置換問題"""
    swaps = count_swaps(train_order)
    return swaps


# 主程式
if __name__ == '__main__':
    # 讀取測試資料
    try:
        n = int(input())  # 測試資料組數
        
        for _ in range(n):
            l = int(input())  # 火車長度
            
            if l == 0:
                print("Optimal train swapping takes 0 swaps.")
            else:
                train = list(map(int, input().split()))
                result = solve(train)
                print(f"Optimal train swapping takes {result} swaps.")
    
    except EOFError:
        pass
