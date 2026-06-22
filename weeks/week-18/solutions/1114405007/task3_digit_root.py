def digit_root(x, base):
    if x == 0:
        return 0
    return 1 + ((x - 1) % (base - 1))


def solve(input_text, base):
    lines = input_text.splitlines()
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        out.append(str(digit_root(x, base)))
    return "\n".join(out) + ("\n" if out else "")


def get_base(student_id):
    u = student_id % 10
    table = {0: 2, 1: 3, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 11, 8: 13, 9: 16}
    return table[u]


def main():
    import sys
    STUDENT_ID = 1114405007
    BASE = get_base(STUDENT_ID)
    input_text = sys.stdin.read()
    output = solve(input_text, BASE)
    sys.stdout.write(output)


if __name__ == "__main__":
    main()
