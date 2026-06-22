import sys

D = 2

def main():
    lines = sys.stdin.read().strip().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "":
            i = i + 1
            continue
        n = int(line)
        if n == 0:
            break
        i = i + 1
        nums = []
        for x in lines[i].split():
            nums.append(int(x))
        i = i + 1

        seen = []
        for v in nums:
            found = False
            for s in seen:
                if s == v:
                    found = True
                    break
            if not found:
                seen.append(v)

        res = []
        for v in seen:
            if v % D == 0:
                res.append(v)

        res.sort()

        if len(res) == 0:
            print("NONE")
        else:
            out = ""
            for j in range(len(res)):
                if j > 0:
                    out = out + " "
                out = out + str(res[j])
            print(out)

if __name__ == "__main__":
    main()
