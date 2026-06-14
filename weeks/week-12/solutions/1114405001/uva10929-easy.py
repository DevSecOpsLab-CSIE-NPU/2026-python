"""UVA 10929 (easy version)"""


def solve(data: str) -> str:
    ans = []
    for line in data.splitlines():
        num = line.strip()
        if not num:
            continue
        if num == "0":
            break

        odd_sum = 0
        even_sum = 0

        for i, ch in enumerate(num):
            if i % 2 == 0:
                odd_sum += int(ch)
            else:
                even_sum += int(ch)

        if (odd_sum - even_sum) % 11 == 0:
            ans.append(f"{num} is a multiple of 11.")
        else:
            ans.append(f"{num} is not a multiple of 11.")

    return "\n".join(ans)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
