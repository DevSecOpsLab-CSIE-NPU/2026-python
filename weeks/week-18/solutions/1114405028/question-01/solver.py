from typing import List


def filter_unique_divisible(nums: List[int], d: int) -> List[int]:
    if d == 0:
        raise ValueError("D must be non-zero")
    seen = set()
    result: List[int] = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            if x % d == 0:
                result.append(x)
    return result


if __name__ == "__main__":
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        print("NONE")
        sys.exit(0)
    *nums_str, d_str = data
    nums = [int(x) for x in nums_str]
    d = int(d_str)
    out = filter_unique_divisible(nums, d)
    if not out:
        print("NONE")
    else:
        print(" ".join(str(x) for x in out))
