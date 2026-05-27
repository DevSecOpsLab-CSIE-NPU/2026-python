def count_square_numbers(a, b):
    count = 0
    i = 1
    while True:
        square = i * i
        if square > b:
            break
        if square >= a:
            count += 1
        i += 1
    return count


def solve() -> None:
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(count_square_numbers(a, b))


if __name__ == "__main__":
    solve()
