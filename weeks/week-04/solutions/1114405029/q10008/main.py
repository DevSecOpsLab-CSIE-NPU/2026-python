import sys
from collections import Counter

def solve():
    # 使用 sys.stdin.read().splitlines() 快速讀取所有內容
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    # 第一行是列數 n
    n = int(lines[0])
    # 將後續 n 行合併，只保留字母並轉大寫
    text = "".join(lines[1:1+n])
    letters = [c.upper() for c in text if c.isalpha()]
    
    # 使用 Counter 統計頻率
    counts = Counter(letters)
    
    # 多條件排序：次數取負(降序), 字母(升序)
    results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in results:
        print(f"{char} {count}")

if __name__ == "__main__":
    solve()