import sys

def get_min_distance(relatives):
    """
    計算給定親戚門牌號碼串列的最佳住所位置（中位數），
    並回傳距離所有親戚家總和的最小值。
    """
    if not relatives:
        return 0
        
    # 1. 必須先對所有門牌號碼進行排序，才能找出正確的中位數
    relatives.sort()
    
    # 2. 找出中位數的索引
    # 若數量為偶數，取中間兩個的任一個皆可得到相同的最小總距離，這裡統一取左邊那個
    mid_index = len(relatives) // 2
    median = relatives[mid_index]
    
    # 3. 計算所有人到中位數的絕對距離總和
    total_distance = sum(abs(x - median) for x in relatives)
    
    return total_distance

if __name__ == '__main__':
    # 讀取所有標準輸入，並以空白/換行進行分割
    input_data = sys.stdin.read().split()
    
    if input_data:
        # 第一個數字是測試資料的組數
        num_test_cases = int(input_data[0])
        idx = 1
        
        for _ in range(num_test_cases):
            # 每一組測資的第一個數字 r 代表親戚的數量
            r = int(input_data[idx])
            idx += 1
            # 接下來的 r 個數字是親戚的門牌號碼
            relatives = [int(x) for x in input_data[idx : idx + r]]
            idx += r
            
            # 呼叫函式計算並印出結果
            print(get_min_distance(relatives))