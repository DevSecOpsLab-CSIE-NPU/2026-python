"""R05 Counter / defaultdict / namedtuple 詳細註解版。"""

from collections import Counter, defaultdict, namedtuple


def main():
    # Counter 最適合做「值出現幾次」的統計。
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    cnt = Counter(words)
    print(cnt)
    print(cnt.most_common(2))

    # defaultdict(list) 可以少掉 if key not in dict 的判斷。
    records = [("系資", "Alice"), ("電子", "Bob"), ("系資", "Carol")]
    grouped = defaultdict(list)
    for dept, name in records:
        grouped[dept].append(name)
    print(dict(grouped))

    # defaultdict(int) 常用來做累加。
    scores = [("Alice", 90), ("Bob", 80), ("Alice", 85)]
    totals = defaultdict(int)
    for name, score in scores:
        totals[name] += score
    print(dict(totals))

    # namedtuple 讓 tuple 可以用欄位名稱讀值。
    Stock = namedtuple("Stock", ["symbol", "price", "change"])
    stock = Stock("AA", 39.48, -0.18)
    print(stock.symbol, stock.price, stock.change)


if __name__ == "__main__":
    main()
