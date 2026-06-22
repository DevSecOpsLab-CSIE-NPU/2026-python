def clean_data(nums, D):
    raise NotImplementedError


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        data = list(map(int, sys.stdin.readline().split()))
        result = clean_data(data, D=3)
        if not result:
            print("NONE")
        else:
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
