import sys

DIVISOR = 3  # 學號末兩碼19，個位 u=9，u%4+2=3


def clean_sequence(numbers: list[int], divisor: int) -> list[int]:
    seen = set()
    deduped = []
    for x in numbers:
        if x not in seen:
            seen.add(x)
            deduped.append(x)
    filtered = [x for x in deduped if x % divisor == 0]
    return sorted(filtered)


def format_result(result: list[int]) -> str:
    if not result:
        return "NONE"
    return " ".join(str(x) for x in result)


def main() -> None:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())
        if n == 0:
            break
        numbers = list(map(int, sys.stdin.readline().split()))
        print(format_result(clean_sequence(numbers, DIVISOR)))


if __name__ == "__main__":
    main()
