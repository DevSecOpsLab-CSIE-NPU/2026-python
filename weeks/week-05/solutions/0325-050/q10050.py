import sys

def count_hartals(n, parties):
    """
    計算 N 天之內，因為各政黨罷會所損失的工作天數。
    利用 Set 來去除多個政黨在同一天罷會的重複計算。
    """
    hartal_days = set()
    
    for h in parties:
        # 利用 range 的步長 (step) 找出該政黨所有罷會的日期 (h, 2h, 3h...)
        for day in range(h, n + 1, h):
            # 判斷是否為假日。題目假設第 1 天是星期日。
            # 所以第 6, 13, 20... 天是星期五 (day % 7 == 6)
            # 第 7, 14, 21... 天是星期六 (day % 7 == 0)
            if day % 7 != 6 and day % 7 != 0:
                hartal_days.add(day)
                
    # 集合的大小即為不重複的罷會工作天數
    return len(hartal_days)

if __name__ == '__main__':
    # 讀取標準輸入
    input_data = sys.stdin.read().split()
    if input_data:
        T = int(input_data[0])  # 測資筆數
        idx = 1
        for _ in range(T):
            N = int(input_data[idx])
            P = int(input_data[idx+1])
            idx += 2
            
            parties = [int(x) for x in input_data[idx : idx + P]]
            idx += P
            
            print(count_hartals(N, parties))