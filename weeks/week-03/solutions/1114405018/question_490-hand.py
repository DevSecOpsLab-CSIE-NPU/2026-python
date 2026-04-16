import  sys

lines = sys.stdin.read().splitlines()
if not lines:
    raise SystemExit

w = max(len(s) for s in lines)
ans = []

for c in range(w):
    row = ""
    for r in range(len(lines) - 1, -1, -1):
        row += lines[r][c] if c < len(lines[r]) else " "
    ans.append(row.rstrip())
    
sys.stdout.write("\n".join(ans))
