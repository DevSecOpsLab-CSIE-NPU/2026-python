import sys


flag = True


def main():
    ans = []
    state = [True]

    for line in sys.stdin:
        for ch in line:
            if ch == '"':
                ans.append('``' if state[0] else "''")
                state[0] = not state[0]
            else:
                ans.append(ch)

    sys.stdout.write(''.join(ans))


if __name__ == '__main__':
    main()