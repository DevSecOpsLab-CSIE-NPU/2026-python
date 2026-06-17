"""A02: context manager patterns with class and @contextmanager."""

import io
import sys
import time
from contextlib import contextmanager
from pathlib import Path


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print("timer start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"timer end: {elapsed:.4f}s")
        return False


@contextmanager
def section(title):
    print("\n" + "=" * 36)
    print(title)
    print("=" * 36)
    yield
    print("-" * 36)


@contextmanager
def capture_output():
    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout


def solve_parity(n):
    bits = bin(n)[2:]
    ones = bits.count("1")
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")


if __name__ == "__main__":
    print("=== with file auto close ===")
    demo_file = Path(__file__).with_name("week13_demo.txt")
    with demo_file.open("w", encoding="utf-8") as f:
        f.write("Hello from Week 13\n")

    with demo_file.open("r", encoding="utf-8") as f:
        print(f.read().strip())

    print("\n=== custom Timer ===")
    with Timer():
        total = sum(range(1_000_000))
        print("sum:", total)

    with section("Week 13 CPE mock"):
        print("problem: UVA 11005")
        print("time limit: 20 min")

    print("\n=== capture stdout for testing ===")
    with capture_output() as out:
        solve_parity(7)
    captured = out.getvalue()
    print("captured:")
    print(captured.strip())
    print("lines:", len(captured.strip().splitlines()))
