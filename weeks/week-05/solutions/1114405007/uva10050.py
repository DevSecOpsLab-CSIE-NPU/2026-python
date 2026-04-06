from sys import stdin


# 依照每個政黨的罷會週期標記天數，並排除每週五、六。
def count_lost_days(day_count, hartal_parameters):
    lost_days = set()

    for parameter in hartal_parameters:
        for day in range(parameter, day_count + 1, parameter):
            weekday = day % 7
            if weekday in (6, 0):
                continue
            lost_days.add(day)

    return len(lost_days)


# 讀取多組測資後，輸出每組實際損失的工作天數。
def solve(data):
    test_case_count = int(data[0])
    index = 1
    results = []

    for _ in range(test_case_count):
        day_count = int(data[index])
        index += 1
        party_count = int(data[index])
        index += 1
        hartal_parameters = list(map(int, data[index:index + party_count]))
        index += party_count
        results.append(str(count_lost_days(day_count, hartal_parameters)))

    return "\n".join(results)


def main():
    tokens = stdin.read().split()
    if not tokens:
        return
    print(solve(tokens))


if __name__ == "__main__":
    main()