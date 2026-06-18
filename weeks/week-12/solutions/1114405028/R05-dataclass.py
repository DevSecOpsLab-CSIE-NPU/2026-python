# R05. dataclass 示範
# 這個範例說明 Python dataclass 的基本用法、field、frozen 與 __post_init__。

from dataclasses import dataclass, field


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
print(p1 == p2)         # True，dataclass 自動生成比較方法
print(p1.distance())    # 5.0


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


@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080


cfg = Config("localhost")
print(cfg)          # Config(host='localhost', port=8080)

try:
    cfg.port = 9090
except Exception as e:
    print(type(e).__name__, e)


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


r = Rectangle(4.0, 6.0)
print(r)  # Rectangle(width=4.0, height=6.0, area=24.0)
