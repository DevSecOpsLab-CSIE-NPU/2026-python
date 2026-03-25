from __future__ import annotations


def minimum_total_distance_easy(addresses: list[int]) -> int:
    if not addresses:
        return 0
    best = float("inf")
    for candidate in addresses:
        total = 0
        for addr in addresses:
            total += abs(addr - candidate)
        if total < best:
            best = total
    return int(best)


def solve_io(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""
    t = int(tokens[0])
    idx = 1
    outputs: list[str] = []
    for _ in range(t):
        r = int(tokens[idx])
        idx += 1
        addresses = [int(tokens[idx + i]) for i in range(r)]
        idx += r
        outputs.append(str(minimum_total_distance_easy(addresses)))
    return "\n".join(outputs)


def main() -> None:
    import sys

    input_data = sys.stdin.read()
    result = solve_io(input_data)
    if result:
        print(result)


if __name__ == "__main__":
    main()
