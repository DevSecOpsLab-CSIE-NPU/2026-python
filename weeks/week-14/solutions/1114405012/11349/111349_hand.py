import sys

def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    total_cases = int(lines[0])
    index = 1
    outputs = []

    for case_number in range(1, total_cases + 1):
        size = int(lines[index].split("=")[1])
        index += 1

        matrix = []
        for _ in range(size):
            matrix.append(list(map(int, lines[index].split())))
            index += 1

        symmetric = True

        for row in range(size):
            for col in range(size):
                if matrix[row][col] < 0:
                    symmetric = False
                    break

                if matrix[row][col] != matrix[size - 1 - row][size - 1 - col]:
                    symmetric = False
                    break

            if not symmetric:
                break

        outputs.append(f"Test #{case_number}: {'Symmetric.' if symmetric else 'Non-symmetric.'}")

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main() 