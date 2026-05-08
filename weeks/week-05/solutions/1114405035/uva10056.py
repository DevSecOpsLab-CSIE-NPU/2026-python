def process_input(input_text: str) -> str:
    lines = [line for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    output = []
    t = int(lines[0])
    for row in lines[1:t + 1]:
        tokens = row.split()
        n = int(tokens[0])
        p = float(tokens[1])
        i = int(tokens[2])

        if p == 1.0:
            output.append('1.0000' if i == 1 else '0.0000')
            continue

        q = 1.0 - p
        result = (q ** (i - 1)) * p / (1.0 - q ** n)
        output.append(f'{result:.4f}')

    return '\n'.join(output)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    outputs: List[str] = []
    cases = int(lines[0])
    for i in range(1, cases + 1):
        n_str, p_str, idx_str = lines[i].split()
        n = int(n_str)
        p = float(p_str)
        player = int(idx_str)

        if p == 0.0:
            outputs.append('0.0000')
            continue

        if p == 1.0:
            outputs.append('1.0000' if player == 1 else '0.0000')
            continue

        base = (1.0 - p) ** (player - 1)
        cycle = (1.0 - p) ** n
        probability = base * p / (1.0 - cycle)
        outputs.append(f'{probability:.4f}')

    return '\n'.join(outputs)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
