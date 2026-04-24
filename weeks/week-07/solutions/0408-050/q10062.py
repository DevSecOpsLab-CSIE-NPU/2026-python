import sys

def solve_cows(n, smaller_counts):
    """
    從後往前反推乳牛的排列順序。
    為了在 N=80,000 的大測資下避免 TLE，使用「樹狀陣列 (BIT)」搭配二元提升 (Binary Lifting)
    來達成 O(log N) 查詢「第 K 小可用數字」與移除。
    """
    # bit 陣列用來維護每個數字是否可用 (1: 可用, 0: 已被用掉)
    bit = [0] * (n + 1)
    
    def add(idx, val):
        """單點修改：在 idx 位置加上 val"""
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
            
    def find_kth(k):
        """利用二元提升在 BIT 中快速尋找第 k 小的可用數字"""
        idx = 0
        # 找出大於等於 n 的 2 的次方步長
        step = 1 << n.bit_length()
        
        while step > 0:
            next_idx = idx + step
            # 如果跳過去沒有超過 n，且累積的可用數字數量小於 k，就安心跳過去
            if next_idx <= n and bit[next_idx] < k:
                idx = next_idx
                k -= bit[next_idx]  # 扣掉跳過的區間總和
            step >>= 1
            
        # 跳完後 idx 會停在累積數量恰好少 1 的位置，所以加 1 就是答案
        return idx + 1

    # 初始狀態：把 1 到 n 所有數字都標記為可用 (加進 BIT 中)
    for i in range(1, n + 1):
        add(i, 1)
        
    ans = [0] * n
    # 題目沒有給第一頭牛的 smaller 數量 (因為必定為 0)，所以我們在前面補 0
    counts = [0] + smaller_counts
    
    # 從最後一頭牛開始「由後往前」反推
    for i in range(n - 1, -1, -1):
        # 這頭牛前面有 counts[i] 頭比牠小，代表牠是剩下數字中的「第 counts[i] + 1 小」
        rank = counts[i] + 1
        val = find_kth(rank)
        ans[i] = val
        # 將用掉的數字從可用名單中移除
        add(val, -1)
        
    return ans

if __name__ == '__main__':
    # 讀取所有輸入並過濾掉換行與空白
    input_data = sys.stdin.read().split()
    idx = 0
    
    # UVA 測資通常包含多組測試資料直到 EOF
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        # 讀取這組測資接下來的 N-1 個數字
        smaller_counts = [int(x) for x in input_data[idx : idx + n - 1]]
        idx += n - 1
        
        # 計算並輸出正確排列
        result = solve_cows(n, smaller_counts)
        for cow in result:
            print(cow)