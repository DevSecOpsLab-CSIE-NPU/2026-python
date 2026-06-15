# task1-easy.py
# Task 1: Sequence Clean (簡單版)

def solve():
    # 範例輸入
    input_str = "5 3 5 2 9 2 8 3 1"
    nums = list(map(int, input_str.split()))
    
    # 去重 (保持順序)
    dedupe = []
    for n in nums:
        if n not in dedupe:
            dedupe.append(n)

    # 排序
    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    
    # 偶數
    evens = [n for n in nums if n % 2 == 0]
    
    print(f"dedupe: {dedupe}")
    print(f"asc: {asc}")
    print(f"desc: {desc}")
    print(f"evens: {evens}")

if __name__ == "__main__":
    solve()
