def rank_students(students, k):
    """
    Rank students by score (desc), age (asc), name (asc) and return top k.

    Args:
        students (list): List of dicts with 'name', 'score', 'age'
        k (int): Number of top students to return

    Returns:
        list: Top k students in ranked order
    """
    # Sort students with the specified criteria
    sorted_students = sorted(students, key=lambda s: (-s['score'], s['age'], s['name']))

    # Return top k
    return sorted_students[:k]