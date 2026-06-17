"""R05: Counter, defaultdict, and namedtuple basics."""

from collections import Counter, defaultdict, namedtuple

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter:", cnt)
print("most common:", cnt.most_common(2))

extra = Counter(["banana", "cherry"])
print("merged:", cnt + extra)

records = [
    ("CS", "Alice"),
    ("EE", "Bob"),
    ("CS", "Carol"),
    ("EE", "David"),
    ("CS", "Eve"),
]

by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)

print("\ndefaultdict groups:")
for dept, members in by_dept.items():
    print(f" {dept}: {members}")

score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    score_sum[name] += score
print("\nscore sums:", dict(score_sum))

Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price} change {s.change}")

data = [
    {"dept": "CS", "score": 85},
    {"dept": "EE", "score": 78},
    {"dept": "CS", "score": 92},
    {"dept": "EE", "score": 88},
]

dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])

print("\ndepartment averages:")
for dept, values in dept_scores.items():
    avg = sum(values) / len(values)
    print(f" {dept}: {avg:.1f}")
