# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85)
print(str(s))    # 王小明：85 分
print(s)         # 王小明：85 分（print 優先用 __str__）

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 沒有 __eq__ 的話，兩個物件只有「同一個記憶體位置」才算相等

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # True（座標相同）
print(p1 == p3)  # False
print(p1 is p2)  # False（是不同的物件，記憶體位置不同）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 只要定義 __eq__ 和一個比較（__lt__），
# @total_ordering 會自動補出 <=, >, >= 四個

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)
b = Score(90)
print(a < b)   # True
print(a > b)   # False（自動生成）
print(a <= b)  # True（自動生成）

scores = [Score(70), Score(95), Score(60)]
print(sorted(scores))  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有一個 __dict__，很耗記憶體
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省

class PointLite:
    __slots__ = ('x', 'y')   # 固定只有這兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# ── 更多常見的特殊方法範例（容器、可呼叫、上下文管理） ────────
class SimpleCollection:
    """示範容器行為：實作 len/iter/contains/getitem/setitem/delitem

    同時示範 __add__、__iadd__、以及把物件當函數呼叫的 __call__。
    """
    def __init__(self, items=None):
        self._items = list(items) if items is not None else []

    def __repr__(self):
        return f"SimpleCollection({self._items!r})"

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, idx):
        return self._items[idx]

    def __setitem__(self, idx, value):
        self._items[idx] = value

    def __delitem__(self, idx):
        del self._items[idx]

    def __add__(self, other):
        return SimpleCollection(self._items + list(other))

    def __iadd__(self, other):
        self._items += list(other)
        return self

    def __call__(self, *args, **kwargs):
        """把 collection 當作可呼叫物件：回傳所有元素總和（示範用）"""
        return sum(self._items)

print('\n=== 容器與特殊方法示範 ===')
col = SimpleCollection([1, 2, 3])
print('repr:', repr(col))
print('len:', len(col))
print('iterate:', [x for x in col])
print('contains 2?', 2 in col)
print('index 1:', col[1])
col[1] = 5
print('修改後:', col)
del col[0]
print('刪除後:', col)
col2 = col + [10, 20]
print('相加後:', col2)
col += [7]
print('原地相加後:', col)
print('當函數呼叫 col():', col())

# 上下文管理（class 實作）的範例：
class DummyLock:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"取得鎖：{self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"釋放鎖：{self.name}")
        # 不吃掉例外，讓錯誤繼續向上傳
        return False

print('\n=== Context manager（class）示範 ===')
with DummyLock('L1'):
    print('在鎖內執行工作')

# 記憶重點 ──────────────────────────────────────────────────
# __repr__  → 開發者用，要能「重現」物件（或方便 debug）
# __str__   → 使用者用，print() 呼叫
# __eq__    → 自訂 == 的意義（通常搭配 __hash__）
# @total_ordering + __lt__ → 自動補齊 <, <=, >, >=（只需實作 __eq__ 和 __lt__）
# __slots__ → 固定屬性，大量物件時省記憶體
# 常見其他方法：
# - __len__, __iter__, __contains__, __getitem__, __setitem__, __delitem__ → 實作容器協定
# - __add__, __iadd__ → 支援 +、+=
# - __call__ → 讓物件可像函數一樣被呼叫
# - __enter__, __exit__ → 實作上下文管理（with）
