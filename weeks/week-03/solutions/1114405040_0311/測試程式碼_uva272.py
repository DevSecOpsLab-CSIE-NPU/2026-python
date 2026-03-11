"""
測試程式碼 - UVA 272 TeX Quotes (ZeroJudge c007)

【題目說明】
  將文字中的普通雙引號「"」依序替換：
    第奇數個 " → ``（兩個 backtick，代表開引號）
    第偶數個 " → ''（兩個 apostrophe，代表閉引號）
  其他字元原樣保留。

【解法說明】
  維護布林旗標 is_open：
    True  → 下一個 " 換成 ``
    False → 下一個 " 換成 ''
  每替換一次就切換旗標。
"""

# ── 解法核心 ────────────────────────────────────────────
def convert_quotes(text):
    """
    將字串 text 中的雙引號依序替換為 `` 和 ''。

    參數：
      text : 可能橫跨多行的原始字串（含換行符）

    回傳：
      替換後的字串
    """
    result = []
    is_open = True   # True = 下一個 " 替換為開引號 ``

    for ch in text:
        if ch == '"':
            if is_open:
                result.append('``')   # 開引號：兩個 backtick
            else:
                result.append("''")   # 閉引號：兩個 apostrophe
            is_open = not is_open     # 切換開/閉狀態
        else:
            result.append(ch)         # 非雙引號字元直接保留

    return ''.join(result)


# ── 測試函式 ────────────────────────────────────────────
def run_tests():
    """執行所有測試案例，比對實際輸出與預期輸出。"""

    # 每筆測試：(輸入字串, 預期輸出字串)
    test_cases = [
        (
            # 測試案例 1：題目原始範例
            '"To be or not to be," quoth the bard, "that is the question."\n',
            "``To be or not to be,'' quoth the bard, ``that is the question.''\n"
        ),
        (
            # 測試案例 2：多行輸入，引號跨行切換
            '"Hello"\n"World"\n',
            "``Hello''\n``World''\n"
        ),
        (
            # 測試案例 3：引號之間有其他標點
            'She said "yes" and he said "no".\n',
            "She said ``yes'' and he said ``no''.\n"
        ),
        (
            # 測試案例 4：無雙引號的文字，原樣輸出
            'No quotes here.\n',
            'No quotes here.\n'
        ),
        (
            # 測試案例 5：引號緊鄰
            '""',
            "``''"
        ),
    ]

    passed = 0
    failed = 0

    print("=" * 60)
    print("UVA 272 測試結果")
    print("=" * 60)

    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = convert_quotes(inp)
        status = "PASS" if result == expected else "FAIL"

        if result == expected:
            passed += 1
        else:
            failed += 1

        # 輸出時隱藏換行符以利閱讀
        inp_display      = repr(inp)
        result_display   = repr(result)
        expected_display = repr(expected)

        print(f"[{status}]  測試案例 {idx}")
        print(f"       輸入   : {inp_display}")
        print(f"       輸出   : {result_display}")
        if status == "FAIL":
            print(f"       預期   : {expected_display}")

    print("-" * 60)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


# ── 主程式 ──────────────────────────────────────────────
if __name__ == "__main__":
    run_tests()
