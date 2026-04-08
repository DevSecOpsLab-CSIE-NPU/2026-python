"""
UVA 299 - Train Car Swapping (簡易版)
=====================================
此程式解決火車車廂排序問題，計算將車廂從任意排列
恢復到正確順序（1, 2, ..., L）所需的最少相鄰交換次數。

====================================================
【題目理解】
====================================================
在火車站有「車箱置換員」的工作是将火車車廂重新排列。
每次只能交換兩個相鄰的車廂，目標是將車廂按照編號 1 到 L 的順序排好。

問題本质：計算最少需要多少次「相鄰交換」才能將排列恢復為有序。

====================================================
【解題核心概念 - 逆序列對 (Inversion Pairs)】
====================================================
什麼是逆序列對？
- 在排列中，如果較大的數字出現在較小數字之前，就稱為一個「逆序列對」
- 正式定義：arr[i] > arr[j] 且 i < j (i 在 j 前面，但 arr[i] 比 arr[j] 大)

為什麼逆序列對數 = 最少交換次數？
- 每次相鄰交換只能消除一個逆序列對
- 例如 [3,1,2]：
  - (3,1) 是逆序列對 → 交換後變成 [1,3,2]
  - (3,2) 是逆序列對 → 交換後變成 [1,2,3]
  - 需要 2 次交換，正好等於逆序列對數量

====================================================
【演算法說明】
====================================================
本程式使用「暴力法」（雙重迴圈）計算逆序列對數：

1. 遍历陣列中的每個位置 i（從 0 到 n-1）
2. 對於每個位置 i，再遍历 i 之後的所有位置 j
3. 如果 arr[i] > arr[j]，表示找到一个逆序列對，計數 +1

時間複雜度：O(n²) - 因為是雙重迴圈
空間複雜度：O(1) - 只用了一個計數器

為什麼這個方法可行？
- 因為 L ≤ 50（題目限制），n² = 2500，最大才 1225 次計算
- 即使最差情況也能快速完成，不需要複雜的合併排序

====================================================
【範例演練】
====================================================
範例 1：[1, 2, 3]
- i=0: arr[0]=1，分別和 arr[1]=2、arr[2]=3 比較，1不大於兩者
- i=1: arr[1]=2，和 arr[2]=3 比較，2不大於3
- i=2: 沒有後面的元素
- 逆序列對數 = 0 → 已經有序，不需要交換

範例 2：[2, 1]
- i=0: arr[0]=2，和 arr[1]=1 比較，2 > 1，找到 1 個逆序列對
- 逆序列對數 = 1 → 需要交換 1 次

範例 3：[3, 1, 2]
- i=0: arr[0]=3
  - 和 arr[1]=1 比較：3 > 1 → 逆序列對 +1 (3,1)
  - 和 arr[2]=2 比較：3 > 2 → 逆序列對 +1 (3,2)
- i=1: arr[1]=1，和 arr[2]=2 比較：1不大於2
- 逆序列對數 = 2 → 需要交換 2 次

====================================================
【輸入輸出格式】
====================================================
輸入：
- 第一行：測資數量 N
- 每組測資：
  - 第一行：火車長度 L
  - 第二行：L 個整數（車廂的當前排列）

輸出：
- 每組測資一行：「Optimal train swapping takes X swaps.」

====================================================

"""

import unittest
from typing import List


def count_inversions(arr: List[int]) -> int:
    """
    計算陣列中的逆序列對數量。

    【核心邏輯】
    - 使用雙重迴圈遍历整個陣列
    - 外層迴圈 i：遍歷每個元素作為「比較的基準」
    - 內層迴圈 j：遍歷i之後的元素，找尋比arr[i]小的元素
    - 如果 arr[i] > arr[j]，表示找到一個「較大的數在前面」的情況

    Args:
        arr: 輸入的整數排列（車廂順序）

    Returns:
        逆序列對的數量（即將車廂排序所需的最少交換次數）

    【範例】
    arr = [3, 1, 2]
    - i=0, j=1: 3 > 1 → 計數+1
    - i=0, j=2: 3 > 2 → 計數+1
    - i=1, j=2: 1 > 2 → 不計數
    - 總計：2 個逆序列對
    """
    inv_count = 0  # 計數器，記錄找到多少個逆序列對
    n = len(arr)  # 陣列長度

    # 外層迴圈：遍歷陣列中的每個位置（除了最後一個）
    for i in range(n):
        # 內層迴圈：遍積当前位置之後的所有位置
        for j in range(i + 1, n):
            # 如果前面的元素比後面的元素大，就是逆序列對
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


def solve_case(train: List[int]) -> int:
    """
    解決單筆測資，計算將火車車廂排序所需的最少交換次數。

    這只是一個包裝函數，直接調用 count_inversions 計算逆序列對數。
    因為「逆序列對數」正好等於「最少相鄰交換次數」。

    Args:
        train: 車廂的當前排列（ List[int] ）

    Returns:
        最少相鄰交換次數（ int ）
    """
    return count_inversions(train)


def main() -> None:
    """
    主函數，處理標準輸入輸出。

    【輸入格式說明】
    - 第一行讀取測資數量 N
    - 接下來依序讀取每組測資：
      1. 讀取火車長度 L
      2. 讀取 L 個整數作為排列

    【輸出格式說明】
    - 每組測資輸出一行，格式為：
      「Optimal train swapping takes X swaps.」
    - 其中 X 是計算出的最少交換次數
    """
    import sys

    # 讀取所有輸入並分割為字串列表
    data = sys.stdin.read().strip().split()
    if not data:  # 如果沒有輸入，直接返回
        return

    it = iter(data)  # 建立迭代器方便依序讀取
    n = int(next(it))  # 讀取測資數量

    results = []  # 存放每組測資的輸出結果

    # 依序處理每組測資
    for _ in range(n):
        l = int(next(it))  # 讀取火車長度
        # 讀取 L 個車廂編號
        train = [int(next(it)) for _ in range(l)]
        # 計算最少交換次數
        swaps = solve_case(train)
        # 格式化輸出結果
        results.append(f"Optimal train swapping takes {swaps} swaps.")

    # 輸出所有結果，每行一個
    sys.stdout.write("\n".join(results))


# ==================== 單元測試 ====================


class TestUVA299Easy(unittest.TestCase):
    """
    UVA 299 題目的單元測試（簡易版）

    使用 unittest 框架編寫測試，針對各種边界情況和典型範例進行驗證。
    """

    def test_already_sorted(self):
        """已排序的車廂應該需要 0 次交換"""
        train = [1, 2, 3, 4, 5]
        self.assertEqual(solve_case(train), 0)

    def test_reverse_order(self):
        """完全反向排序的車廂"""
        train = [5, 4, 3, 2, 1]
        self.assertEqual(solve_case(train), 10)

    def test_example(self):
        """基本範例"""
        train = [3, 1, 2]
        self.assertEqual(solve_case(train), 2)

    def test_single_car(self):
        """單一車廂（边界情況）"""
        train = [1]
        self.assertEqual(solve_case(train), 0)

    def test_two_cars_ordered(self):
        """兩個已排序的車廂"""
        train = [1, 2]
        self.assertEqual(solve_case(train), 0)

    def test_two_cars_reversed(self):
        """兩個反向的車廂"""
        train = [2, 1]
        self.assertEqual(solve_case(train), 1)

    def test_long_train(self):
        """較長的火車 L=50（最大限制）"""
        # 反向排列 50 個數，逆序列對數 = C(50,2) = 1225
        train = list(range(50, 0, -1))
        self.assertEqual(solve_case(train), 1225)

    def test_empty_train(self):
        """空排列（边界情況）"""
        train = []
        self.assertEqual(solve_case(train), 0)


if __name__ == "__main__":
    # 當直接執行此檔案時，執行單元測試
    unittest.main()
