import subprocess
import sys

test_input = """1

5 2
2 1 2 3 4
=
2 1 3 2 5
<
"""

expected_output = """5
"""

result = subprocess.run([sys.executable, 'uva_948.py'], input=test_input, text=True, capture_output=True)

if result.returncode == 0:
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
else:
    print("Error:", result.stderr)