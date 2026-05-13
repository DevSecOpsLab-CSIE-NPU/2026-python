# UVA 10929 - You can say 11
# 簡單版本（含中文註解）

import sys


def main() -> None:
    out = []

    for raw in sys.stdin:
        num = raw.strip()
        if not num:
            continue
        if num == "0":
            break

        rem = 0
        # 用字串逐位計算模 11，避免大數溢位
        for ch in num:
            rem = (rem * 10 + (ord(ch) - ord("0"))) % 11

        if rem == 0:
            out.append(f"{num} is a multiple of 11.")
        else:
            out.append(f"{num} is not a multiple of 11.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
