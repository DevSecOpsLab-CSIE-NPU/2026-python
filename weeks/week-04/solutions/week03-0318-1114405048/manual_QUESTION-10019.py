import sys


def main():
    # 讀到 EOF，每兩個數字是一組
    nums = sys.stdin.read().split()

    i = 0
    while i + 1 < len(nums):
        a = int(nums[i])
        b = int(nums[i + 1])
        print(abs(a - b))
        i += 2


if __name__ == "__main__":
    main()
