
"""
測試程式碼 - UVA 490 Rotating Sentences (ZeroJudge c045)

【題目說明】
  將多行文字順時針旋轉 90 度輸出：
    - 原本最後一行 → 旋轉後最左欄（由上到下輸出）
    - 原本第一行   → 旋轉後最右欄（由上到下輸出）
  各行長度不足時補空白，形成完整矩形再旋轉。

【解法說明】
  1. 讀取所有行，去掉行末換行符。
  2. 找最大寬度 max_width，每行補空白至相同長度（ljust）。
  3. 旋轉後共輸出 max_width 行，第 j 行 =
       原矩陣第 j 欄，由最後一行掃到第一行（由下往上）。
"""

# ── 解法核心 ────────────────────────────────────────────
def rotate_90_clockwise(lines):
    """
    將多行字串列表順時針旋轉 90 度。

    參數：
      lines : list of str（不含換行符）

    回傳：
      旋轉後的 list of str
    """
    if not lines:
        return []

    # 找最大寬度，補齊空白讓所有行等長
    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]

    nrows = len(padded)   # 原始行數
    result = []

    # 旋轉後共 max_width 行
    for j in range(max_width):
        # 第 j 欄：從最後一行往第一行取字元（由下往上 = 旋轉後由左到右）
        new_row = ''.join(padded[nrows - 1 - i][j] for i in range(nrows))
        result.append(new_row)

    return result


# ── 測試函式 ────────────────────────────────────────────
def run_tests():
    """執行所有測試案例，比對實際輸出與預期輸出。"""

    # 每筆測試：(輸入行列表, 預期輸出行列表)
    test_cases = [
        (
            # 測試案例 1：UVA 490 原題範例（HELLO / WORLD）
            ["HELLO", "WORLD"],
            ["WH", "OE", "RL", "LL", "DO"]
        ),
        (
            # 測試案例 2：只有一行
            ["ABC"],
            ["A", "B", "C"]
        ),
        (
            # 測試案例 3：行長度不同，需補空白
            # 原矩陣（補齊後）：
            #   "HI   "
            #   "HELLO"
            # 旋轉後第 0 欄由下往上: H, H → "HH"
            #         第 1 欄由下往上: E, I → "EI"
            #         第 2 欄由下往上: L, ' ' → "L "
            #         第 3 欄由下往上: L, ' ' → "L "
            #         第 4 欄由下往上: O, ' ' → "O "
            ["HI", "HELLO"],
            ["HH", "EI", "L ", "L ", "O "]
        ),
        (
            # 測試案例 4：含空白字元的行
            ["AB", "C "],
            ["CA", "  B"]  # 旋轉：第0欄下往上 C,A；第1欄 ' ',B
            # 修正：原矩陣 "AB"/"C "
            #   第 0 欄由下往上: C, A → "CA"
            #   第 1 欄由下往上: ' ', B → " B"
        ),
        (
            # 測試案例 5：單一字元
            ["X"],
            ["X"]
        ),
    ]

    # 修正測試案例 4 的預期輸出（剛才有筆誤）
    test_cases[3] = (
        ["AB", "C "],
        ["CA", " B"]
    )

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


# ── 主程式 ──────────────────────────────────────────────
if __name__ == "__main__":
    run_tests()
