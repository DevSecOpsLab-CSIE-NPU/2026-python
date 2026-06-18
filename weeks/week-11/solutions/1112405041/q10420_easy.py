# AI Easy 版: 10420 List of Conquests
import sys

def solve():
    """
    統計各個國家的征服次數並依國家名稱字典序排序輸出。
    """
    lines = sys.stdin.read().splitlines()
    if not lines: return

    try:
        n = int(lines[0])
    except ValueError: return

    stats = {}
    for i in range(1, n + 1):
        if i >= len(lines): break
        parts = lines[i].split()
        if not parts: continue

        country = parts[0]
        stats[country] = stats.get(country, 0) + 1

    for country in sorted(stats.keys()):
        print(f"{country} {stats[country]}")

if __name__ == "__main__":
    solve()
