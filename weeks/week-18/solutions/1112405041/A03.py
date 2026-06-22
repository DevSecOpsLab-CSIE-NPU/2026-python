def digit_root_in_base(x, base):
    raise NotImplementedError


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digit_root_in_base(x, base=8))


if __name__ == "__main__":
    main()
