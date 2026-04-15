import sys


def make_map() -> dict[str, str]:
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]
    mp: dict[str, str] = {}
    for row in rows:
        for i in range(1, len(row)):
            key = row[i]
            prev = row[i - 1]
            mp[key] = prev
            if key.isalpha():
                mp[key.upper()] = prev.upper()
    return mp


KEYMAP = make_map()


def solve(data: str) -> str:
    lines = []
    for line in data.splitlines():
        lines.append("".join(KEYMAP.get(ch, ch) for ch in line))
    return "\n".join(lines)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
