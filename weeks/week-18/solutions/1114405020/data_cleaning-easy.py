def clean_data(nums: list[int], d: int) -> list[int]:
    """【AI 教學版】資料清理

    此版本包含詳細的繁體中文註解，解釋每一步的設計與時間複雜度權衡。
    """
    # 輸入驗證：若除數小於 1 則拋出 ValueError，保護程式免於零除或非法運算
    if d < 1:
        raise ValueError("除數 d 必須是大於或等於 1 的整數")

    # 步驟 1：去除重複（保留第一次出現的順序）
    # 使用 seen (set) 達到 O(1) 的超快尋找速度，同時用 list 保存順序，整體複雜度為 O(n)
    seen = set()
    deduped = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            deduped.append(num)

    # 步驟 2：篩選能被 d 整除的數
    # 使用 Python 的 List Comprehension 寫法，乾淨且高效，複雜度為 O(n)
    filtered = [num for num in deduped if num % d == 0]

    # 步驟 3：由小到大排序
    # Python 內建的 sorted 使用 Timsort 演算法，時間複雜度為 O(k log k)，其中 k ≦ n
    return sorted(filtered)
