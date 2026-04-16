"""
Task 1: Sequence Clean

輸入一行以空白分隔的整數，輸出：
1. 去重後（保留第一次出現順序）的序列
2. 由小到大排序結果（含重複）
3. 由大到小排序結果（含重複）
4. 偶數序列（維持原始順序，含重複）
"""


def dedupe_ordered(nums: list[int]) -> list[int]:
    """去重，保留第一次出現順序，使用 seen set 追蹤已出現的元素。"""
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


def sort_asc(nums: list[int]) -> list[int]:
    """原始序列由小到大排序（保留重複值）。"""
    return sorted(nums)


def sort_desc(nums: list[int]) -> list[int]:
    """原始序列由大到小排序（保留重複值）。"""
    return sorted(nums, reverse=True)


def filter_evens(nums: list[int]) -> list[int]:
    """從原始序列篩出偶數，維持原始順序。"""
    return [n for n in nums if n % 2 == 0]


def sequence_clean(line: str) -> None:
    """解析一行整數並輸出四種序列結果。"""
    nums = list(map(int, line.split()))
    dedupe = dedupe_ordered(nums)
    asc = sort_asc(nums)
    desc = sort_desc(nums)
    evens = filter_evens(nums)

    print("dedupe:", " ".join(map(str, dedupe)))
    print("asc:", " ".join(map(str, asc)))
    print("desc:", " ".join(map(str, desc)))
    print("evens:", " ".join(map(str, evens)))


if __name__ == "__main__":
    line = input()
    sequence_clean(line)
