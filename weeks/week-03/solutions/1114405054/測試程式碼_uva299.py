"""
測試程式碼 - UVA 299 Train Swapping (ZeroJudge e561)
"""


def count_inversions(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


def run_tests():
    test_cases = [
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
        ([3, 1, 2], 2),
        ([4, 3, 2, 1], 6),
        ([2, 1, 3, 4], 1),
        ([1], 0),
        ([2, 3, 1], 2),
        ([1, 3, 2, 4, 5], 1),
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
        print(f"[{status}]  輸入: {arr}")
        print(f"       輸出: Optimal train swapping takes {result} swaps.  (預期: {expected})")

    print("-" * 55)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


if __name__ == "__main__":
    run_tests()