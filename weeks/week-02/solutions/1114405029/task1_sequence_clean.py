def remove_duplicates(numbers):
    """Helper function to remove duplicates while keeping first occurrence order."""
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def main():
    line = input()
    numbers = list(map(int, line.split()))

    dedupe = remove_duplicates(numbers)
    asc = sorted(numbers)
    desc = sorted(numbers, reverse=True)
    evens = [num for num in numbers if num % 2 == 0]

    print(f"dedupe: {' '.join(map(str, dedupe))}")
    print(f"asc: {' '.join(map(str, asc))}")
    print(f"desc: {' '.join(map(str, desc))}")
    print(f"evens: {' '.join(map(str, evens))}")


if __name__ == "__main__":
    main()