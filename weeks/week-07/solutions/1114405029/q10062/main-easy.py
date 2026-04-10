import sys

# 簡易版：使用 Python 內建 list 配合 insert 或 pop
# 邏輯最直觀：同樣由後往前，每次找出「第 k 大」的數
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    # 讀取題目提供的數據 (第 2 到 N 頭牛的前面小牛數)
    smaller_counts = [int(x) for x in input_data[1:]]
    
    # 準備一個 1 到 N 的數字清單
    numbers = list(range(1, n + 1))
    result = [0] * n
    
    # 從最後一頭牛開始決定它的編號
    # 遍歷順序：n-1, n-2, ..., 1
    for i in range(n - 1, 0, -1):
        # 題目說前面有 k 個比它小，表示它是當前數字清單中索引值為 k 的數
        k = smaller_counts[i-1]
        # 取得該數字並從清單移除
        result[i] = numbers.pop(k)
        
    # 最後剩下的一個數字就是第一頭牛的編號
    result[0] = numbers[0]
    
    # 依序輸出結果
    for val in result:
        print(val)

if __name__ == "__main__":
    solve()