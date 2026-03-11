def student_ranking(students, k):
    sorted_students = sorted(students, key=lambda s: (-s['score'], s['age'], s['name']))
    return sorted_students[:k]