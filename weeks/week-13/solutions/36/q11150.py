from typing import List


def can_jump_distance(d: int, s: int, t: int) -> bool:
    """判斷距離 d 是否可以由 s..t 的跳躍長度組成。"""
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
    """計算青蛙過河最少需要踩到的石子數。"""
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
    """解析整個輸入，回傳每個測資的最小踩石子數。"""
    data = [int(token) for line in lines for token in line.split()]
    output: List[str] = []
    index = 0
    while index < len(data):
        length = data[index]
        index += 1
        if index >= len(data):
            break
        s = data[index]
        t = data[index + 1]
        m = data[index + 2]
        index += 3
        stones = data[index:index + m]
        index += m
        answer = min_stones_to_cross(length, s, t, stones)
        output.append(str(answer))
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()
