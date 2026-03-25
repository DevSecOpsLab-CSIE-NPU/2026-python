import sys

def find_median_and_sum(nums):
    if not nums:
        return 0, 0, 0
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = nums[n // 2 - 1]
    min_sum = sum(abs(x - median) for x in nums)
    possible = 1 if n % 2 == 1 else 2
    return median, min_sum, possible

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        nums = list(map(int, sys.stdin.readline().split()))
        A, min_sum, possible = find_median_and_sum(nums)
        print(A, min_sum, possible)

if __name__ == "__main__":
    main()