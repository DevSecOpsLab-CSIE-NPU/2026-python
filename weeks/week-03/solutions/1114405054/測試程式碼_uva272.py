"""
測試程式碼 - UVA 272 TeX Quotes (ZeroJudge c007)
"""


def convert_quotes(text):
    result = []
    is_open = True
    for ch in text:
        if ch == '"':
            if is_open:
                result.append('``')
            else:
                result.append("''")
            is_open = not is_open
        else:
            result.append(ch)
    return ''.join(result)


def run_tests():
    test_cases = [
        ('"To be or not to be," quoth the bard, "that is the question."\n', "``To be or not to be,'' quoth the bard, ``that is the question.''\n"),
        ('"Hello"\n"World"\n', "``Hello''\n``World''\n"),
        ('She said "yes" and he said "no".\n', "She said ``yes'' and he said ``no''.\n"),
        ('No quotes here.\n', 'No quotes here.\n'),
        ('""', "``''"),
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
        print(f"[{status}]  測試案例 {idx}")
        print(f"       輸入   : {repr(inp)}")
        print(f"       輸出   : {repr(result)}")
        if status == "FAIL":
            print(f"       預期   : {repr(expected)}")

    print("-" * 60)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


if __name__ == "__main__":
    run_tests()