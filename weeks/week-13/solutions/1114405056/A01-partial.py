"""A01: functools.partial practical usage."""

from functools import partial


def power(base, exp):
    return base**exp


students = [
    {"name": "Alice", "math": 80, "english": 70},
    {"name": "Bob", "math": 65, "english": 90},
    {"name": "Carol", "math": 95, "english": 55},
]


def get_score(student, subject):
    return student[subject]


def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total


if __name__ == "__main__":
    print("=== partial basics ===")
    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    print(square(5))
    print(cube(3))
    print([square(n) for n in range(1, 6)])

    print("\n=== partial + sorted key ===")
    by_math = partial(get_score, subject="math")
    by_english = partial(get_score, subject="english")
    print("math:", [s["name"] for s in sorted(students, key=by_math, reverse=True)])
    print("english:", [s["name"] for s in sorted(students, key=by_english, reverse=True)])

    print("\n=== base cost example ===")
    uniform_costs = [1] * 36
    calc = partial(cost_in_base, costs=uniform_costs)
    n = 255
    best_cost = min(calc(n, b) for b in range(2, 37))
    best_bases = [b for b in range(2, 37) if calc(n, b) == best_cost]
    print(f"n={n}, best_cost={best_cost}, best_bases={best_bases}")

    print("\n=== partial(print, end=' ') ===")
    print_same_line = partial(print, end=" ")
    for i in range(1, 6):
        print_same_line(i)
    print()
