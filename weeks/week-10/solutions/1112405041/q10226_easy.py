import sys

def solve():
    """
    UVA 10226 魔改版：字典序排列且只輸出差異部分
    解法：使用回溯法 (Backtracking) 產生字典序排列，
    並維護上一個排列的紀錄，只印出與上一個排列不同的部分。
    """
    lines = sys.stdin.readlines()
    if not lines:
        return

    line_idx = 0
    while line_idx < len(lines):
        try:
            line = lines[line_idx].strip()
            if not line:
                line_idx += 1
                continue
            N = int(line)
        except (ValueError, IndexError):
            break
        line_idx += 1

        # 讀取每個人不想排的位置
        constraints = []
        for _ in range(N):
            # 以 0 結尾的數列
            parts = list(map(int, lines[line_idx].strip().split()))
            # 過濾掉 0
            constraints.append(set(p for p in parts if p != 0))
            line_idx += 1

        # 產生所有字母 A, B, C...
        people = [chr(ord('A') + i) for i in range(N)]
        used = [False] * N
        current_path = []
        last_path = [None] * N

        def backtrack(depth):
            if depth == N:
                # 輸出邏輯：只輸出與上次不同的部分
                diff_idx = 0
                while diff_idx < N and current_path[diff_idx] == last_path[diff_idx]:
                    diff_idx += 1

                # 從第一個不同的地方開始印
                print(" " * diff_idx + "".join(current_path[diff_idx:]))

                # 更新 last_path
                for i in range(N):
                    last_path[i] = current_path[i]
                return

            for i in range(N):
                if not used[i]:
                    # 檢查限制：第 i 個人 (people[i]) 不想排在 depth+1 的位置
                    if (depth + 1) in constraints[i]:
                        continue

                    used[i] = True
                    current_path.append(people[i])
                    backtrack(depth + 1)
                    current_path.pop()
                    used[i] = False

        backtrack(0)

if __name__ == "__main__":
    solve()
