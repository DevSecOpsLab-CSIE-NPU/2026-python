import sys

# 手打版本：模擬現場實作，保持邏輯清晰
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    while ptr < len(input_data):
        try:
            n = int(input_data[ptr])
            ptr += 1
        except:
            break

        dislike = []
        for i in range(n):
            row_dislike = set()
            while True:
                val = int(input_data[ptr])
                ptr += 1
                if val == 0:
                    break
                row_dislike.add(val)
            dislike.append(row_dislike)

        names = [chr(65+i) for i in range(n)]
        used = [False] * n
        curr = []
        prev = [""] * n

        def run(depth):
            if depth == n:
                start_idx = 0
                while start_idx < n and curr[start_idx] == prev[start_idx]:
                    start_idx += 1
                print(" " * start_idx + "".join(curr[start_idx:]))
                for i in range(n):
                    prev[i] = curr[i]
                return

            for i in range(n):
                if not used[i]:
                    if (depth + 1) in dislike[i]:
                        continue
                    used[i] = True
                    curr.append(names[i])
                    run(depth + 1)
                    curr.pop()
                    used[i] = False

        run(0)

if __name__ == "__main__":
    solve()
