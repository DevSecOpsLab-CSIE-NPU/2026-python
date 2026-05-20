from typing import List


def can_jump_distance(d: int, s: int, t: int) -> bool:
    """用最簡單的方式判斷 d 是否能夠拆成 s..t 的跳躍距離之和。"""
    if d < 0:
        return False
    if s == t:
        return d % s == 0

    max_check = 1000
    reachable = [False] * (max_check + 1)
    reachable[0] = True
    for i in range(1, max_check + 1):
        for step in range(s, t + 1):
            if i - step >= 0 and reachable[i - step]:
                reachable[i] = True
                break

    if d <= max_check:
        return reachable[d]

    window = 100
    for start in range(max_check - window + 1):
        if all(reachable[start + k] for k in range(window)):
            return d >= start
    return False


def min_stones_to_cross(length: int, s: int, t: int, stones: List[int]) -> int:
    """依序檢查每一個石頭位置，計算最少踩到的石子數。"""
    positions = [0] + sorted(stones) + [length]
    best = [float('inf')] * len(positions)
    best[0] = 0

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            gap = positions[j] - positions[i]
            if can_jump_distance(gap, s, t):
                cost = 0 if j == len(positions) - 1 else 1
                candidate = best[i] + cost
                if candidate < best[j]:
                    best[j] = candidate

    return int(best[-1])


def solve(lines: List[str]) -> List[str]:
    """逐行讀取資料並回傳答案。"""
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
        answer = min_stones_to_cross(length, s, t, stones)
        output.append(str(answer))
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()
