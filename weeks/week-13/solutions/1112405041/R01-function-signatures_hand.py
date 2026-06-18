def add_all(*args): return sum(args)
def make_student(**kwargs): return kwargs
def solve():
    print(add_all(1, 2, 3))
    print(make_student(name="Test", grade=90))
if __name__ == '__main__': solve()
