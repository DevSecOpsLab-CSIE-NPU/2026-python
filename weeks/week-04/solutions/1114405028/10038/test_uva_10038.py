import subprocess
import sys

test_input = """4 1 4 2 3
5 1 4 2 -1 6
"""

expected_output = """Jolly
Not jolly
"""

result = subprocess.run([sys.executable, 'uva_10038.py'], input=test_input, text=True, capture_output=True)

if result.returncode == 0:
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
else:
    print("Error:", result.stderr)