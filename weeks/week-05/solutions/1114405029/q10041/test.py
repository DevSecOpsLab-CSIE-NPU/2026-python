import subprocess
import sys
import os

def run_test(inp):
    result = subprocess.run(["python3", "main.py"], input=inp, capture_output=True, text=True, cwd=os.path.dirname(__file__))
    return result.stdout

def main():
    tests = [
        ("2\n3 2 4 100\n8 10 20 15 200 199 1000 300 400 500\n", "98\n1656"),
    ]
    for inp, expected in tests:
        out = run_test(inp)
        if out == expected:
            print("PASS")
        else:
            print(f"FAIL: expected {expected!r}, got {out!r}")

if __name__ == "__main__":
    main()