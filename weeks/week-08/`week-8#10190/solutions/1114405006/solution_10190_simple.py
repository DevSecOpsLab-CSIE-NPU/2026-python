def build_sequence(n: int, m: int):
    # 題目要求 m 必須大於 1，否則無法持續相除
    if m <= 1:
        return None

    seq = [n]

    # 一直除到 1，途中只要不能整除就失敗
    while n != 1:
        if n % m != 0:
            return None
        n //= m
        seq.append(n)

    return seq


def solve() -> None:
    import sys

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        n, m = map(int, line.split())
        seq = build_sequence(n, m)

        # 需至少有兩個數字，且必須嚴格遞減才算合法鏈
        if seq is None or len(seq) < 2 or any(seq[i] <= seq[i + 1] for i in range(len(seq) - 1)):
            out.append("Boring!")
        else:
            out.append(" ".join(map(str, seq)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()