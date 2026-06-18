from functools import partial
def get_score(student, subject): return student[subject]
def solve():
    students = [{"name": "A", "math": 80}, {"name": "B", "math": 95}]
    by_math = partial(get_score, subject="math")
    print(sorted(students, key=by_math, reverse=True))
if __name__ == '__main__': solve()
