import sys


def parse_cases(text):
    lines = [line.strip() for line in text.splitlines()]
    idx = 0
    cases = []

    while idx < len(lines):
        if lines[idx] == "":
            idx += 1
            continue

        n = int(lines[idx])
        idx += 1
        dislike = []

        for _ in range(n):
            nums = [int(x) for x in lines[idx].split()]
            idx += 1

            banned = set()
            for x in nums:
                if x == 0:
                    break
                banned.add(x)
            dislike.append(banned)

        cases.append((n, dislike))

    return cases


def compress_output(full_lines):
    if not full_lines:
        return []

    out = [full_lines[0]]
    prev = full_lines[0]

    for cur in full_lines[1:]:
        i = 0
        while i < len(cur) and cur[i] == prev[i]:
            i += 1
        out.append(cur[i:])
        prev = cur

    return out


def solve_case(n, dislike):
    people = [chr(ord("A") + i) for i in range(n)]
    used = [False] * n
    current = []
    valid_lines = []

    def dfs(pos):
        if pos == n:
            valid_lines.append("".join(current))
            return

        pos_1_based = pos + 1

        # 依人名順序嘗試，確保輸出是字典序
        for person_idx in range(n):
            if used[person_idx]:
                continue
            if pos_1_based in dislike[person_idx]:
                continue

            used[person_idx] = True
            current.append(people[person_idx])
            dfs(pos + 1)
            current.pop()
            used[person_idx] = False

    dfs(0)
    return "\n".join(compress_output(valid_lines))


def solve(text):
    cases = parse_cases(text)
    blocks = [solve_case(n, dislike) for n, dislike in cases]
    return "\n\n".join(blocks) + "\n"


def main():
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
