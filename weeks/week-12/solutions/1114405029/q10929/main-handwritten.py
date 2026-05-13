import sys

def main():
    for line in sys.stdin:
        s = line.strip()

        if s == "0":
            break

        odd_sum = 0
        even_sum = 0

        for i in range(len(s)):
            digit = int(s[i])

            if i % 2 == 0:
                odd_sum += digit
            else:
                even_sum += digit

        difference = abs(odd_sum - even_sum)

        if difference % 11 == 0:
            print(f"{s} is a multiple of 11.")
        else:
            print(f"{s} is not a multiple of 11.")

if __name__ == "__main__":
    main()