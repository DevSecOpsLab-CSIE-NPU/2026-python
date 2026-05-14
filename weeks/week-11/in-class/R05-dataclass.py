# R05. dataclass（Python 3.7+）
# @dataclass / field / __post_init__ / frozen

from dataclasses import dataclass, field

# ── 基本 @dataclass：自動產生 __init__ / __repr__ / __eq__ ─
@dataclass
class Point:
    x: float
    y: float

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
p3 = Point(0.0, 0.0)

print(p1)               # Point(x=3.0, y=4.0)
print(p1 == p2)         # True  （自動比較欄位）
print(p1.distance())    # 5.0

# ── 預設值 / field ────────────────────────────────────────
@dataclass
class Student:
    name: str
    student_id: str
    scores: list = field(default_factory=list)  # 可變預設值用 field()
    grade: str = "A"                            # 不可變預設值直接給

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0.0


s = Student("王小明", "11144050001")
s.add_score(85)
s.add_score(92)
print(s)
print(s.average())  # 88.5

# ── frozen=True：不可變（類似 namedtuple）────────────────
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080

cfg = Config("localhost")
print(cfg)          # Config(host='localhost', port=8080)

try:
    cfg.port = 9090  # 不可修改
except Exception as e:
    print(type(e).__name__, e)

# ── __post_init__：初始化後的額外處理 ────────────────────
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)     # 不由外部傳入

    def __post_init__(self):
        self.area = self.width * self.height


r = Rectangle(4.0, 6.0)
print(r)        # Rectangle(width=4.0, height=6.0, area=24.0)
