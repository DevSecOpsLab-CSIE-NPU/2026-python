def solve_hartals_easy(n_days: int, parties: list[int]) -> int:
    """
    計算因為政黨罷會 (hartals) 而損失的工作天數。
    這是一個更容易記憶且簡潔的版本（利用 Python 集合的特性）。
    """
    # 步驟 1: 使用集合 (Set) 來記錄有發生罷會的所有日期
    # 對於每個政黨的罷會參數 p，產生從 p 開始，間隔為 p，直到 n_days 為止的所有罷會天數
    hartal_days = set()
    for p in parties:
        # range(p, n_days + 1, p) 會產生所有 p 的倍數
        # update() 將這些天數加入集合中，因為是集合，重複的天數會自動被過濾掉
        hartal_days.update(range(p, n_days + 1, p))
        
    # 步驟 2: 計算這些罷會天數中，有多少天「不是」星期五或星期六
    # d % 7 != 6 代表不是星期五
    # d % 7 != 0 代表不是星期六
    # 搭配生成器表示式 (Generator expression) 和 sum()，計算符合條件的天數
    return sum(1 for d in hartal_days if d % 7 != 6 and d % 7 != 0)
