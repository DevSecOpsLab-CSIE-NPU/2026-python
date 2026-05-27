import sys


def check_symmetric(values):
    left = 0
    right = len(values) - 1

    while left <= right:
        if values[left] < 0 or values[right] < 0:
            return False

        if values[left] != values[right]:
            return False

        left += 1
        right -= 1

    return True


def solve(data):
    parts = data.split()

    if len(parts) == 0:
        return ""

    t = int(parts[0])
    pos = 1
    output = []

    for case_id in range(1, t + 1):
        n = int(parts[pos + 2])
        pos += 3

        values = []

        for _ in range(n * n):
            values.append(int(parts[pos]))
            pos += 1

        if check_symmetric(values):
            output.append(f"Test #{case_id}: Symmetric.")
        else:
            output.append(f"Test #{case_id}: Non-symmetric.")

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()