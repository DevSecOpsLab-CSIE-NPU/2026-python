"""UVA 272 - 好記版本（-easy）。

這版用最直覺作法：
- 用一個布林值記錄「目前要放左引號還是右引號」
- 掃過每個字元，遇到 `"` 就替換
"""


def main() -> None:
    import sys

    text = sys.stdin.read()
    out = []
    left_quote = True

    for c in text:
        if c == '"':
            if left_quote:
                out.append("``")
            else:
                out.append("''")
            left_quote = not left_quote
        else:
            out.append(c)

    print("".join(out), end="")


if __name__ == "__main__":
    main()
