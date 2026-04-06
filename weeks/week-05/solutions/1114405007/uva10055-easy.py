from sys import stdin


# 每一行只有兩個整數，直接輸出它們的差的絕對值。
def main():
    answer = []

    for line in stdin:
        line = line.strip()
        if not line:
            continue

        a, b = map(int, line.split())
        answer.append(str(abs(a - b)))

    print("\n".join(answer))


if __name__ == "__main__":
    main()