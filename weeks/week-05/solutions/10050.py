import sys

def is_working_day(day):
    weekday = ((day - 1) % 7) + 1
    return weekday not in [6, 7]

def has_hartal(day, hartals):
    for h in hartals:
        if day % h == 0:
            return True
    return False

def calculate_lost_days(N, hartals):
    lost = 0
    for day in range(1, N + 1):
        if is_working_day(day) and has_hartal(day, hartals):
            lost += 1
    return lost

def main():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    index = 1
    for _ in range(T):
        N = int(input_data[index])
        index += 1
        P = int(input_data[index])
        index += 1
        hartals = []
        for i in range(P):
            hartals.append(int(input_data[index]))
            index += 1
        result = calculate_lost_days(N, hartals)
        print(result)

if __name__ == "__main__":
    main()