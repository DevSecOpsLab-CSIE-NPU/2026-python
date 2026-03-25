import sys

def calculate_probability(N, p, i):
    if p == 0:
        return 0.0
    q = 1 - p
    if q ** N == 1:
        return 1.0 if i == 1 else 0.0
    prob = p * (q ** (i - 1)) / (1 - q ** N)
    return prob

def main():
    input_data = sys.stdin.read().split()
    S = int(input_data[0])
    index = 1
    for _ in range(S):
        N = int(input_data[index])
        p = float(input_data[index + 1])
        i = int(input_data[index + 2])
        index += 3
        prob = calculate_probability(N, p, i)
        print(f"{prob:.4f}")

if __name__ == "__main__":
    main()