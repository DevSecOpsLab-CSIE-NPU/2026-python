def process(nums: list[int], D: int = 4) -> list[int]:
    seen = set()
    deduped = []
    for x in nums:
        if x not in seen:
            deduped.append(x)
            seen.add(x)
    filtered = [x for x in deduped if x % D == 0]
    filtered.sort()
    return filtered
