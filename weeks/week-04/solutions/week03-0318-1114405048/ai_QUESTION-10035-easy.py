import sys


def main():
    for line in sys.stdin:
        a, b = line.split()

        if a == "0" and b == "0":
            break

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        cnt = 0

        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            s = x + y + carry
            if s >= 10:
                cnt += 1
                carry = 1
            else:
                carry = 0

            i -= 1
            j -= 1

        if cnt == 0:
            print("No carry operation.")
        elif cnt == 1:
            print("1 carry operation.")
        else:
            print(f"{cnt} carry operations.")


if __name__ == "__main__":
    main()