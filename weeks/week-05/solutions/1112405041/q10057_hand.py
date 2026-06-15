import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    curr = 0
    while curr < len(input_data):
        try:
            n = int(input_data[curr])
            curr += 1
            x = []
            for _ in range(n):
                x.append(int(input_data[curr]))
                curr += 1

            x.sort()

            # Find medians
            # If n is odd: m1 = m2 = x[n//2]
            # If n is even: m1 = x[(n-1)//2], m2 = x[n//2]
            m1 = x[(n - 1) // 2]
            m2 = x[n // 2]

            # Count how many Xi in input are in range [m1, m2]
            count = 0
            for val in x:
                if m1 <= val <= m2:
                    count += 1

            # Number of possible integer A's
            possible_a = m2 - m1 + 1

            print(f"{m1} {count} {possible_a}")
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    solve()
