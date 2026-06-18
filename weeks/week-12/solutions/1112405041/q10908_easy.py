# AI Easy 版: 10908 Largest Square
import sys

def solve():
    """
    在 M*N 網格中，給定中心點 (r, c)，尋找以其為中心且字元皆相同的最大奇數邊長正方形。
    解法：中心擴張法。
    """
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    t_cases = int(input_data[ptr]); ptr += 1

    for _ in range(t_cases):
        m = int(input_data[ptr])
        n = int(input_data[ptr+1])
        q = int(input_data[ptr+2])
        ptr += 3

        grid = input_data[ptr : ptr + m]
        ptr += m

        print(f"{m} {n} {q}")
        for _ in range(q):
            r = int(input_data[ptr])
            c = int(input_data[ptr+1])
            ptr += 2

            char = grid[r][c]
            ans = 1
            # 嘗試擴張半徑
            while True:
                offset = (ans + 2) // 2
                r1, r2 = r - offset, r + offset
                c1, c2 = c - offset, c + offset

                # 邊界檢查
                if r1 < 0 or r2 >= m or c1 < 0 or c2 >= n: break

                # 檢查新增的邊緣字元是否相同
                is_ok = True
                for i in range(r1, r2 + 1):
                    if grid[i][c1] != char or grid[i][c2] != char:
                        is_ok = False; break
                if is_ok:
                    for j in range(c1, c2 + 1):
                        if grid[r1][j] != char or grid[r2][j] != char:
                            is_ok = False; break

                if is_ok: ans += 2
                else: break
            print(ans)

if __name__ == "__main__":
    solve()
