import sys

def is_jolly(sequence):
    """
    判斷一個整數序列是否為 Jolly Jumper。
    """
    n = len(sequence)
    
    # 根據題目定義，n=1 時必定是 Jolly
    if n <= 1:
        return "Jolly"
        
    # 建立一個集合來儲存所有計算出來的差值
    diffs = set()
    
    # 走訪序列，計算相鄰元素的絕對差值
    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i+1])
        diffs.add(diff)
        
    # 建立一個標準答案的集合，也就是 1 到 n-1
    expected_diffs = set(range(1, n))
    
    # 直接比對兩個集合是否完全相等
    if diffs == expected_diffs:
        return "Jolly"
    else:
        return "Not jolly"

if __name__ == '__main__':
    # 讀取標準輸入
    for line in sys.stdin:
        parts = [int(x) for x in line.split()]
        # 第一個數字 n 不需要，我們直接用 len() 取得序列長度
        sequence = parts[1:]
        print(is_jolly(sequence))