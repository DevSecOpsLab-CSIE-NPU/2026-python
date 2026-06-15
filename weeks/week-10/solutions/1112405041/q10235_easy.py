import sys

def solve():
    """
    UVA 10235 魔改版：網格哈密頓迴路計數 (插頭 DP)
    題目要求計算在 N*M 網格上，所有非障礙物格子都被蛇（迴路）恰好覆蓋的方法數。
    這是典型的插頭 DP 應用。
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    ptr = 1

    for case_idx in range(1, T + 1):
        N = int(input_data[ptr])
        M = int(input_data[ptr+1])
        ptr += 2

        grid = []
        last_r, last_c = -1, -1
        for r in range(N):
            row = [int(x) for x in input_data[ptr]]
            grid.append(row)
            for c in range(M):
                if row[c] == 1:
                    last_r, last_c = r, c
            ptr += 1

        if last_r == -1: # 沒有需要覆蓋的格子
            print(f"Case {case_idx}: 1")
            continue

        MOD = 1000000007
        # dp[狀態] = 方法數
        dp = {0: 1}

        # 狀態編碼：3 進位 (0: 無插頭, 1: 左括號, 2: 右括號)
        # 總共 M+1 個插頭位置

        for r in range(N):
            # 換行處理：將插頭狀態左移一位
            new_dp = {}
            for state, count in dp.items():
                if (state >> (2 * M)) & 3 == 0:
                    new_dp[state << 2] = count
            dp = new_dp

            for c in range(M):
                new_dp = {}
                for state, count in dp.items():
                    # 取得當前格子的左側插頭 (left) 與上方插頭 (up)
                    left = (state >> (2 * c)) & 3
                    up = (state >> (2 * (c + 1))) & 3

                    # 清除這兩個位置的狀態，準備更新
                    base_state = state & ~(3 << (2 * c)) & ~(3 << (2 * (c + 1)))

                    if grid[r][c] == 0: # 障礙物，不能有插頭
                        if left == 0 and up == 0:
                            new_dp[base_state] = (new_dp.get(base_state, 0) + count) % MOD
                    else: # 非障礙物，必須有兩個插頭
                        if left == 0 and up == 0:
                            # 新建一個括號對 (1, 2)
                            ns = base_state | (1 << (2 * c)) | (2 << (2 * (c + 1)))
                            new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                        elif left == 0 or up == 0:
                            # 延續插頭 (橫向或縱向)
                            plug = left or up
                            ns1 = base_state | (plug << (2 * c))
                            ns2 = base_state | (plug << (2 * (c + 1)))
                            new_dp[ns1] = (new_dp.get(ns1, 0) + count) % MOD
                            new_dp[ns2] = (new_dp.get(ns2, 0) + count) % MOD
                        elif left == 1 and up == 1:
                            # 兩個左插頭碰撞，需將對應的右括號改成左括號
                            temp_state = base_state
                            stack = 1
                            for i in range(c + 2, M + 1):
                                target = (temp_state >> (2 * i)) & 3
                                if target == 1: stack += 1
                                elif target == 2: stack -= 1
                                if stack == 0:
                                    ns = temp_state & ~(3 << (2 * i)) | (1 << (2 * i))
                                    new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                                    break
                        elif left == 2 and up == 2:
                            # 兩個右插頭碰撞，需將對應的左括號改成右括號
                            temp_state = base_state
                            stack = 1
                            for i in range(c - 1, -1, -1):
                                target = (temp_state >> (2 * i)) & 3
                                if target == 2: stack += 1
                                elif target == 1: stack -= 1
                                if stack == 0:
                                    ns = temp_state & ~(3 << (2 * i)) | (2 << (2 * i))
                                    new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                                    break
                        elif left == 2 and up == 1:
                            # 右括號遇上左括號，直接消掉
                            new_dp[base_state] = (new_dp.get(base_state, 0) + count) % MOD
                        elif left == 1 and up == 2:
                            # 左括號遇上右括號，代表一個迴路閉合
                            if r == last_r and c == last_c:
                                if base_state == 0:
                                    new_dp[0] = (new_dp.get(0, 0) + count) % MOD
                dp = new_dp

        print(f"Case {case_idx}: {dp.get(0, 0)}")

if __name__ == "__main__":
    solve()
