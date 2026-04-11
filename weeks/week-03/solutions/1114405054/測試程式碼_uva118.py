"""
測試程式碼 - UVA 118 Martian Robots (ZeroJudge c082)
"""

DIRECTIONS = ['N', 'E', 'S', 'W']
DX = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
DY = {'N': 1, 'E': 0, 'S': -1, 'W': 0}


def simulate(max_x, max_y, robots):
    scents = set()
    results = []

    for (x, y, facing, commands) in robots:
        lost = False
        for cmd in commands:
            if cmd == 'L':
                facing = DIRECTIONS[(DIRECTIONS.index(facing) - 1) % 4]
            elif cmd == 'R':
                facing = DIRECTIONS[(DIRECTIONS.index(facing) + 1) % 4]
            elif cmd == 'F':
                new_x = x + DX[facing]
                new_y = y + DY[facing]
                if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                    if (x, y) not in scents:
                        scents.add((x, y))
                        lost = True
                        break
                else:
                    x, y = new_x, new_y
        if lost:
            results.append(f"{x} {y} {facing} LOST")
        else:
            results.append(f"{x} {y} {facing}")

    return results


def run_tests():
    test_cases = [
        (5, 3, [(1, 1, 'E', 'RFRFRFRF'), (3, 2, 'N', 'FRRFLLFFRRFLL'), (0, 3, 'W', 'LLFFFLFLFL')], ["1 1 E", "3 3 N LOST", "2 3 S"]),
        (5, 5, [(2, 2, 'N', 'LLLL')], ["2 2 N"]),
        (2, 2, [(2, 2, 'N', 'F'), (2, 2, 'N', 'F')], ["2 2 N LOST", "2 2 N"]),
        (3, 3, [(0, 0, 'S', 'F')], ["0 0 S LOST"]),
    ]

    passed = 0
    failed = 0
    print("=" * 55)
    print("UVA 118 測試結果")
    print("=" * 55)

    for idx, (max_x, max_y, robots, expected_list) in enumerate(test_cases, 1):
        results = simulate(max_x, max_y, robots)
        case_pass = results == expected_list
        if case_pass:
            passed += 1
            print(f"[PASS]  測試案例 {idx}")
        else:
            failed += 1
            print(f"[FAIL]  測試案例 {idx}")
            for r, e in zip(results, expected_list):
                flag = "✓" if r == e else "✗"
                print(f"        {flag} 輸出: '{r}'  預期: '{e}'")

    print("-" * 55)
    print(f"共 {passed + failed} 組，通過 {passed} 組，失敗 {failed} 組")


if __name__ == "__main__":
    run_tests()