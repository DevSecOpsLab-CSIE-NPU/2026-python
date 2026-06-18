from contextlib import contextmanager
@contextmanager
def section(title):
    print(f"=== {title} ==="); yield; print("=" * 10)
if __name__ == '__main__':
    with section("Test"): print("Logic running")
