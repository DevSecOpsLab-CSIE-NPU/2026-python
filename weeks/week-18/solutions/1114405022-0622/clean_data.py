def clean_data(data: list, d: int) -> list | str:
    if d == 0:
        return "NONE"
    
    # 1. 去重且保序 (Preserve first occurrence)
    seen = set()
    deduped = []
    for x in data:
        if x not in seen:
            deduped.append(x)
            seen.add(x)
    
    # 2. 篩選 (Divisible by d)
    filtered = [x for x in deduped if x % d == 0]
    
    # 3. 排序 (Ascending)
    filtered.sort()
    
    # 回傳結果
    return filtered if filtered else "NONE"
