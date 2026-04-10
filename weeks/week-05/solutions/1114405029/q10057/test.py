import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_test(inp):
    result = subprocess.run(["python3", "main.py"], input=inp, capture_output=True, text=True, cwd=script_dir)
    return result.stdout

def main():
    tests = [
        ("2\n10\n1 2 3 4 5 6 7 8 9 10\n3\n2 2 2\n", "1 9 10\n3 1 2\n8 6 1\n2 0 1"),
    ]
    for inp, expected in tests:
        out = run_test(inp)
        if out == expected:
            print("PASS")
        else:
            print(f"FAIL: expected {expected!r}, got {out!r}")

if __name__ == "__main__":
    main()