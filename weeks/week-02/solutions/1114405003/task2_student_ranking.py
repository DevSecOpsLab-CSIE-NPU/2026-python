def _ranking_key(student):
    """
    Generate sorting key for student ranking.
    
    Sorting order:
    1. Score: descending (higher scores first)
    2. Age: ascending (younger students first on same score)
    3. Name: ascending (alphabetically on same score and age)
    
    Args:
        student: Tuple (name, score, age)
        
    Returns:
        Tuple of sort keys: (-score, age, name)
    """
    name, score, age = student
    return (-score, age, name)


def rank_students(students, k):
    """
    Rank students with multi-key sorting criteria.
    
    Sorting priority:
    1. Score: descending (higher is better)
    2. Age: ascending (younger is better in tie)
    3. Name: alphabetically ascending (lexicographic in full tie)
    
    Args:
        students: List of tuples (name, score, age)
        k: Number of top students to return
        
    Returns:
        List of top k students sorted according to criteria,
        as list of tuples [(name, score, age), ...]
    """
    sorted_students = sorted(students, key=_ranking_key)
    return sorted_students[:k]
