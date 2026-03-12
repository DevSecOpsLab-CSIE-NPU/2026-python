# R10. 去重且保序（1.10）
# 利用 set 記錄見過的值，生成器保留原順序。

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == "__main__":
    data = [1, 2, 1, 3, 2, 4]
    print("original", data)
    print("dedupe", list(dedupe(data)))
    print("dedupe2 by value", list(dedupe2(data)))
    data2 = [{'id': 1}, {'id': 2}, {'id': 1}]
    print("dedupe2 by key (id)", list(dedupe2(data2, key=lambda d: d['id'])))
