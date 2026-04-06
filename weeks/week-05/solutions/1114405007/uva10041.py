from sys import stdin


# 取排序後的中位數，能讓所有親戚到新家的距離總和最小。
def minimum_total_distance(addresses):
    sorted_addresses = sorted(addresses)
    median_address = sorted_addresses[len(sorted_addresses) // 2]
    return sum(abs(address - median_address) for address in sorted_addresses)


# 依照題目輸入格式逐組處理，回傳每組的最小距離總和。
def solve(data):
    test_case_count = int(data[0])
    results = []
    index = 1

    for _ in range(test_case_count):
        relative_count = int(data[index])
        index += 1
        addresses = list(map(int, data[index:index + relative_count]))
        index += relative_count
        results.append(str(minimum_total_distance(addresses)))

    return "\n".join(results)


def main():
    tokens = stdin.read().split()
    if not tokens:
        return

    print(solve(tokens))


if __name__ == "__main__":
    main()