# UVA 118 機器人指令模擬
# 依題目要求處理邊界與 scent 標記

def turn_left(direction):
    directions = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    return directions[direction]


def turn_right(direction):
    directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    return directions[direction]


def move_forward(x, y, direction):
    if direction == 'N':
        return x, y + 1
    if direction == 'S':
        return x, y - 1
    if direction == 'E':
        return x + 1, y
    return x - 1, y


def simulate_robot(x, y, direction, commands, max_x, max_y, scents):
    lost = False
    for command in commands:
        if command == 'L':
            direction = turn_left(direction)
        elif command == 'R':
            direction = turn_right(direction)
        elif command == 'F':
            next_x, next_y = move_forward(x, y, direction)
            if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
                x, y = next_x, next_y
            else:
                if (x, y, direction) in scents:
                    continue
                scents.add((x, y, direction))
                lost = True
                break
    return x, y, direction, lost


def solve_118(input_text):
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''
    max_x, max_y = map(int, lines[0].split())
    output = []
    scents = set()
    idx = 1
    while idx + 1 < len(lines):
        x, y, direction = lines[idx].split()
        x, y = int(x), int(y)
        commands = lines[idx + 1].strip()
        x, y, direction, lost = simulate_robot(x, y, direction, commands, max_x, max_y, scents)
        output.append(f"{x} {y} {direction}" + (" LOST" if lost else ""))
        idx += 2
    return "\n".join(output)


def main():
    import sys
    data = sys.stdin.read()
    if data.strip():
        print(solve_118(data))


if __name__ == '__main__':
    main()
