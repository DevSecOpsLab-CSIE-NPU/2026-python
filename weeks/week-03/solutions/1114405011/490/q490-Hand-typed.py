import sys

def solve(input_text):
    lines = input_text.splitlines()
    if not lines:
        return ""
    max_w = max(len(line) for line in lines)
    padded = [line.ljust(max_w) for line in lines]
    rotated = [''.join(col) for col in zip(*padded[::-1])]
    return '\n'.join(rotated)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))