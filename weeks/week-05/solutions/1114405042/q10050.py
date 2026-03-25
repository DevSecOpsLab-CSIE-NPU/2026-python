def solve_hartals(n_days: int, parties: list[int]) -> int:
    """
    計算在 N 天內，因為政黨罷會 (hartals) 而損失的工作天數。
    
    :param n_days: 模擬的總天數
    :param parties: 一個包含各個政黨罷會參數的列表
    :return: 損失的工作天數
    """
    lost_days = 0
    
    # 迴圈跑過每一天，天數從 1 到 n_days (包含 n_days)
    for day in range(1, n_days + 1):
        # 判斷是否為星期五或星期六 (假日)
        # 第一天 (day 1) 是星期天，所以：
        # day % 7 == 6 代表星期五
        # day % 7 == 0 代表星期六
        if day % 7 == 6 or day % 7 == 0:
            continue # 如果是假日，即使有罷會也不算損失工作天，直接跳過這一天
            
        # 檢查今天是否有任何一個政黨發起罷會
        has_hartal = False
        for p in parties:
            if day % p == 0: # 如果天數是該政黨罷會參數的倍數，代表今天該政黨會罷會
                has_hartal = True
                break # 只要有一個政黨罷會，這天就算作罷會日，不用繼續檢查其他政黨
                
        # 如果今天有罷會（且不是假日），則損失的工作天數加 1
        if has_hartal:
            lost_days += 1
            
    return lost_days
