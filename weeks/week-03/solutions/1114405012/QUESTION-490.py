import sys

# 題目敘述中的簡單示例。
SAMPLE_INPUT = "HELLO\nWORLD\n"

# 將 HELLO / WORLD 順時針旋轉 90 度後的結果。
SAMPLE_OUTPUT = "WH\nOE\nRL\nLL\nDO"


def rotate_sentences(lines: list[str]) -> list[str]:
    # 沒有任何輸入列時，直接回傳空清單。
    if not lines:
        return []

    max_length = max(len(line) for line in lines)
    rotated = []

    for column in range(max_length):
        row_chars = []
        for line in reversed(lines):
            if column < len(line):
                row_chars.append(line[column])
            else:
                # 不足的部分以空白補齊，形成完整矩形。
                row_chars.append(" ")

        # 只去掉每列最右側多餘的填充空白，保留中間與左側空白。
        rotated.append("".join(row_chars).rstrip())

    return rotated


def solve(text: str) -> str:
    # splitlines() 會保留每一列內容，但移除換行字元本身。
    lines = text.splitlines()
    return "\n".join(rotate_sentences(lines))


def run_sample_test() -> None:
    # 使用題目說明中的 HELLO / WORLD 範例檢查結果。
    result = solve(SAMPLE_INPUT)
    print(result)
    assert result == SAMPLE_OUTPUT, "範例測試未通過"


if __name__ == "__main__":
    # 在終端直接執行時，沒有輸入就跑內建範例測試。
    if sys.stdin.isatty():
        run_sample_test()
    else:
        data = sys.stdin.read()
        if not data:
            sys.exit(0)
        print(solve(data))
