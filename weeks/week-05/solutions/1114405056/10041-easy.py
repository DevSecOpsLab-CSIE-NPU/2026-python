from __future__ import annotations

import sys


def minimum_total_distance(addresses: list[int]) -> int:
    # 這題的關鍵是：
    # 如果想讓「到所有親戚的距離總和」最小，
    # 把房子選在排序後的中間位置就可以了，也就是中位數。
    addresses.sort()

    # 排序後的中間那一間，就是最適合當作新家的位置。
    middle_index = len(addresses) // 2
    best_address = addresses[middle_index]

    # 再把這個位置到每個親戚家的距離全部加總。
    total_distance = 0
    for address in addresses:
        total_distance += abs(address - best_address)

    return total_distance


def solve(data: str) -> str:
    # 把整份輸入先切成一個個數字，依照題目格式慢慢取用。
    parts = data.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    index = 1
    outputs: list[str] = []

    for _ in range(case_count):
        # 每組資料開頭先給親戚人數，後面才是真正的地址清單。
        count = int(parts[index])
        index += 1

        addresses: list[int] = []
        for _ in range(count):
            addresses.append(int(parts[index]))
            index += 1

        outputs.append(str(minimum_total_distance(addresses)))

    return "\n".join(outputs)


def main() -> None:
    # 從標準輸入讀資料，並把答案直接印出。
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()