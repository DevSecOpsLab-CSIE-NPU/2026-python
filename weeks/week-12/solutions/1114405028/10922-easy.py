# 10922 UVA 2 the 9s 簡易版
# 這個版本直接計算字串各位數字和，並遞迴求 9 的深度。

def solve() -> None:
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    out = []

    for s in lines:
        if s == "0":
            break
        digit_sum = sum(int(ch) for ch in s)
        if digit_sum % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
            continue

        depth = 1
        while digit_sum > 9:
            digit_sum = sum(int(ch) for ch in str(digit_sum))
            depth += 1

        if digit_sum == 9:
            out.append(f"9-degree of {s} is {depth}.")
        else:
            out.append(f"{s} is not a multiple of 9.")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()
