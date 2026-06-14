"""UVA 10931 - Parity (easy version)"""


def solve(data: str) -> str:
    lines = [x.strip() for x in data.splitlines() if x.strip()]
    result = []

    for item in lines:
        num = int(item)
        if num == 0:
            break

        binary = format(num, "b")

        ones = 0
        for ch in binary:
            if ch == "1":
                ones += 1

        result.append(f"The parity of {binary} is {ones} (mod 2).")

    return "\n".join(result)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
