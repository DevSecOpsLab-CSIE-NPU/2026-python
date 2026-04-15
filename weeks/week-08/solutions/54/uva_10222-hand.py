import sys


def build_map() -> dict[str, str]:
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


KEYMAP = build_map()


def solve(data: str) -> str:
    return "\n".join("".join(KEYMAP.get(ch, ch) for ch in line) for line in data.splitlines())


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
