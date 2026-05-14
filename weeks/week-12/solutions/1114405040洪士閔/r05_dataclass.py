"""R05. dataclass。

這份版本示範 @dataclass、field、frozen、__post_init__，
讓資料類別的用途與優點更容易記憶。
"""

from dataclasses import dataclass, field


# 基本 dataclass：自動幫我們產生 __init__ / __repr__ / __eq__。
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
print(p1 == p2)         # True  （欄位自動比較）
print(p1.distance())    # 5.0


# field(default_factory=list) 可以避免所有實例共用同一個可變 list。
@dataclass
class Student:
    name: str
    student_id: str
    scores: list = field(default_factory=list)
    grade: str = "A"

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0.0


s = Student("王小明", "11144050001")
s.add_score(85)
s.add_score(92)
print(s)
print(s.average())  # 88.5


# frozen=True：建立後不可再修改，類似不可變物件。
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080


cfg = Config("localhost")
print(cfg)          # Config(host='localhost', port=8080)

try:
    cfg.port = 9090  # 這裡會失敗，因為 frozen=True
except Exception as e:
    print(type(e).__name__, e)


# __post_init__：在 dataclass 初始化完之後，再做額外處理。
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


r = Rectangle(4.0, 6.0)
print(r)        # Rectangle(width=4.0, height=6.0, area=24.0)
