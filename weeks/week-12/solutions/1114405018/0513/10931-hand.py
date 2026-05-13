def get_parity_output(number):
  
    binary = bin(number)[2:]  
    ones = binary.count('1')
    return f"The parity of {binary} is {ones} (mod 2)."


def main():
    while True:
        n = input().strip()
        if n == "0":
            break
        print(get_parity_output(int(n)))


if __name__ == "__main__":
    main()