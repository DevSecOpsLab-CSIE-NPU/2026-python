import subprocess
import sys

# Test cases
test_input = """3
This is a test
Hello World
Python Programming
"""

expected_output = """T 4
O 4
I 3
N 3
H 3
S 3
A 2
L 2
P 2
R 2
G 2
M 2
E 1
W 1
D 1
Y 1
"""

# Run the program
result = subprocess.run([sys.executable, 'uva_10008.py'], input=test_input, text=True, capture_output=True)

if result.returncode == 0:
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
        print("Expected:")
        print(expected_output)
        print("Got:")
        print(result.stdout)
else:
    print("Error:", result.stderr)