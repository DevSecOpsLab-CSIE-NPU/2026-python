import itertools
import sys


def parse_cases(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    i = 0
    cases = []

    while i < len(lines):
        n = int(lines[i])
        i += 1

        dislike = []
        for _ in range(n):
            nums = list(map(int, lines[i].split()))
            i += 1

            banned = set()
            for x in nums:
                if x == 0:
                    break
                banned.add(x)
            dislike.append(banned)

        cases.append((n, dislike))

    return cases


def valid(perm, dislike):
    # perm 是像 ('A','C','B') 的排列
    for person_idx in range(len(dislike)):
        person = chr(ord("A") + person_idx)
        pos = perm.index(person) + 1  # 位置改成 1-based
        if pos in dislike[person_idx]:
            return False
    return True


def compress(lines):
    if not lines:
        return []

    out = [lines[0]]
    prev = lines[0]

    for cur in lines[1:]:
        j = 0
        while j < len(cur) and cur[j] == prev[j]:
            j += 1
        out.append(cur[j:])
        prev = cur

    return out


def solve_case(n, dislike):
    people = [chr(ord("A") + i) for i in range(n)]

    full = []
    for p in itertools.permutations(people):
        if valid(p, dislike):
            full.append("".join(p))

    return "\n".join(compress(full))


def solve(text):
    cases = parse_cases(text)
    blocks = [solve_case(n, dislike) for n, dislike in cases]
    return "\n\n".join(blocks) + "\n"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
