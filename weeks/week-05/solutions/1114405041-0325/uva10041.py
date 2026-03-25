"""UVA 10041 - Vito's Family（主解法）。

本檔案採用「中位數」性質：
對一組數列，選擇中位數可以讓到所有點的絕對距離總和最小。
時間複雜度主要是排序 O(r log r)。
"""

from __future__ import annotations


def minimum_total_distance(addresses: list[int]) -> int:
    """計算最小總距離。

    參數:
        addresses: 親戚門牌號碼清單（可重複）。

    回傳:
        以最佳房子位置（中位數）為基準時的最小距離總和。
    """
    if not addresses:
        return 0

    # 先排序，方便取得中位數。
    sorted_addresses = sorted(addresses)

    # 若長度為偶數，選中間偏左或偏右都可以得到同樣最小值。
    median = sorted_addresses[len(sorted_addresses) // 2]

    # 計算所有地址到中位數的絕對距離總和。
    return sum(abs(x - median) for x in sorted_addresses)


def solve_io(data: str) -> str:
    """依 UVA 輸入格式解析並輸出答案。"""
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    outputs: list[str] = []

    for _ in range(t):
        r = int(tokens[idx])
        idx += 1

        # 讀取此測資的 r 個門牌。
        addresses = [int(tokens[idx + i]) for i in range(r)]
        idx += r

        outputs.append(str(minimum_total_distance(addresses)))

    return "\n".join(outputs)


def main() -> None:
    import sys

    input_data = sys.stdin.read()
    result = solve_io(input_data)
    if result:
        print(result)


if __name__ == "__main__":
    main()
