import sys


def generate_permutations(n, forbidden):
    used = [False] * n
    cur = [0] * n
    results = []

    def dfs(pos):
        if pos == n:
            results.append("".join(chr(ord("A") + x) for x in cur))
            return

        for person in range(n):
            if used[person]:
                continue
            if pos in forbidden[person]:
                continue
            used[person] = True
            cur[pos] = person
            dfs(pos + 1)
            used[person] = False

    dfs(0)
    return results


def compressed_print(arrangements):
    out = []
    prev = None
    for s in arrangements:
        if prev is None:
            out.append(s)
        else:
            i = 0
            while i < len(s) and s[i] == prev[i]:
                i += 1
            out.append(s[i:])
        prev = s
    return out


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    idx = 0
    case_outputs = []

    while idx < len(data):
        n = int(data[idx])
        idx += 1

        forbidden = [set() for _ in range(n)]
        for i in range(n):
            while True:
                v = int(data[idx])
                idx += 1
                if v == 0:
                    break
                forbidden[i].add(v - 1)

        arrangements = generate_permutations(n, forbidden)
        case_outputs.append("\n".join(compressed_print(arrangements)))

    sys.stdout.write("\n\n".join(case_outputs))


if __name__ == "__main__":
    solve()
