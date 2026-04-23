# 檔名: q948-easy.py
# 這是找假幣問題 (False coin) 的簡易好記版 (Easy Version)

import sys

# 1. 一次把所有輸入讀進來，用空白/換行切成一個一個的純字串列表
input_data = sys.stdin.read().split()

if input_data:
    M = int(input_data[0])  # 測資筆數
    idx = 1
    
    for t in range(M):
        N = int(input_data[idx])
        K = int(input_data[idx+1])
        idx += 2
        
        # 2. 建立兩張嫌疑犯名單，假設一開始大家都有嫌疑 (True 代表可能是假幣)
        can_be_heavy = [True] * (N + 1)
        can_be_light = [True] * (N + 1)
        
        for _ in range(K):
            P = int(input_data[idx])
            idx += 1
            
            # 讀取左盤與右盤的硬幣
            left = [int(x) for x in input_data[idx : idx + P]]
            idx += P
            right = [int(x) for x in input_data[idx : idx + P]]
            idx += P
            
            result = input_data[idx]
            idx += 1
            
            # 把放在天平上的硬幣集合起來，用 set() 尋找時速度會比較快
            on_scale = set(left + right)
            
            # 3. 根據秤重結果「洗清嫌疑 (將 True 變成 False)」
            if result == '=':
                # 天平平衡：盤子上的硬幣全都是真的，洗清嫌疑
                for x in on_scale:
                    can_be_heavy[x] = False
                    can_be_light[x] = False
            elif result == '<':
                # 左輕右重
                for x in range(1, N + 1):
                    if x not in on_scale:
                        can_be_heavy[x] = False  # 沒放在不平衡天平上的，絕對是真的
                        can_be_light[x] = False
                for x in left:
                    can_be_heavy[x] = False  # 左邊比較輕，不可能有「重假幣」
                for x in right:
                    can_be_light[x] = False  # 右邊比較重，不可能有「輕假幣」
            elif result == '>':
                # 左重右輕
                for x in range(1, N + 1):
                    if x not in on_scale:
                        can_be_heavy[x] = False  # 沒放在不平衡天平上的，絕對是真的
                        can_be_light[x] = False
                for x in left:
                    can_be_light[x] = False  # 左邊比較重，不可能有「輕假幣」
                for x in right:
                    can_be_heavy[x] = False  # 右邊比較輕，不可能有「重假幣」
                    
        # 4. 統計最後有幾個硬幣還有嫌疑
        suspects = []
        for i in range(1, N + 1):
            if can_be_heavy[i] or can_be_light[i]:
                suspects.append(i)
                
        # 依題目要求，多筆測資的輸出之間需要有一行空行
        if t > 0:
            print()
            
        # 只有「唯一」一個嫌疑犯時，才能確定它是假幣
        if len(suspects) == 1:
            print(suspects[0])
        else:
            print(0)