import sys


def main():
    nums = sys.stdin.read().split()

    # 每兩個數字一組
    for i in range(0, len(nums), 2):
        a = int(nums[i])
        b = int(nums[i + 1])
        print(abs(a - b))


if __name__ == "__main__":
    main()