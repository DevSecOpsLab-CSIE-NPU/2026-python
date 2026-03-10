def process_sequence(nums):
    """
    Process a sequence of integers and return deduplicated, sorted, and even numbers.

    Args:
        nums (list): List of integers

    Returns:
        dict: Dictionary with keys 'dedupe', 'asc', 'desc', 'evens'
    """
    # Deduplicate while preserving order (without using set)
    seen = []
    dedupe = []
    for num in nums:
        if num not in seen:
            seen.append(num)
            dedupe.append(num)

    # Ascending sort
    asc = sorted(nums)

    # Descending sort
    desc = sorted(nums, reverse=True)

    # Even numbers in original order
    evens = [num for num in nums if num % 2 == 0]

    return {
        'dedupe': dedupe,
        'asc': asc,
        'desc': desc,
        'evens': evens
    }