"""
Task 1: Sequence Clean
給定一行整數，輸出去重、排序、偶數序列
"""


def process_sequence(nums_str):
    """
    處理整數序列，輸出四種結果

    參數：
        nums_str: 以空白分隔的整數字串
    回傳：
        包含四種結果的字典
    """
    nums = list(map(int, nums_str.split()))

    seen = []
    seen_set = set()
    for n in nums:
        if n not in seen_set:
            seen.append(n)
            seen_set.add(n)

    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    evens = [n for n in nums if n % 2 == 0]

    return {"dedupe": seen, "asc": asc, "desc": desc, "evens": evens}


def main():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    if not lines:
        return

    for line in lines:
        result = process_sequence(line)
        print(f"dedupe: {' '.join(map(str, result['dedupe']))}")
        print(f"asc: {' '.join(map(str, result['asc']))}")
        print(f"desc: {' '.join(map(str, result['desc']))}")
        print(f"evens: {' '.join(map(str, result['evens']))}")


if __name__ == "__main__":
    main()
