"""R01: flexible function signatures.

Topics:
- *args
- **kwargs
- keyword-only parameters
"""


def add_all(*args):
    """Collect positional args as a tuple and sum them."""
    return sum(args)


def make_student(**kwargs):
    """Collect named args as a dict."""
    return kwargs


def send_score(student_id, *, subject, score):
    """subject and score must be passed by name."""
    print(f"student={student_id} | {subject}={score}")


def report(title, *scores, prefix="score"):
    avg = sum(scores) / len(scores) if scores else 0.0
    print(f"{prefix} report - {title}: avg={avg:.1f}")


if __name__ == "__main__":
    print("=== *args ===")
    print(add_all(1, 2))
    print(add_all(1, 2, 3, 4, 5))
    print(add_all())

    print("\n=== **kwargs ===")
    s = make_student(name="Alice", grade=85, seat=12)
    print(s)

    print("\n=== keyword-only ===")
    send_score("411234001", subject="math", score=90)

    print("\n=== mixed signature ===")
    report("midterm", 80, 90, 70)
    report("final", 95, 85, 75, 100, prefix="final")
