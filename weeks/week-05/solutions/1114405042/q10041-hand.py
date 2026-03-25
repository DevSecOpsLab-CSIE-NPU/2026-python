def solve_vito_easy(date: list[int]) -> int:
    if len(date) <= 1:
        return 0
    houses = date[1:]
    houses.sort()
    median = houses[len(houses) // 2]
    return sum(abs(h - median)for h in houses)