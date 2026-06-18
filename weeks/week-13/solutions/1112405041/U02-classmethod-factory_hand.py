class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_string(cls, s):
        x, y = map(int, s.split(','))
        return cls(x, y)
    def __repr__(self): return f"Point({self.x}, {self.y})"
if __name__ == '__main__': print(Point.from_string("3,4"))
