"""
UVA 10268 - 雞蛋掉落問題 (簡化版本)

題目：N 顆雞蛋，F 層樓。每次從某層掉雞蛋，判斷樓層是否臨界點。
      求最少試驗次數（最壞情況下）確定臨界樓層。

核心思想：動態規劃，狀態 dp[e] = 現有 e 顆雞蛋時，
         目前試驗次數下最多能測多少層樓。
         
        逆向迭代是關鍵：避免 dp[e] 新值覆蓋 dp[e-1] 舊值。
"""

from __future__ import annotations

import sys
from typing import Optional, List


def minimum_trials(eggs: int, floors: int) -> Optional[int]:
    """
    計算最少試驗次數（不超過 63）。
    
    時間複雜度: O(63 × eggs) = O(eggs)
    空間複雜度: O(eggs)
    
    參數：
        eggs: 雞蛋數量（1 ≤ eggs）
        floors: 樓層數（1 ≤ floors ≤ 100000）
    
    回傳：
        最少試驗次數（≤63），或 None if 超過 63 次
    """
    # 邊界條件檢查
    if floors <= 0:
        return 0
    if eggs <= 0:
        return None
    
    # dp[e] = 有 e 顆雞蛋、當前試驗次數時，最多能測多少層
    # 初始值：0 顆雞蛋無法測任何層，1 顆雞蛋只能線性搜索
    dp = [0] * (eggs + 1)
    
    # 逐漸增加試驗次數（最多 63 次）
    for trials in range(1, 64):
        # *** 重點：反向迭代 ***
        # 為什麼反向？因為 dp[e] 新值使用 dp[e-1] 舊值
        # 若正向迭代，dp[e-1] 已被本輪更新，無法得到上一輪的值
        # 例如當 e=2 時，我們需要「上一輪的 dp[1]」，不是「本輪新的 dp[1]」
        for e in range(eggs, 0, -1):
            # DP 公式：試驗次數 +1 時，測試範圍擴展
            # 新公式 = 下層能測層數 + 上層能測層數 + 1（中間試驗點）
            # dp[e] += dp[e-1] + 1
            # 或等價：dp[e] = dp[e] + dp[e-1] + 1
            dp[e] = dp[e] + dp[e - 1] + 1
        
        # 提前終止：當最多雞蛋數的測試層數已足夠
        if dp[eggs] >= floors:
            return trials
    
    # 超過 63 次試驗
    return None


def main() -> None:
    """
    主程式：讀取多筆測資（EOF 或 eggs=0 結束）。
    
    輸入格式：
    每行 "eggs floors"（空白分隔）
    直到讀到 "0 0" 或 EOF 結束
    
    輸出格式：
    每行一個整數（最少試驗次數）或文字
    """
    output_lines: List[str] = []
    
    try:
        for line in sys.stdin:
            line = line.strip()
            
            # 跳過空白行
            if not line:
                continue
            
            # 分割第一行輸入
            parts = line.split()
            if len(parts) < 2:
                continue
            
            eggs, floors = int(parts[0]), int(parts[1])
            
            # 終止條件：eggs = 0
            if eggs == 0:
                break
            
            # 計算答案
            trials = minimum_trials(eggs, floors)
            
            # 格式化輸出
            if trials is None:
                output_lines.append("More than 63 trials needed.")
            else:
                output_lines.append(str(trials))
    
    except (EOFError, ValueError):
        # 捕捉輸入結束或轉換錯誤
        pass
    
    # 一次性輸出所有結果（減少 I/O）
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    main()