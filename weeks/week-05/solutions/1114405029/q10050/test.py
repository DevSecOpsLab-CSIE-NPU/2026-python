import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_test(inp):
    result = subprocess.run(["python3", "main.py"], input=inp, capture_output=True, text=True, cwd=script_dir)
    return result.stdout

def main():
    tests = [
        ("2\n100\n4\n3\n4\n12\n15\n14\n3\n3\n4\n8\n", "37\n5"),
    ]
    for inp, expected in tests:
        out = run_test(inp)
        if out == expected:
            print("PASS")
        else:
            print(f"FAIL: expected {expected!r}, got {out!r}")

if __name__ == "__main__":
    main()