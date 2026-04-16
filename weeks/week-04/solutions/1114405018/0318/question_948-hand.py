import sys

def match(coin: int, heavy: bool, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in weighings:
        if coin in left:
            expect = ">" if heavy else "<"
        elif coin in right:
            expect = "<" if heavy else ">"
        else:
            expect = "="

        if expect != result:
            return False

    return True

tokens = iter(sys.stdin.read().split())
t = int(next(tokens))
answers = []

for _ in range(t):
    n = int(next(tokens))
    k = int(next(tokens))

    weighings = []
    for _ in range(k):
        p = int(next(tokens))
        left = [int(next(tokens)) for _ in range(p)]
        right = [int(next(tokens)) for _ in range(p)]
        result = next(tokens)
        weighings.append((left, right, result))

    candidates = []
    for coin in range(1, n + 1):
        if match(coin, True, weighings) or match(coin, False, weighings):
            candidates.append(coin)

    answers.append(str(candidates[0]) if len(candidates) == 1 else "0")

print("\n\n".join(answers))
