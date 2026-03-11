import sys

# 題目敘述中的經典範例輸入。
SAMPLE_INPUT = '"To be or not to be," quoth the bard, "that is the question."\n'

# 題目範例輸入對應的預期輸出。
SAMPLE_OUTPUT = "``To be or not to be,'' quoth the bard, ``that is the question.''\n"


def transform_quotes(text: str) -> str:
    # opening=True 代表下一個遇到的雙引號要轉成左引號 ``。
    opening = True
    output = []

    for char in text:
        if char == '"':
            if opening:
                output.append("``")
            else:
                output.append("''")
            opening = not opening
        else:
            # 非雙引號字元全部原樣保留，包含換行。
            output.append(char)

    return "".join(output)


def solve(text: str) -> str:
    # 本題只需要將全文中的普通雙引號依序替換即可。
    return transform_quotes(text)


def run_sample_test() -> None:
    # 直接用題目敘述中的句子驗證結果。
    result = solve(SAMPLE_INPUT)
    print(result, end="")
    assert result == SAMPLE_OUTPUT, "範例測試未通過"


if __name__ == "__main__":
    # 若有標準輸入，就依題目規則轉換全部內容。
    if sys.stdin.isatty():
        run_sample_test()
    else:
        data = sys.stdin.read()
        if not data:
            sys.exit(0)
        print(solve(data), end="")
