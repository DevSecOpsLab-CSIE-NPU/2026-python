from timing import timeit
from search import linear_search, binary_search

data = list(range(1, 100001))
target = 99999

@timeit
def test_linear():
    return linear_search(data, target)

@timeit
def test_binary():
    return binary_search(data, target)

test_linear()
test_binary()

print(f"linear 花了: {test_linear.last_elapsed:.6f} 秒")
print(f"binary 花了: {test_binary.last_elapsed:.6f} 秒")
