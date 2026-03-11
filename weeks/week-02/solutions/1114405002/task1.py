def sequence_clean(seq):
    # Dedupe: keep first occurrence order
    seen = set()
    dedupe = []
    for num in seq:
        if num not in seen:
            seen.add(num)
            dedupe.append(num)

    # Ascending sort
    asc = sorted(seq)

    # Descending sort
    desc = sorted(seq, reverse=True)

    # Evens: keep original order
    evens = [num for num in seq if num % 2 == 0]

    return {
        'dedupe': dedupe,
        'asc': asc,
        'desc': desc,
        'evens': evens
    }