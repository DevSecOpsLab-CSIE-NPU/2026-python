import sys


def solve(data: str) -> str:
    """把一般雙引號 \" 交替替換成 `` 與 ''。"""
    # False 代表下一個引號要變成開引號 ``。
    # True 代表下一個引號要變成閉引號 ''。
    close_next = False

    out = []
    for ch in data:
        if ch == '"':
            if not close_next:
                out.append("``")
            else:
                out.append("''")
            close_next = not close_next
        else:
            # 不是雙引號就原樣保留（含空白、換行、標點）。
            out.append(ch)

    return "".join(out)


def main() -> None:
    text = sys.stdin.read()
    print(solve(text), end="")


if __name__ == "__main__":
    main()
