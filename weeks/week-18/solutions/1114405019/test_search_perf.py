"""
針對 search_perf.py 的單元測試。

測重點：linear_search / binary_search 的正確性（FOUND / NOT FOUND / idx / cmp），
以及 generate_sorted_array 對「K 在不在陣列裡」的控制能力。
timeit 量測與畫圖（plot_radar）不在此檔測試，因為效能數字會隨機器浮動、
畫圖也沒有「正確答案」可斷言。
"""

import math

from search_perf import binary_search, generate_sorted_array, linear_search


def test_binary_found_idx_matches_value():
    """找到時，回報的 idx 必須真的指向 target，而不是隨便回一個數字。"""
    arr = [2, 4, 6, 8, 10, 12, 14]
    idx, cmp = binary_search(arr, 10)
    assert idx is not None
    assert arr[idx] == 10
    assert cmp >= 1


def test_binary_not_found_in_gap_between_elements():
    """target 落在兩個元素中間，最容易因為 off-by-one 誤判成鄰居元素。"""
    arr = [1, 3, 5, 7, 9]
    idx, cmp = binary_search(arr, 4)
    assert idx is None
    assert cmp >= 1


def test_binary_not_found_below_minimum():
    """target 比陣列最小值還小，迴圈必須正確收斂到 NOT FOUND，不能誤判邊界。"""
    arr = [10, 20, 30]
    idx, _ = binary_search(arr, 1)
    assert idx is None


def test_binary_not_found_above_maximum():
    """target 比陣列最大值還大，同樣是邊界收斂測試。"""
    arr = [10, 20, 30]
    idx, _ = binary_search(arr, 99)
    assert idx is None


def test_single_element_found():
    """陣列只有 1 個元素，且該元素恰為 target：最小規模的 FOUND 案例。"""
    idx, cmp = binary_search([5], 5)
    assert idx == 0
    assert cmp == 1


def test_single_element_not_found():
    """陣列只有 1 個元素，且該元素不是 target：最小規模的 NOT FOUND 案例。"""
    idx, cmp = binary_search([5], 7)
    assert idx is None
    assert cmp == 1


def test_first_element_boundary():
    """target 剛好是陣列第一個元素，確認迴圈條件沒有漏掉左邊界。"""
    arr = [2, 4, 6, 8, 10]
    idx, _ = binary_search(arr, 2)
    assert idx == 0


def test_last_element_boundary():
    """target 剛好是陣列最後一個元素，確認迴圈條件沒有漏掉右邊界。"""
    arr = [2, 4, 6, 8, 10]
    idx, _ = binary_search(arr, 10)
    assert idx == len(arr) - 1


def test_binary_cmp_upper_bound():
    """
    二分搜尋的比較次數理論上限約為 ceil(log2(m)) + 1。
    如果超出這個量級，代表搜尋邏輯（例如沒有正確折半）有問題。
    """
    arr = list(range(0, 2000, 2))  # m = 1000 個唯一升冪整數
    upper_bound = math.ceil(math.log2(len(arr))) + 1
    for target in (-5, 0, 1, 998, 1998, 50000):
        _, cmp = binary_search(arr, target)
        assert cmp <= upper_bound


def test_linear_binary_consistency_found_and_not_found():
    """
    交叉驗證：同一陣列、同一 target，linear 與 binary 的 FOUND/NOT FOUND
    結果必須一致；陣列為唯一值時，FOUND 的 idx 也必須一致。
    若兩者結果不一致，代表至少一個演算法寫錯了。
    """
    arr = generate_sorted_array(m=500, target=119, present=True, seed=1)
    for target in (119, -999, arr[0], arr[-1], arr[len(arr) // 2] + 1):
        l_idx, _ = linear_search(arr, target)
        b_idx, _ = binary_search(arr, target)
        assert (l_idx is None) == (b_idx is None)
        if l_idx is not None:
            assert l_idx == b_idx


def test_generate_sorted_array_present_guarantees_target():
    """present=True 時，target 必須恰好出現一次，且陣列升冪排列。"""
    arr = generate_sorted_array(m=300, target=119, present=True, seed=42)
    assert arr.count(119) == 1
    assert arr == sorted(arr)


def test_generate_sorted_array_absent_guarantees_no_target():
    """present=False 時，target 絕對不能出現在陣列中。"""
    arr = generate_sorted_array(m=300, target=119, present=False, seed=42)
    assert 119 not in arr
    assert arr == sorted(arr)
