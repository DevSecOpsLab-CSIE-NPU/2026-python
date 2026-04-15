import sys

def build_map():
   
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    table = {" ": " "}

    for row in rows:
        for i in range(1, len(row)):
            table[row[i]] = row[i - 1]

    return table

def solve(text):
    table = build_map()
    out = []

    for line in text.splitlines():
        out.append("".join(table.get(ch, ch) for ch in line))

    return "\n".join(out)

def main():
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()