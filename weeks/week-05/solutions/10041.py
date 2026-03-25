import sys

def calculate_min_distance(addresses):
    if not addresses:
        return 0
    addresses.sort()
    n = len(addresses)
    if n % 2 == 1:
        median = addresses[n // 2]
    else:
        median = addresses[n // 2 - 1]
    total_distance = sum(abs(addr - median) for addr in addresses)
    return total_distance

def main():
    data = sys.stdin.read().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        r = int(data[index])
        index += 1
        addresses = []
        for i in range(r):
            addresses.append(int(data[index]))
            index += 1
        result = calculate_min_distance(addresses)
        print(result)

if __name__ == "__main__":
    main()