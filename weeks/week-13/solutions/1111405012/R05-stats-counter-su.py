"""R05 Counter / defaultdict / namedtuple 簡化版。"""

from collections import Counter, defaultdict, namedtuple


def main():
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    cnt = Counter(words)
    print(cnt)
    print(cnt.most_common(2))

    records = [("系資", "Alice"), ("電子", "Bob"), ("系資", "Carol")]
    grouped = defaultdict(list)
    for dept, name in records:
        grouped[dept].append(name)
    print(dict(grouped))

    scores = [("Alice", 90), ("Bob", 80), ("Alice", 85)]
    totals = defaultdict(int)
    for name, score in scores:
        totals[name] += score
    print(dict(totals))

    Stock = namedtuple("Stock", ["symbol", "price", "change"])
    stock = Stock("AA", 39.48, -0.18)
    print(stock.symbol, stock.price, stock.change)


if __name__ == "__main__":
    main()
