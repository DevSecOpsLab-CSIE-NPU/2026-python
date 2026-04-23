# task1.py
# Task 1: Sequence Clean

def process_sequence(input_str: str):
    nums = list(map(int, input_str.split()))
    
    # 1. 去重後（保留第一次出現順序）
    dedupe = []
    seen = set()
    for n in nums:
        if n not in seen:
            dedupe.append(n)
            seen.add(n)

    # 2. 由小到大排序
    asc = sorted(nums)
    
    # 3. 由大到小排序
    desc = sorted(nums, reverse=True)
    
    # 4. 偶數序列（維持原始順序）
    evens = [n for n in nums if n % 2 == 0]
    
    return dedupe, asc, desc, evens

if __name__ == "__main__":
    import sys
    line = sys.stdin.read().strip()
    if line:
        d, a, ds, e = process_sequence(line)
        print(f"dedupe: {' '.join(map(str, d))}")
        print(f"asc: {' '.join(map(str, a))}")
        print(f"desc: {' '.join(map(str, ds))}")
        print(f"evens: {' '.join(map(str, e))}")
