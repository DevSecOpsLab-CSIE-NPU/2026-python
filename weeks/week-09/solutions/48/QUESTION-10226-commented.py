import sys


# 產生所有符合限制的排列（字典序）
def generate_permutations(n, forbidden):
    used = [False] * n
    cur = [0] * n
    results = []

    def dfs(pos):
        # 已填完所有位置，收下答案
        if pos == n:
            results.append("".join(chr(ord("A") + x) for x in cur))
            return

        # 依 A, B, C... 嘗試，確保字典序
        for person in range(n):
            if used[person]:
                continue
            # 這個人不能站在 pos 位置
            if pos in forbidden[person]:
                continue
            used[person] = True
            cur[pos] = person
            dfs(pos + 1)
            used[person] = False

    dfs(0)
    return results


# 依題意壓縮輸出：與上一個答案相同前綴不印
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
        # 每個人一行，直到讀到 0
        for i in range(n):
            while True:
                v = int(data[idx])
                idx += 1
                if v == 0:
                    break
                # 題目位置通常是 1-based，轉成 0-based
                forbidden[i].add(v - 1)

        arrangements = generate_permutations(n, forbidden)
        case_outputs.append("\n".join(compressed_print(arrangements)))

    # 多組測資以空行分隔
    sys.stdout.write("\n\n".join(case_outputs))


if __name__ == "__main__":
    solve()
