import sys
from collections import Counter

# UVA 10226 - Hardwood Species


def solve():
    """
    Standard: 使用 sys.stdin.read 和 collections.Counter 來達到最高效能。
    """
    input_data = sys.stdin.read().split("\n\n")
    if not input_data or not input_data[0]:
        return

    n = int(input_data[0].strip())
    cases = input_data[1:]

    for i, case in enumerate(cases):
        if i > 0:
            print()

        trees = case.strip().split("\n")
        if not trees or trees[0] == "":
            continue

        total = len(trees)
        counts = Counter(trees)

        for tree in sorted(counts.keys()):
            percentage = (counts[tree] / total) * 100
            print(f"{tree} {percentage:.4f}")


def solve_easy():
    """
    Easy: 使用 dict 計算出現次數，內建 sort 排序。
    """
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0])
    idx = 2

    for i in range(n):
        if i > 0:
            print()

        counts = {}
        total = 0
        while idx < len(lines) and lines[idx].strip() != "":
            tree = lines[idx]
            counts[tree] = counts.get(tree, 0) + 1
            total += 1
            idx += 1

        for tree in sorted(counts.keys()):
            percentage = (counts[tree] / total) * 100
            print(f"{tree} {percentage:.4f}")

        idx += 1


def solve_manual():
    """
    Manual: 不使用高階內建函數如 Counter，純手動讀取與計數，方便記憶。
    """
    try:
        cases = int(input())
        input()  # 空行
    except:
        return

    for i in range(cases):
        if i > 0:
            print()

        trees = []
        counts = []
        total = 0

        while True:
            try:
                line = input()
                if line == "":
                    break
            except:
                break

            total += 1
            found = False
            for j in range(len(trees)):
                if trees[j] == line:
                    counts[j] += 1
                    found = True
                    break
            if not found:
                trees.append(line)
                counts.append(1)

        # 手動排序 (Bubble Sort)
        for x in range(len(trees)):
            for y in range(0, len(trees) - x - 1):
                if trees[y] > trees[y + 1]:
                    trees[y], trees[y + 1] = trees[y + 1], trees[y]
                    counts[y], counts[y + 1] = counts[y + 1], counts[y]

        for j in range(len(trees)):
            percentage = (counts[j] / total) * 100
            print(f"{trees[j]} {percentage:.4f}")


if __name__ == "__main__":
    solve()
