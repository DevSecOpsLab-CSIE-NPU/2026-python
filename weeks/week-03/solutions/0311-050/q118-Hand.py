def solve_robots(world_size, robots_data):
    max_x, max_y = world_size
    scents = set()
    results = []

    turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    for robot in robots_data:
        x, y, face, instructions = robot
        is_lost = False

        for cmd in instructions:
            if is_lost:
                break

            if cmd == 'L':
                face = turn_left[face]
            elif cmd == 'R':
                face = turn_right[face]
            elif cmd == 'F':
                dx, dy = moves[face]
                next_x = x + dx
                next_y = y + dy

                if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                    if (x, y, face) in scents:
                        continue
                    else:
                        scents.add((x, y, face))
                        is_lost = True
                else:
                    x, y = next_x, next_y

        if is_lost:
            results.append(f"{x} {y} {face} LOST")
        else:
            results.append(f"{x} {y} {face}")

    return results