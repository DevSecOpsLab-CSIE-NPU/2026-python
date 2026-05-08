def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    if not lines:
        return ''

    results = []
    for line in lines:
        a, b = line.split()
        diff = abs(int(a) - int(b))
        results.append(str(diff))
    return '\n'.join(results)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
