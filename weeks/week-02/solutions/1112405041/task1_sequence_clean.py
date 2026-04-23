def clean_sequence(data_str: str):
    """
    Task 1: Sequence Clean
    要求：去重(保序)、從小到大、從大到小、偶數序列(保序)
    老師的惡意提醒：不可直接用 set() 去重，因為會破壞原始順序。
    """
    try:
        # 將輸入字串轉為整數列表
        nums = [int(x) for x in data_str.split()]
    except ValueError:
        return "", "", "", ""

    if not nums:
        return "", "", "", ""

    # 1. Dedupe (保留第一次出現順序)
    # 使用 dict.fromkeys() 是 Python 3.7+ 保序去重的標準做法
    deduped = list(dict.fromkeys(nums))
    dedupe_str = " ".join(map(str, deduped))

    # 2. Ascending (從小到大)
    asc = sorted(nums)
    asc_str = " ".join(map(str, asc))

    # 3. Descending (從大到小)
    desc = sorted(nums, reverse=True)
    desc_str = " ".join(map(str, desc))

    # 4. Evens (偶數序列，維持原始順序)
    evens = [x for x in nums if x % 2 == 0]
    evens_str = " ".join(map(str, evens))

    return dedupe_str, asc_str, desc_str, evens_str

if __name__ == "__main__":
    # 測試範例
    input_data = "5 3 5 2 9 2 8 3 1"
    d, a, ds, e = clean_sequence(input_data)
    print(f"dedupe: {d}")
    print(f"asc: {a}")
    print(f"desc: {ds}")
    print(f"evens: {e}")
