import subprocess

test_cases = [
    ("1\n3 1\n3\n1 2 3 1 2\n=", "3"),
]

for i, (test_input, expected) in enumerate(test_cases):
    result = subprocess.run(['python', 'uva948.py'], 
                           input=test_input, 
                           capture_output=True, 
                           text=True)
    actual = result.stdout.strip()
    status = "PASS" if actual == expected else "FAIL"
    print(f"Test {i+1}: {status}")
