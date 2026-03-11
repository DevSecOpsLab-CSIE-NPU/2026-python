"""
測試程式碼 - UVA 299 Train Swapping (ZeroJudge e561)

【題目說明】
  計算將火車車廂從當前順序排到 1, 2, ..., L 所需的
  最少相鄰交換次數。

【解法說明】
  最少相鄰交換次數 = 陣列的「逆序數（inversion count）」。
  逆序數定義：所有 (i, j) 組合中，i < j 且 arr[i] > arr[j] 的數量。
  L ≤ 50，使用 O(n²) 雙層迴圈直接計算即可。
"""

# ── 解法核心 ────────────────────────────────────────────
def count_inversions(arr):
    """
    計算陣列的逆序數（等於最少相鄰交換次數）。

    參數：
      arr : 車廂排列的整數列表

    回傳：
      逆序數（int）
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1   # 發現一對逆序，計數加一
    return count


# ── 測試函式 ────────────────────────────────────────────
def run_tests():
    """執行所有測試案例，比對實際輸出與預期輸出。"""

    # 每筆測試：(車廂排列, 預期最少交換次數)
    test_cases = [
        ([1, 2, 3],       0),   # 已排序，不需要交換
        ([3, 2, 1],       3),   # 完全反序，需 3 次
        ([3, 1, 2],       2),   # 需 2 次
        ([4, 3, 2, 1],    6),   # 完全反序，需 6 次 (4*3/2)
        ([2, 1, 3, 4],    1),   # 只有一對逆序
        ([1],             0),   # 單一車廂，不需交換
        ([2, 3, 1],       2),   # 2>1, 3>1，共 2 對逆序
        ([1, 3, 2, 4, 5], 1),   # 只有 3>2 一對逆序
    ]

    passed = 0
    failed = 0

    print("=" * 55)
    print("UVA 299 測試結果")
    print("=" * 55)

    for arr, expected in test_cases:
        result = count_inversions(arr)
        status = "PASS" if result == expected else "FAIL"

        if result == expected:
            passed += 1
        else:
            failed += 1

        # 輸出格式與題目相同
        print(f"[{status}]  輸入: {arr}")
        print(f"       輸出: Optimal train swapping takes {result} swaps.  (預期: {expected})")

    print("-" * 55)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


# ── 主程式 ──────────────────────────────────────────────
if __name__ == "__main__":
    run_tests()
