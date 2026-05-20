from typing import List

def can_jump_distance(d: int, s: int, t: int) -> bool:
    if d < 0:
        return False
    if s == t:
        return d % s == 0

    max_check = 1000
    reach = [False] * (max_check + 1)
    reach[0] = True
    for i in range(1, max_check + 1):
        for step in range(s, t + 1):
            if i - step >= 0 and reach[i - step]:
                reach[i] = True
                break

    if d <= max_check:
        return reach[d]

    window = 100
    for start in range(max_check - window + 1):
        if all(reach[start + i] for i in range(window)):
            return d >= start
    return False

def min_stones_to_cross(length: int, s: int, t: int, stones: List[int]) -> int:
    points = [0] + sorted(stones) + [length]
    n = len(points)
    distances = [float('inf')] * n
    distances[0] = 0

    for i in range(n):
        for j in range(i + 1, n):
            gap = points[j] - points[i]
            if can_jump_distance(gap, s, t):
                extra = 0 if j == n - 1 else 1
                distances[j] = min(distances[j], distances[i] + extra)

    return int(distances[-1])   

def solve(lines: List[str]) -> List[str]:
    numbers: List[int] = []
    for line in lines:  
        for token in line.split():
            numbers.append(int(token))
    output: List[str] = []
    idx = 0
    while idx < len(numbers):
        length = numbers[idx]
        idx += 1
        s = numbers[idx]
        t = numbers[idx + 1]
        m = numbers[idx + 2]
        idx += 3
        stones = numbers[idx:idx + m]
        idx += m
        result = min_stones_to_cross(length, s, t, stones)
        output.append(str(result))
    return output

def main() -> None:
    import sys
    lines = sys.stdin.read().strip().split('\n')
    answers = solve(lines)
    print('\n'.join(answers))

if __name__ == "__main__":
    main()