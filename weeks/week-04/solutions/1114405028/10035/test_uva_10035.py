import subprocess
import sys

test_input = """123 456
555 555
123 594
0 0
"""

expected_output = """No carry operation.
3 carry operations.
1 carry operation.
"""

result = subprocess.run([sys.executable, 'uva_10035.py'], input=test_input, text=True, capture_output=True)

if result.returncode == 0:
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
else:
    print("Error:", result.stderr)