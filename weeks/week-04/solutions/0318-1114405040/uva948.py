"""
UVA 948: 假幣檢測

找出被標記的假硬幣是哪一個，通過天平秤重結果推斷。
"""

def solve_case(n, k, measurements):
    """
    嘗試每一個硬幣的兩種情況：
    1. 假幣比真幣重
    2. 假幣比真幣輕
    """
    
    # 嘗試每一個可能的假幣
    for fake_coin in range(1, n + 1):
        # 嘗試假幣比真幣重
        if check_hypothesis(n, measurements, fake_coin, True):
            return fake_coin
        
        # 嘗試假幣比真幣輕
        if check_hypothesis(n, measurements, fake_coin, False):
            return fake_coin
    
    return 0


def check_hypothesis(n, measurements, fake_coin, is_heavier):
    """
    檢查假設是否與所有秤重結果一致。
    """
    
    for pi, left, right, result in measurements:
        # 計算假設下的左邊重量
        left_weight = pi  # 先假設全部是真幣
        
        # 如果假幣在左邊
        if fake_coin in left:
            if is_heavier:
                left_weight += 1
            else:
                left_weight -= 1
        
        # 計算假設下的右邊重量
        right_weight = pi  # 先假設全部是真幣
        
        # 如果假幣在右邊
        if fake_coin in right:
            if is_heavier:
                right_weight += 1
            else:
                right_weight -= 1
        
        # 根據秤重結果檢查
        expected_result = None
        if left_weight < right_weight:
            expected_result = '<'
        elif left_weight > right_weight:
            expected_result = '>'
        else:
            expected_result = '='
        
        # 如果不一致，這個假設不對
        if expected_result != result:
            return False
    
    return True


try:
    m = int(input())
    
    for case_idx in range(m):
        if case_idx > 0:
            print()  # 測試資料間輸出空白列
        
        # 讀取空白列
        while True:
            line = input().strip()
            if line:
                parts = list(map(int, line.split()))
                n = parts[0]
                k = parts[1]
                break
        
        measurements = []
        
        for _ in range(k):
            # 讀取第一列：硬幣編號
            left_input = list(map(int, input().split()))
            pi = left_input[0]
            left_coins = left_input[1:pi+1]
            right_coins = left_input[pi+1:2*pi+1]
            
            # 讀取第二列：秤重結果
            result = input().strip()
            
            measurements.append((pi, left_coins, right_coins, result))
        
        # 求解
        answer = solve_case(n, k, measurements)
        print(answer)
except EOFError:
    pass
