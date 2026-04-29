"""UVA 10268 - 498-bis (Egg Drop Problem)

簡單版：最少測試次數
"""


def min_trials_needed(k, n):
    """
    k 個雞蛋，n 層樓
    求最少測試次數
    
    使用組合數：最少 t 次試驗能測試的最大樓層數為
    sum(C(t, i)) for i = 1 to min(t, k)
    """
    if k == 0 or n == 0:
        return 0
    if k == 1:
        return n  # 只有 1 個雞蛋，必須從下往上逐層試
    
    # 對於 k >= 2，用組合數計算
    trials = 0
    while True:
        trials += 1
        # 計算 trials 次試驗能測試的最大層數
        max_floors = 0
        c = 1  # C(trials, 0)
        for i in range(1, min(trials, k) + 1):
            c = c * (trials - i + 1) // i
            max_floors += c
        
        if max_floors >= n:
            return trials


def main():
    import sys
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
