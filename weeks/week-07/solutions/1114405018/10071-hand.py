import sys

def answer_hand(s, d):

    left, right = s, 2_000_000_000
    while left < right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2 - s * (s - 1) // 2
        if total >= d:
            right = mid
        else:
            left = mid + 1

    return left

def solve(text):

    nums = [int(x) for x in text.split()]
    out = []
    for i in range(0, len(nums) - 1, 2):
        s, d = nums[i], nums[i + 1]
        out.append(str(answer_hand(s, d)))
    return "\n".join(out)

def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()