"""
紅燈測試：二分搜尋效能（Binary Search Efficiency）- 第四題

測試目標：驗證線性搜尋與二分搜尋的輸出格式與比較次數
預期狀態：所有測試失敗（尚未實作解題檔）
"""


def run_tests():
    print("=" * 70)
    print("開始執行紅燈測試（Red Light Tests）- 二分搜尋效能")
    print("=" * 70)

    test_cases = [
        ([12, 37, 58, 80, 95, 101, 138, 160, 188, 210], 138, "基本情況：目標值存在於中間"),
        ([5, 8, 13, 21, 34, 55, 89], 5, "邊界情況：目標值在最前面"),
        ([3, 10, 17, 24, 31, 38], 40, "邊界情況：目標值不存在"),
        ([1, 4, 7, 9, 12, 15, 18, 21], 21, "邊界情況：目標值在最後面"),
    ]

    passed = 0
    failed = 0

    for index, (numbers, target, description) in enumerate(test_cases, 1):
        try:
            from solution import linear_search, binary_search

            linear_found, linear_idx, linear_cmp = linear_search(numbers, target)
            binary_found, binary_idx, binary_cmp = binary_search(numbers, target)

            expected_found = target in numbers
            expected_idx = numbers.index(target) if expected_found else -1

            if (
                linear_found == expected_found
                and binary_found == expected_found
                and linear_idx == expected_idx
                and binary_idx == expected_idx
            ):
                print(f"✓ Test Case {index} 通過：{description}")
                print(f"  陣列: {numbers}")
                print(f"  目標: {target}")
                print(f"  Linear: found={linear_found}, idx={linear_idx}, cmp={linear_cmp}")
                print(f"  Binary: found={binary_found}, idx={binary_idx}, cmp={binary_cmp}")
                passed += 1
            else:
                print(f"✗ Test Case {index} 失敗：{description}")
                print(f"  陣列: {numbers}")
                print(f"  目標: {target}")
                print(f"  期望 found={expected_found}, idx={expected_idx}")
                print(f"  Linear: found={linear_found}, idx={linear_idx}, cmp={linear_cmp}")
                print(f"  Binary: found={binary_found}, idx={binary_idx}, cmp={binary_cmp}")
                failed += 1
        except (ImportError, ModuleNotFoundError, NameError, AttributeError):
            print(f"✗ Test Case {index} 失敗：{description}")
            print(f"  陣列: {numbers}")
            print(f"  目標: {target}")
            print(f"  錯誤: 解題檔未實作或函數不存在")
            failed += 1
        except Exception as exc:
            print(f"✗ Test Case {index} 失敗：{description}")
            print(f"  陣列: {numbers}")
            print(f"  目標: {target}")
            print(f"  錯誤: {exc}")
            failed += 1

        print()

    print("=" * 70)
    if passed == 0 and failed == len(test_cases):
        print(f"❌ 紅燈測試：{failed}/{len(test_cases)} 失敗（正常，解題檔尚未實作）")
    else:
        print(f"✓ 測試結果：{passed}/{len(test_cases)} 通過")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
