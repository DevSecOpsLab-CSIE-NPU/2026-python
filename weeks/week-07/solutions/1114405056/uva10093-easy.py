import sys


def popcount(x: int) -> int:
    return x.bit_count()


def valid_row_masks(m: int):
    masks = []
    for mask in range(1 << m):
        # 同一列內，橫向相距 1 或 2 都會互打，故不可同時放炮兵。
        if (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0:
            masks.append(mask)
    return masks


def solve(data: str) -> str:
    # 讀入地圖，H 為不可放置。
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]

    blocked = []
    for row in grid:
        b = 0
        for j, ch in enumerate(row):
            if ch == "H":
                b |= 1 << j
        blocked.append(b)

    states = valid_row_masks(m)
    size = len(states)

    # 每一列只保留「不踩到山地」的合法狀態。
    allowed = []
    for i in range(n):
        row_states = []
        for s in states:
            if (s & blocked[i]) == 0:
                row_states.append(s)
        allowed.append(row_states)

    # 由於縱向攻擊距離是 2，轉移時要同時檢查上一列與上上列。
    neg = -10**9
    prev = [[neg] * size for _ in range(size)]

    idx = {s: k for k, s in enumerate(states)}

    # 第 0 列初始化，視為前兩列都為空。
    zero_i = idx[0]
    for s0 in allowed[0]:
        i0 = idx[s0]
        prev[zero_i][i0] = popcount(s0)

    for r in range(1, n):
        curr = [[neg] * size for _ in range(size)]
        for s_prev2_i in range(size):
            for s_prev_i in range(size):
                base = prev[s_prev2_i][s_prev_i]
                if base < 0:
                    continue

                s_prev2 = states[s_prev2_i]
                s_prev = states[s_prev_i]

                for s_now in allowed[r]:
                    # 與前一列、前二列同欄都不允許。
                    if (s_now & s_prev) != 0:
                        continue
                    if (s_now & s_prev2) != 0:
                        continue

                    i_now = idx[s_now]
                    val = base + popcount(s_now)
                    if val > curr[s_prev_i][i_now]:
                        curr[s_prev_i][i_now] = val

        prev = curr

    ans = 0
    for row in prev:
        best = max(row)
        if best > ans:
            ans = best

    return str(ans)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
