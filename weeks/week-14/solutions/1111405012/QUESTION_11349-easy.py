import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    test_count = int(lines[0])
    line_index = 1
    result = []

    for case_number in range(1, test_count + 1):
        size = int(lines[line_index].split("=")[1])
        line_index += 1

        numbers = []
        for _ in range(size):
            numbers += [int(x) for x in lines[line_index].split()]
            line_index += 1

        symmetric = True
        for i in range(len(numbers)):
            # 題目要求中心對稱，而且每個數都不能是負數。
            if numbers[i] < 0 or numbers[i] != numbers[len(numbers) - 1 - i]:
                symmetric = False
                break

        if symmetric:
            result.append(f"Test #{case_number}: Symmetric.")
        else:
            result.append(f"Test #{case_number}: Non-symmetric.")

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
