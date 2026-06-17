"""U02: classmethod factory constructors."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, text):
        x, y = map(int, text.split(","))
        return cls(x, y)

    @classmethod
    def from_list(cls, values):
        return cls(values[0], values[1])

    @classmethod
    def origin(cls):
        return cls(0, 0)


class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"


class CostTable:
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        if len(costs) != 36:
            raise ValueError("cost table must contain 36 integers")
        self.costs = costs

    def total_cost(self, n, base):
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, text):
        values = list(map(int, text.split()))
        return cls(values)


if __name__ == "__main__":
    print("=== point factories ===")
    p1 = Point(3, 4)
    p2 = Point.from_string("3,4")
    p3 = Point.from_list([3, 4])
    p4 = Point.origin()
    print(p1, p2, p3, p4)

    print("\n=== cls in inheritance ===")
    cp = ColoredPoint.from_string("5,6")
    print(cp)
    print(type(cp))

    print("\n=== base-cost demo ===")
    table = CostTable.uniform(1)
    n = 255
    for base in range(2, 11):
        print(f"n={n}, base={base}, cost={table.total_cost(n, base)}")
