from itertools import permutations
import sys

def solve():
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return

    idx = 0
    first = True
    while idx < len(lines):
        N = int(lines[idx])
        idx += 1

        forbidden = []
        for _ in range(N):
            f = []
            for x in map(int, lines[idx].split()):
                if x == 0:
                    break
                f.append(x)
            forbidden.append(set(f))
            idx += 1

        if not first:
            print()
        first = False

        persons = [chr(ord('A') + i) for i in range(N)]
        prev = ""

        for p in permutations(persons):
            ok = True
            for pos, person in enumerate(p):
                if (pos + 1) in forbidden[ord(person) - ord('A')]:
                    ok = False
                    break
            if not ok:
                continue

            cur = ''.join(p)
            if not prev:
                print(cur)
            else:
                for i in range(len(prev)):
                    if i >= len(cur) or prev[i] != cur[i]:
                        print(cur[i:])
                        break
            prev = cur

if __name__ == "__main__":
    solve()