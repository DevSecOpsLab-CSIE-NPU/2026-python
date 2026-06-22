import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    pos = 0
    while pos < len(lines):
        a = lines[pos].strip()
        if a == "":
            pos = pos + 1
            continue
        n = int(a)
        if n == 0:
            break
        pos = pos + 1
        arr = []
        temp = lines[pos].split()
        for t in temp:
            arr.append(int(t))
        pos = pos + 1

        seen = []
        for num in arr:
            ok = True
            for s in seen:
                if s == num:
                    ok = False
                    break
            if ok:
                seen.append(num)

        res = []
        for v in seen:
            if v % 2 == 0:
                res.append(v)

        res.sort()

        if len(res) == 0:
            print("NONE")
        else:
            out = ""
            for i in range(len(res)):
                if i > 0:
                    out = out + " "
                out = out + str(res[i])
            print(out)

if __name__ == "__main__":
    main()
