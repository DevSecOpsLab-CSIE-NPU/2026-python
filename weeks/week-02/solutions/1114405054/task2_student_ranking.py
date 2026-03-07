def get_ranking(students, k):
    return sorted(students, key=lambda x: (-x[1], x[2], x[0]))[:k]
