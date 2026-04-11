"""
測試程式碼 - UVA 490 Rotating Sentences (ZeroJudge c045)
"""


def rotate_90_clockwise(lines):
    if not lines:
        return []
    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]
    nrows = len(padded)
    result = []
    for j in range(max_width):
        new_row = ''.join(padded[nrows - 1 - i][j] for i in range(nrows))
        result.append(new_row)
    return result


def run_tests():
    test_cases = [
        (["HELLO", "WORLD"], ["WH", "OE", "RL", "LL", "DO"]),
        (["ABC"], ["A", "B", "C"]),
        (["HI", "HELLO"], ["HH", "EI", "L ", "L ", "O "]),
        (["AB", "C "], ["CA", " B"]),
        (["X"], ["X"]),
    ]

    passed = 0
    failed = 0
    print("=" * 55)
    print("UVA 490 測試結果")
    print("=" * 55)

    for idx, (lines, expected) in enumerate(test_cases, 1):
        result = rotate_90_clockwise(lines)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"[{status}]  測試案例 {idx}")
        print(f"       輸入  : {lines}")
        print(f"       輸出  : {result}")
        if status == "FAIL":
            print(f"       預期  : {expected}")

    print("-" * 55)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


if __name__ == "__main__":
    run_tests()