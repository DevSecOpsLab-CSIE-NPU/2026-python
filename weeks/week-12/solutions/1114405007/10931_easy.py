# UVA 10931 - Parity
# 簡單版本（含中文註解）

import sys


def main() -> None:
    out = []

    for raw in sys.stdin:
        s = raw.strip()
        if not s:
            continue

        num = int(s)
        if num == 0:
            break

        b = bin(num)[2:]  # 轉成不含前導 0 的二進位字串
        ones = b.count("1")  # 統計 1 的數量
        out.append(f"The parity of {b} is {ones} (mod 2).")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
