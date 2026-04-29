"""UVA 10268 - 498-bis (Egg Drop Problem)

一般版：完整的二項係數實現
"""

import sys


def max_floors(trials, eggs):
    """
    用 trials 次試驗和 eggs 個雞蛋最多能測試的樓層數
    使用二項係數：sum(C(trials, i)) for i in 1..min(trials, eggs)
    """
    result = 0
    c = 1  # C(trials, 0)
    
    for i in range(1, min(trials, eggs) + 1):
        c = c * (trials - i + 1) // i
        result += c
    
    return result


def min_trials_needed(eggs, floors):
    """
    求最少試驗次數
    二分搜尋試驗次數 t，使得 max_floors(t, eggs) >= floors
    """
    if eggs == 0 or floors == 0:
        return 0
    
    # 二分搜尋
    left, right = 1, 64  # 最多 64 次試驗
    
    while left < right:
        mid = (left + right) // 2
        if max_floors(mid, eggs) >= floors:
            right = mid
        else:
            left = mid + 1
    
    return left


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split()
        k, n = int(parts[0]), int(parts[1])
        
        if k == 0:
            break
        
        trials = min_trials_needed(k, n)
        
        if trials > 63:
            print("More than 63 trials needed.")
        else:
            print(trials)


if __name__ == "__main__":
    main()
