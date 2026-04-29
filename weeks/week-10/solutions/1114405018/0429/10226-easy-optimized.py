import sys


def parse_cases(text):
    """解析輸入文本，提取每個測試案例的人數和他們的不喜歡位置集合"""
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

            # 將0之前的所有數字作為不喜歡的位置
            banned = set()
            for x in nums:
                if x == 0:
                    break
                banned.add(x)
            dislike.append(banned)

        cases.append((n, dislike))

    return cases


def compress(lines):
    """壓縮輸出：只保留與前一行不同的部分"""
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


def solve_case_backtracking(n, dislike):
    """
    使用回溯算法生成所有有效的排列。
    
    優點：避免生成無效排列，在構建過程中進行剪枝。
    對於存在許多限制的情況，效率比蠻力法高。
    """
    valid_perms = []
    used = [False] * n  # 追蹤已使用的人
    current = []

    def backtrack(pos):
        """
        回溯函數
        pos: 當前要填的位置（1-based），從1到n
        """
        if pos > n:
            # 找到一個完整有效的排列
            valid_perms.append("".join(current))
            return

        # 嘗試在當前位置放置每一個人
        for person_idx in range(n):
            if used[person_idx]:
                continue

            person_label = chr(ord("A") + person_idx)

            # 檢查這個人是否允許在這個位置
            if pos not in dislike[person_idx]:
                # 放置這個人
                used[person_idx] = True
                current.append(person_label)

                # 遞迴到下一個位置
                backtrack(pos + 1)

                # 回溯
                current.pop()
                used[person_idx] = False

    backtrack(1)
    return "\n".join(compress(valid_perms))


def solve(text):
    """求解所有測試案例"""
    cases = parse_cases(text)
    blocks = [solve_case_backtracking(n, dislike) for n, dislike in cases]
    return "\n\n".join(blocks) + "\n"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
