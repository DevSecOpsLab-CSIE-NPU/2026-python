import sys

def solve(text):
    nums = list(map(int, text.split()))
    if not nums:
        return ""
    
    it = iter(nums)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        dislike = [set() for _ in range(n)]
        for i in range(n):
            while True:
                x = next(it)
                if x == 0:
                    break
                dislike[i].add(x)

        names = [chr(ord('A') + i) for i in range(n)]
        ans = None
        for perm in itertools.permutations(names):
            if all((j + 1) not in dislike[i] for i, j in enumerate(perm)):
                ans = "".join(perm)
                break
        out.append(ans)

    return "\n".join(out) + "\n"

def main():
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()
    