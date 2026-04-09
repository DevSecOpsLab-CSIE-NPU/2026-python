from typing import List


def reconstruct_permutation(N: int, inversion: List[int]) -> List[int]:
    
    inv = [0] + inversion

    remaining = list(range(1, N + 1))  

    result = []

    for i in range(1, N + 1):
        k = inv[i - 1] + 1
        num = remaining.pop(k - 1)
        result.append(num)
    return result


def solve() -> None:

    import sys

    data = sys.stdin.read().strip().split()

    if not data:
        return

    N = int(data[0])
    inversion = [int(x) for x in data[1:]]
    result = reconstruct_permutation(N, inversion)
    for num in result:
        print(num)
