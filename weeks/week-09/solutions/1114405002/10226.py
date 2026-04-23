import sys

def backtrack(current, used, forbidden, N, perms):
    if len(current) == N:
        perms.append(current[:])
        return
    for i in range(N):
        if not used[i] and (len(current) + 1 not in forbidden[i]):
            used[i] = True
            current.append(i)
            backtrack(current, used, forbidden, N, perms)
            current.pop()
            used[i] = False

def main():
    with open('test_input_10226.txt', 'r') as f:
        data = f.read().split()
    index = 0
    with open('10226_test.log', 'w') as log:
        while index < len(data):
            N = int(data[index])
            index += 1
            forbidden = []
            for i in range(N):
                f = set()
                while True:
                    pos = int(data[index])
                    index += 1
                    if pos == 0:
                        break
                    f.add(pos)
                forbidden.append(f)
            perms = []
            backtrack([], [False] * N, forbidden, N, perms)
            # now print
            prev = None
            for perm in perms:
                s = ''.join(chr(ord('A') + p) for p in perm)
                if prev is None:
                    log.write(s + '\n')
                    prev = s
                    continue
                i = 0
                while i < len(s) and i < len(prev) and s[i] == prev[i]:
                    i += 1
                if i < len(s):
                    log.write(s[i:] + '\n')
                    prev = s

if __name__ == "__main__":
    main()