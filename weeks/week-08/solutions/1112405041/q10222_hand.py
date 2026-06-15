import sys

# 【August 的惡意：身分置換 & 最新公告對齊】
# 根據 CHECK_LIST.md 最新公告：此題已從「優質學生」修正回「Decode the Mad man」。
# 鍵盤佈局向左偏移 2 位 (標準 UVA 10222 規則)。

def solve():
    # 定義鍵盤佈局
    kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

    # 建立查找映射 (向左移 2 位)
    mapping = {}
    for i in range(len(kb)):
        if i >= 2:
            mapping[kb[i]] = kb[i-2]

    # 讀取輸入並轉為小寫
    try:
        raw = sys.stdin.read().lower()
    except EOFError:
        return

    result = []
    for char in raw:
        if char in mapping:
            result.append(mapping[char])
        else:
            result.append(char)

    print("".join(result), end="")

if __name__ == "__main__":
    solve()
