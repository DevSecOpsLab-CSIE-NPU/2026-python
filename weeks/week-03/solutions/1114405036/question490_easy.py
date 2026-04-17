def rotate_text(lines):
    width = max(len(line) for line in lines) if lines else 0
    padded = [line.ljust(width) for line in lines]
    out = []
    for c in range(width):
        row = ''.join(padded[r][c] for r in range(len(padded) - 1, -1, -1))
        out.append(row.rstrip())
    return out

if __name__ == '__main__':
    import sys
    print('\n'.join(rotate_text(sys.stdin.read().splitlines())))
