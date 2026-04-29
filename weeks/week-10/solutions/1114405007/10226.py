import sys

"""
優化說明：
- 先預計算每個位置可放的人，減少 DFS 中重複的限制判斷。
- 用 bitmask 記錄已使用的人，讓遞迴狀態更精簡、速度更快。
- 將輸入解析與核心求解分開，後續測試與維護更容易。
"""


def solve_case(size, forbidden_positions):
    letters = [chr(ord("A") + index) for index in range(size)]
    allowed_by_slot = [
        [person for person in range(size) if slot + 1 not in forbidden_positions[person]]
        for slot in range(size)
    ]

    path = [""] * size
    previous = ""
    output = []

    def dfs(slot, used_mask):
        nonlocal previous
        if slot == size:
            permutation = "".join(path)
            prefix = 0
            while prefix < size and prefix < len(previous) and previous[prefix] == permutation[prefix]:
                prefix += 1
            output.append(permutation[prefix:])
            previous = permutation
            return

        for person in allowed_by_slot[slot]:
            bit = 1 << person
            if used_mask & bit:
                continue
            path[slot] = letters[person]
            dfs(slot + 1, used_mask | bit)

    dfs(0, 0)
    return "\n".join(output)


def solve(reader):
    cases = []

    while True:
        line = reader.readline()
        if not line:
            break

        stripped = line.strip()
        if not stripped:
            continue

        size = int(stripped)
        forbidden_positions = []
        for _ in range(size):
            values = list(map(int, reader.readline().split()))
            forbidden_positions.append(set(values[:-1]))

        cases.append(solve_case(size, forbidden_positions))

    return "\n\n".join(cases)


def main():
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    main()