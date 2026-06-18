class Score:
    def __init__(self, v): self.v = v
    def __repr__(self): return f"Score({self.v})"
    def __eq__(self, o): return self.v == o.v
if __name__ == '__main__':
    print(Score(80) == Score(80))
