"""0617 任務二 — linear_search vs binary_search 效能測試

目的:
- 使用自己實作的 timeit 裝飾器
- 比較 linear_search 與 binary_search 的搜尋時間
- 把結果提供給 README.md 撰寫效能評估
"""

from timing import timeit
from search import linear_search, binary_search


DATA_SIZE = 100_000
REPEAT = 100

data = list(range(DATA_SIZE))
target = DATA_SIZE - 1


@timeit(repeat=REPEAT)
def timed_linear_search():
    return linear_search(data, target)


@timeit(repeat=REPEAT)
def timed_binary_search():
    return binary_search(data, target)


def main():
    linear_result = timed_linear_search()
    binary_result = timed_binary_search()

    print("linear_search result:", linear_result)
    print("binary_search result:", binary_result)

    print("linear_search average elapsed:", timed_linear_search.last_elapsed)
    print("binary_search average elapsed:", timed_binary_search.last_elapsed)

    print("linear_search records count:", len(timed_linear_search.records))
    print("binary_search records count:", len(timed_binary_search.records))


if __name__ == "__main__":
    main()