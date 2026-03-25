from __future__ import annotations


def solve_io(data: str) -> str:
    nums = data.split()
    result: list[str] = []
    idx = 0
    while idx + 1 < len(nums):
        a = int(nums[idx])
        b = int(nums[idx + 1])
        result.append(str(abs(a - b)))
        idx += 2
    return "\n".join(result)


def main() -> None:
    import sys

    text = sys.stdin.read()
    out = solve_io(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
