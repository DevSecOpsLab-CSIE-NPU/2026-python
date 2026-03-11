"""
測試程式碼 - UVA 100 The 3n+1 Problem
ZeroJudge: c039

【題目說明】
  給定區間 [i, j]，找出區間內所有數的 Collatz 數列長度（cycle-length）的最大值。

【解法說明】
  1. 使用記憶化（memoization）快取已計算過的 cycle-length，避免重複計算。
  2. 對每個輸入的 (i, j) 取區間最小值與最大值，掃描整個區間求最大值。
  3. 輸出時保持原始 i, j 順序（不按大小排序）。
"""

import sys

# ── 解法核心 ────────────────────────────────────────────
# 記憶化字典：key = n，value = n 的 cycle-length
memo = {1: 1}


def cycle_length(n):
    """迭代式記憶化計算 n 的 cycle-length。"""
    path = []
    current = n

    # 不斷前進直到遇到已知結果
    while current not in memo:
        path.append(current)
        if current % 2 == 0:
            current = current // 2      # 偶數：除以 2
        else:
            current = 3 * current + 1   # 奇數：3n+1

    # 從已知結果往回填入路徑中每個節點
    base = memo[current]
    for i, val in enumerate(reversed(path)):
        memo[val] = base + i + 1

    return memo[n]


def max_cycle_in_range(i, j):
    """計算 [min(i,j), max(i,j)] 區間內的最大 cycle-length。"""
    lo, hi = min(i, j), max(i, j)
    return max(cycle_length(n) for n in range(lo, hi + 1))


# ── 測試函式 ────────────────────────────────────────────
def run_tests():
    """執行所有測試案例，比對實際輸出與預期輸出。"""

    # 每筆測試：(i, j, 預期最大 cycle-length)
    test_cases = [
        (1,    10,   20),   # 區間 [1,10]，最大值為 9 的 cycle-length = 20
        (100,  200, 125),   # 題目提供的範例
        (201,  210,  89),   # 題目提供的範例
        (900, 1000, 174),   # 題目提供的範例
        (10,    1,   20),   # 注意：i > j 也要能正確處理（區間反向）
        (22,   22,   16),   # 單一數字：22 的 cycle-length = 16
        (1,     1,    1),   # 邊界：最小值 1，cycle-length = 1
    ]

    passed = 0
    failed = 0

    print("=" * 50)
    print("UVA 100 測試結果")
    print("=" * 50)

    for i, j, expected in test_cases:
        result = max_cycle_in_range(i, j)
        status = "PASS" if result == expected else "FAIL"

        if result == expected:
            passed += 1
        else:
            failed += 1

        # 輸出測試結果，格式與題目輸出相同
        print(f"[{status}]  輸入: {i} {j}  →  輸出: {i} {j} {result}  (預期: {expected})")

    print("-" * 50)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


# ── 主程式 ──────────────────────────────────────────────
if __name__ == "__main__":
    # 若直接執行此檔案，進行測試
    run_tests()
