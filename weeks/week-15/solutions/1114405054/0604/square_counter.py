"""平方數計數 — 實作檔

計算區間 [a, b] 內完全平方數的個數
"""

import math


def count_squares(a: int, b: int) -> int:
    """
    回傳區間 [a, b] 內完全平方數的個數。
    
    Args:
        a: 區間起點
        b: 區間終點
        
    Returns:
        區間內完全平方數的個數
        
    Raises:
        ValueError: 如果 a > b
    """
    if a > b:
        raise ValueError("a must be <= b")
    
    # 計算最小的完全平方數根：ceil(sqrt(a))
    min_sqrt = math.ceil(math.sqrt(a))
    
    # 計算最大的完全平方數根：floor(sqrt(b))
    max_sqrt = math.floor(math.sqrt(b))
    
    # 若最小根大於最大根，表示區間內沒有完全平方數
    if min_sqrt > max_sqrt:
        return 0
    
    # 回傳個數
    return max_sqrt - min_sqrt + 1
