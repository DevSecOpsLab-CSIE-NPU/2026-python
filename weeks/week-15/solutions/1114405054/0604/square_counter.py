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
    
    # TODO: 待實作
    return 0
