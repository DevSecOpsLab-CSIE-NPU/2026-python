from collections import Counter
import sys


def format_frequencies(line: str) -> str:
    """將單行文字轉成 UVA 10062 規定的輸出格式。"""
    counts = Counter(line)
    ordered_items = sorted(counts.items(), key=lambda item: (item[1], -ord(item[0])))
    return "\n".join(f"{ord(char)} {frequency}" for char, frequency in ordered_items)


def solve(data: str) -> str:
    """逐行統計字元頻率，案例之間以空白行分隔。"""
    if not data:
        return ""

    lines = data.splitlines()
    return "\n\n".join(format_frequencies(line) for line in lines)


def main() -> None:
    # UVA 10062 會一路讀到 EOF，因此直接把整份輸入讀進來處理即可。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()