# UVA 10252 - Common Permutation
# 詳細註解版（繁體中文）

import sys
from collections import Counter


def solve() -> None:
    data = sys.stdin.read().splitlines()
    out = []

    # 每兩行是一組字串：找兩字串共同字元（含重複次數）並依字典序輸出
    i = 0
    while i + 1 < len(data):
        a = data[i]
        b = data[i + 1]
        i += 2

        ca = Counter(a)
        cb = Counter(b)

        # UVA 10252 的字元範圍通常為 a-z；這裡直接遍歷 ASCII 更穩健
        common_chars = []
        for ch in map(chr, range(256)):
            k = min(ca.get(ch, 0), cb.get(ch, 0))
            if k > 0:
                common_chars.append(ch * k)

        out.append("".join(common_chars))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
