def solve(data: str) -> str:
    lines = data.strip().splitlines()
    t = int(lines[0])
    answers = []

    for i in range(1, t + 1):
        s = lines[i].strip()
        decimal_value = int(s)
        hex_value = int(s, 16)

        b1 = bin(decimal_value).count("1")
        b2 = bin(hex_value).count("1")

        answers.append(f"{b1} {b2}")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))