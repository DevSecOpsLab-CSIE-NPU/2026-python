def deduplicate(numbers):
    """
    Remove duplicates from a list while preserving the first occurrence order.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of unique integers in order of first appearance
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


def get_evens(numbers):
    """
    Filter even numbers from list, preserving original order.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of even numbers in original order
    """
    return [num for num in numbers if num % 2 == 0]


def process_sequence(input_str):
    """
    Process a sequence of integers and return results in multiple formats.
    
    Args:
        input_str: Space-separated string of integers (e.g., "5 3 5 2 9")
        
    Returns:
        Dictionary with keys:
        - 'dedupe': Deduplicated sequence preserving first occurrence order
        - 'asc': Sorted in ascending order
        - 'desc': Sorted in descending order
        - 'evens': Even numbers preserving original order
    """
    # Parse input string to list of integers
    numbers = list(map(int, input_str.split()))
    
    return {
        'dedupe': deduplicate(numbers),
        'asc': sorted(numbers),
        'desc': sorted(numbers, reverse=True),
        'evens': get_evens(numbers)
    }
