def solve_probability(n: int, p: float, i: int) -> float:
    """
    計算第 i 個玩家在有 N 個玩家的遊戲中獲勝的機率。
    這是一個無限等比級數的問題：
    第一輪贏的機率：前 (i-1) 個人都失敗，第 i 個人成功 -> (1-p)^(i-1) * p
    第二輪贏的機率：第一輪所有 N 個人都失敗，接著前 (i-1) 個人也失敗，第 i 個人成功 -> (1-p)^N * (1-p)^(i-1) * p
    ...
    因此這是一個首項 a = (1-p)^(i-1) * p，公比 r = (1-p)^N 的無窮等比級數。
    總和 S = a / (1 - r)
    
    :param n: 總玩家人數
    :param p: 單次成功的機率
    :param i: 目標玩家的順位 (1 到 N)
    :return: 獲勝機率 (浮點數)
    """
    # 如果成功的機率是 0，那麼任何人都無法獲勝，機率為 0.0
    if p == 0:
        return 0.0
        
    # q 代表失敗的機率
    q = 1.0 - p
    
    # 首項 a: 第 i 個玩家在第一輪就獲勝的機率
    # 也就是前面 i-1 個人都失敗，輪到他時成功
    first_term_a = (q ** (i - 1)) * p
    
    # 公比 r: 所有人經過一輪 (N 個人) 後都沒有人獲勝的機率
    common_ratio_r = q ** n
    
    # 根據無窮等比級數求和公式：S = a / (1 - r)
    probability = first_term_a / (1.0 - common_ratio_r)
    
    return probability
