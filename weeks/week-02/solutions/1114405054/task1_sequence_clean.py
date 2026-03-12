def clean_sequence(input_str):
    if not input_str.strip():
        return {"dedupe": [], "asc": [], "desc": [], "evens": []}
    nums = [int(x) for x in input_str.split()]
    return {
        "dedupe": list(dict.fromkeys(nums)),
        "asc": sorted(nums),
        "desc": sorted(nums, reverse=True),
        "evens": [x for x in nums if x % 2 == 0]
    }