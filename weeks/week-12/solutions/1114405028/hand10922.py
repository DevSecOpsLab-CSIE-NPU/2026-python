def solve() -> None:
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    out = []

    for s in lines:
        if s == "0":
            break

        total = sum(int(ch) for ch in s)
        if total % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
            continue

        degree = 1
        while total > 9:
            total = sum(int(ch) for ch in str(total))
            degree += 1

        if total == 9:
            out.append(f"9-degree of {s} is {degree}.")
        else:
            out.append(f"{s} is not a multiple of 9.")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()
