import sys

def solve():
    # 讀取所有輸入並依空白分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # 第一個數字是測試資料組數 M
        num_datasets_str = next(iterator, None)
        if num_datasets_str is None:
            return
        M = int(num_datasets_str)
    except StopIteration:
        return
        
    for i in range(M):
        try:
            # 讀取 N (硬幣數) 和 K (秤重次數)
            N = int(next(iterator))
            K = int(next(iterator))
        except StopIteration:
            break
            
        # 使用集合來追蹤可能的假幣
        # potential_light: 可能是較輕的假幣
        # potential_heavy: 可能是較重的假幣
        all_coins = set(range(1, N + 1))
        potential_light = set(all_coins)
        potential_heavy = set(all_coins)
        
        for _ in range(K):
            try:
                # 讀取這次秤重每邊的硬幣數量 Pi
                P = int(next(iterator))
                
                left = []
                for _ in range(P):
                    left.append(int(next(iterator)))
                    
                right = []
                for _ in range(P):
                    right.append(int(next(iterator)))
                    
                operator = next(iterator)
                
                left_set = set(left)
                right_set = set(right)
                on_scale = left_set | right_set
                off_scale = all_coins - on_scale
                
                if operator == '=':
                    # 平衡：天平上的所有硬幣都是真的
                    potential_light -= on_scale
                    potential_heavy -= on_scale
                elif operator == '<':
                    # 左邊輕，右邊重
                    # 1. 不在该次秤重中的硬币一定是真的
                    potential_light -= off_scale
                    potential_heavy -= off_scale
                    
                    # 2. 假币如果是轻的，一定在左边 (不能在右边)
                    potential_light -= right_set
                    
                    # 3. 假币如果是重的，一定在右边 (不能在左边)
                    potential_heavy -= left_set
                    
                elif operator == '>':
                    # 左邊重，右邊輕
                    # 1. 不在该次秤重中的硬币一定是真的
                    potential_light -= off_scale
                    potential_heavy -= off_scale
                    
                    # 2. 假币如果是轻的，一定在左边 (不能在左边)
                    potential_light -= left_set
                    
                    # 3. 假币如果是重的，一定在左边 (不能在右边)
                    potential_heavy -= right_set
                    
            except StopIteration:
                break
                
        # 最終可能的假幣是兩集合的聯集
        candidates = list(potential_light | potential_heavy)
        
        # 輸出格式要求：每組測試資料間輸出一空白列
        if i > 0:
            print()
            
        # 如果候選名單只有 1 個，則找到假幣
        if len(candidates) == 1:
            print(candidates[0])
        else:
            # 無法唯一確定或沒有候選者 (照題目邏輯通常是有一個)
            print(0)

if __name__ == "__main__":
    solve()
