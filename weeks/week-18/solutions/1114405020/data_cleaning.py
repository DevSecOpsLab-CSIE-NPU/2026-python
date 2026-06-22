def clean_data(nums: list[int], d: int) -> list[int]:
    """資料清理：
    1. 去除重複（保留第一次出現的順序）
    2. 只保留能被 d 整除的數
    3. 由小到大排序
    若 d < 1，拋出 ValueError。
    """
    if d < 1:
        raise ValueError("d must be an integer >= 1")

    # 步驟 1: 去重保序
    seen = set()
    deduped = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            deduped.append(num)

    # 步驟 2: 只保留能被 d 整除的數
    filtered = [num for num in deduped if num % d == 0]

    # 步驟 3: 由小到大排序
    return sorted(filtered)
