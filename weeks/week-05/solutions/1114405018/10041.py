from typing import List


def min_total_distance(addresses: List[int]) -> int:
    """回傳新家到所有親戚門牌的最小總距離。"""
    if not addresses:
        return 0

    # 將門牌排序後，選擇中位數位置可使絕對距離總和最小。
    sorted_addresses = sorted(addresses)
    median = sorted_addresses[len(sorted_addresses) // 2]
    # 計算所有親戚到中位數門牌的距離總和。
    return sum(abs(a - median) for a in sorted_addresses)


def solve(data: str) -> str:
    """處理 UVA 10041 輸入格式，回傳每組答案。"""
    tokens = list(map(int, data.split()))
    if not tokens:
        return ""

    # 第一個整數是測資組數，後續用 idx 逐段讀取每組資料。
    t = tokens[0]
    idx = 1
    outputs = []

    for _ in range(t):
        r = tokens[idx]
        idx += 1
        # 讀取本組的 r 個門牌，並將索引往後移。
        addresses = tokens[idx:idx + r]
        idx += r
        outputs.append(str(min_total_distance(addresses)))

    return "\n".join(outputs)


if __name__ == "__main__":
    import sys

    # 從標準輸入讀完整資料並輸出答案。
    input_data = sys.stdin.read()
    print(solve(input_data))
