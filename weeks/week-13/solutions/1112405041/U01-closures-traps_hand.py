def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
def solve():
    c = make_counter(10)
    print(c(), c())
if __name__ == '__main__': solve()
