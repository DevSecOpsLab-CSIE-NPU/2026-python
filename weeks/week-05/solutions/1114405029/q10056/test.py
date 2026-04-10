import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_test(inp):
    result = subprocess.run(["python3", "main.py"], input=inp, capture_output=True, text=True, cwd=script_dir)
    return result.stdout

def main():
    tests = [
        ("3\n3 0.1666667 1\n3 0.1666667 2\n2 0.5 1\n", "0.3956\n0.3297\n0.6667"),
    ]
    for inp, expected in tests:
        out = run_test(inp)
        if out == expected:
            print("PASS")
        else:
            print(f"FAIL: expected {expected!r}, got {out!r}")

if __name__ == "__main__":
    main()