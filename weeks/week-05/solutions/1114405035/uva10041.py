from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    outputs: List[str] = []
    idx = 0
    t = int(lines[idx])
    idx += 1
    for _ in range(t):
        parts = [int(x) for x in lines[idx].split()]
        r = parts[0]
        positions = sorted(parts[1:])
        median = positions[len(positions) // 2]
        distance_sum = sum(abs(pos - median) for pos in positions)
        outputs.append(str(distance_sum))
        idx += 1

    return '\n'.join(outputs)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List


def process_input(input_text: str) -> str:
    """解析輸入並回傳每組測資的最小距離總和。"""
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    results: List[str] = []
    t = int(lines[0])
    for index in range(1, t + 1):
        parts = [int(x) for x in lines[index].split()]
        positions = sorted(parts[1:])
        median = positions[len(positions) // 2]
        distance_sum = sum(abs(pos - median) for pos in positions)
        results.append(str(distance_sum))

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    text = sys.stdin.read()
    print(process_input(text), end='')
