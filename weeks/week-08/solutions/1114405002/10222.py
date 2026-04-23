import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    id = int(sys.stdin.readline().strip())
    if is_prime(id):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()