def clean_sequence(input_str):
    if not input_str or not input_str.strip():
        return {"dedupe": [], "asc": [], "desc": [], "evens": []}
    
    nums = [int(x) for x in input_str.split()]
    
   
    dedupe = []
    seen = set()
    for n in nums:
        if n not in seen:
            dedupe.append(n)
            seen.add(n)
            
    return {
        "dedupe": dedupe,
        "asc": sorted(nums),
        "desc": sorted(nums, reverse=True),
        "evens": [x for x in nums if x % 2 == 0]
    }

if __name__ == "__main__":
    try:
        raw_input = input()
        res = clean_sequence(raw_input)
        print(f"dedupe: {' '.join(map(str, res['dedupe']))}")
        print(f"asc: {' '.join(map(str, res['asc']))}")
        print(f"desc: {' '.join(map(str, res['desc']))}")
        print(f"evens: {' '.join(map(str, res['evens']))}")
    except EOFError:
        pass