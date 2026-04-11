import sys
def run():
    line_input = sys.stdin.readline()
    if not line_input: return
    n = int(line_input.strip())
    counts = {}
    for _ in range(n):
        text = sys.stdin.readline()
        for char in text:
            if char.isalpha():
                c = char.upper()
                if c in counts: counts[c] += 1
                else: counts[c] = 1
    items = list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    for char, count in items:
        print(f"{char} {count}")
if __name__ == "__main__":
    run()