"""
ZeroJudge c095: 00665 - False coin
題目鏈接: https://zerojudge.tw/ShowProblem?problemid=c095

題目描述:
輸入的第一列有一個整數 M，代表以下有幾組測試資料。
每組測試資料的第一列有2個整數 N 和 K。
N 代表硬幣的數量（1 <= N <= 100），K 是秤重的次數（1 <= K <= 100）。
接下來的 2K 列描述秤重，每連續的2列是一次秤重。
前一列開始有一個數Pi（1 <= Pi <= N/2），代表這次秤重每邊放的硬幣個數，
接下來的前 Pi個數字是左邊的硬幣號碼，後 Pi 個數字是右邊的硬幣號碼。
後一列用 <, >, 或 = 表示秤重的結果。
"""

import sys

def solve():
    # 使用 sys.stdin.read().split() 一次讀取所有輸入
    # split() 會自動跳過所有的空白字符（包含空格、換行、以及題目描述中的空白列）
    # 因此我們只需要依序讀取 token 即可，不需要額外處理空白列
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # 讀取測試資料組數 M
        M_str = next(iterator)
        M = int(M_str)
    except StopIteration:
        return

    first_case = True
    
    for _ in range(M):
        try:
            # 讀取 N (硬幣數) 和 K (秤重次數)
            N = int(next(iterator))
            K = int(next(iterator))
        except StopIteration:
            break
            
        # possible_light[i] = True 表示第 i 枚硬幣有可能是「較輕的假幣」
        # possible_heavy[i] = True 表示第 i 枚硬幣有可能是「較重的假幣」
        possible_light = [True] * (N + 1)
        possible_heavy = [True] * (N + 1)
        
        for _ in range(K):
            # 讀取每次秤重資訊
            # 格式: Pi 左邊硬幣... 右邊硬幣...
            # 下一行: 結果符號
            try:
                Pi = int(next(iterator))
                
                left_coins = []
                for _ in range(Pi):
                    left_coins.append(int(next(iterator)))
                    
                right_coins = []
                for _ in range(Pi):
                    right_coins.append(int(next(iterator)))
                
                result = next(iterator)
                
                left_set = set(left_coins)
                right_set = set(right_coins)
                weighed_coins = left_set | right_set
                
                if result == '=':
                    # 若天平平衡，則台面上的所有硬幣肯定都是真的
                    for coin in weighed_coins:
                        possible_light[coin] = False
                        possible_heavy[coin] = False 
                
                elif result == '<':
                    # 左邊輕，右邊重
                    # 1. 沒上天平的硬幣必定是真的 
                    for i in range(1, N + 1):
                        if i not in weighed_coins:
                            possible_light[i] = False
                            possible_heavy[i] = False
                    
                    # 2. 左邊的硬幣不可能是「重」的
                    for coin in left_set:
                        possible_heavy[coin] = False
                        
                    # 3. 右邊的硬幣不可能是「輕」的
                    for coin in right_set:
                        possible_light[coin] = False
                        
                elif result == '>':
                    # 左邊重，右邊輕
                    # 1. 沒上天平的硬幣必定是真的
                    for i in range(1, N + 1):
                        if i not in weighed_coins:
                            possible_light[i] = False
                            possible_heavy[i] = False
                            
                    # 2. 左邊的硬幣不可能是「輕」的
                    for coin in left_set:
                        possible_light[coin] = False
                        
                    # 3. 右邊的硬幣不可能是「重」的
                    for coin in right_set:
                        possible_heavy[coin] = False

            except StopIteration:
                break
        
        # 掃描所有硬幣，看誰還可能是假幣
        candidates = []
        for i in range(1, N + 1):
            if possible_light[i] or possible_heavy[i]:
                candidates.append(i)
        
        # 輸出格式: 各組測試資料間均有一空白列
        if not first_case:
            print()
        first_case = False
        
        # 若只剩下唯一的嫌疑犯，即為答案
        if len(candidates) == 1:
            print(candidates[0])
        else:
            print(0)

if __name__ == '__main__':
    solve()
