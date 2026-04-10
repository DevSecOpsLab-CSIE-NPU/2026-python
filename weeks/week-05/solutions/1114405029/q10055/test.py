import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_test(inp):
    result = subprocess.run(["python3", "main.py"], input=inp, capture_output=True, text=True, cwd=script_dir)
    return result.stdout

def main():
    tests = [
        ("3 5\n1 2\n2 1 3\n2 1 2\n1 3\n2 2 3\n", "1\n1\n0"),
    ]
    for inp, expected in tests:
        out = run_test(inp)
        if out == expected:
            print("PASS")
        else:
            print(f"FAIL: expected {expected!r}, got {out!r}")

if __name__ == "__main__":
    main()