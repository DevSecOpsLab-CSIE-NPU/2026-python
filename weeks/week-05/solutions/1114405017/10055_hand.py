import sys
input = sys.stdin.read().split()
if not input: exit()
N, Q = int(input[0]), int(input[1])
bit = [0] * (N + 1)
def update(i):
    while i <= N:
        bit[i] ^= 1   
        i += i & -i 
def query(i):
    res = 0
    while i > 0:
        res ^= bit[i]
        i -= i & -i
    return res
ptr = 2
out = []
for _ in range(Q):
    op = input[ptr]
    if op == '1':
        idx = int(input[ptr+1])
        update(idx)
        ptr += 2
    else:
        L, R = int(input[ptr+1]), int(input[ptr+2])
        out.append(str(query(R) ^ query(L-1)))
        ptr += 3
sys.stdout.write('\n'.join(out) + '\n')