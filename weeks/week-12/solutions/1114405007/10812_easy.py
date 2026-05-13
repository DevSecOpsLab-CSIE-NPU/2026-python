# UVA 10812 - Beat the Spread!
# 簡單版本（含中文註解）

import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        s = int(data[idx])
        d = int(data[idx + 1])
        idx += 2

        # 若總和小於差，或 (s + d) 不是偶數，就不可能有整數解
        if s < d or (s + d) % 2 != 0:
            out.append("impossible")
            continue

        high = (s + d) // 2
        low = (s - d) // 2

        # 分數不能是負數
        if low < 0:
            out.append("impossible")
        else:
            out.append(f"{high} {low}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
