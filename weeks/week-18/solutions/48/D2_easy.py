import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    idx = 0
    while idx < len(data):
        line = data[idx].strip()
        if not line:
            idx += 1
            continue
        n = int(line)
        if n == 0:
            break
        idx += 1
        nums = list(map(int, data[idx].split()))
        idx += 1

        seen = set()
        uniq = []
        for x in nums:
            if x not in seen:
                seen.add(x)
                uniq.append(x)

        filtered = [x for x in uniq if x % 2 == 0]

        filtered.sort()

        if not filtered:
            print("NONE")
        else:
            print(" ".join(map(str, filtered)))

if __name__ == "__main__":
    main()
