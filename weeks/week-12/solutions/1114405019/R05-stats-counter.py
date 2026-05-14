# R05-stats-counter.py
# 使用 collections 中的 Counter, defaultdict 與 namedtuple

from collections import Counter, defaultdict, namedtuple

def collections_demo():
    # 1. Counter: 快速計算頻率
    # 常用於統計單字出現次數、字元出現次數等
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_counts = Counter(words)
    print(f"計數結果: {word_counts}")
    print(f"出現次數最多的前 1 名: {word_counts.most_common(1)}")
    print(f"Apple 出現次數: {word_counts['apple']}")

    # 2. defaultdict: 避免 KeyError 的字典
    # 當存取不存在的 key 時，會自動根據提供的工廠函數建立預設值 (例如 list, int)
    groups = defaultdict(list)
    groups['fruits'].append('apple')
    groups['fruits'].append('banana')
    groups['veggies'].append('carrot')
    print(f"\nDefaultDict 分組結果: {dict(groups)}")

    # 3. namedtuple: 具名元組
    # 讓 tuple 的元素可以透過名稱存取，提升程式碼可讀性，且依然具備 tuple 的輕量特性
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"\n座標物件: {p}")
    print(f"存取屬性: x={p.x}, y={p.y}")
    print(f"解構賦值: {p[0]}, {p[1]}")

if __name__ == "__main__":
    print("=== Collections 工具模組示範 ===")
    collections_demo()
