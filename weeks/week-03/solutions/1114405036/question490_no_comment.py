def rotate_text(lines):
    width = max((len(line) for line in lines), default=0)
    padded = [line.ljust(width) for line in lines]
    return [''.join(padded[r][c] for r in range(len(padded) - 1, -1, -1)).rstrip() for c in range(width)]

if __name__ == '__main__':
    import sys
    print('\n'.join(rotate_text(sys.stdin.read().splitlines())))
