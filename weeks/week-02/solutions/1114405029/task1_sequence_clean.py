"""
Task 1: Sequence Clean
處理整數序列：去重保序、升序、降序及篩選偶數。
"""

def dedupe_sequence(nums: list) -> list:
    """
    去重並保留第一次出現的順序。
    不可直接使用 set()，因為會破壞順序。
    """
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

def get_evens(nums: list) -> list:
    """
    篩選出序列中的偶數，並維持原始順序。
    """
    return [x for x in nums if x % 2 == 0]

def process_sequences(input_str: str):
    """
    解析輸入字串並執行各項序列操作，最後輸出結果。
    """
    if not input_str.strip():
        return
    
    # 解析輸入
    try:
        nums = [int(x) for x in input_str.split()]
    except ValueError:
        return

    # 1. 去重保序
    deduped = dedupe_sequence(nums)
    
    # 2. 由小到大排序 (ASC)
    asc_sorted = sorted(nums)
    
    # 3. 由大到小排序 (DESC)
    desc_sorted = sorted(nums, reverse=True)
    
    # 4. 偶數序列 (Evens)
    evens = get_evens(nums)

    # 格式化輸出
    print(f"dedupe: {' '.join(map(str, deduped))}")
    print(f"asc: {' '.join(map(str, asc_sorted))}")
    print(f"desc: {' '.join(map(str, desc_sorted))}")
    print(f"evens: {' '.join(map(str, evens))}")

if __name__ == "__main__":
    import sys
    # 讀取標準輸入的一行資料
    input_data = sys.stdin.read()
    process_sequences(input_data)