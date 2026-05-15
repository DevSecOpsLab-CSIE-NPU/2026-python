import subprocess

def run_test(input_str):
    process = subprocess.Popen(['python', '10908_manual.py'], 
                             stdin=subprocess.PIPE, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             text=True)
    stdout, stderr = process.communicate(input=input_str)
    return stdout

test_cases = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""

expected_output = """7 10 4
3
1
5
1
"""

if __name__ == "__main__":
    print("Running tests for 10908_manual.py...")
    output = run_test(test_cases)
    print("Input:")
    print(test_cases)
    print("Output:")
    print(output)
    if output.strip() == expected_output.strip():
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected:")
        print(expected_output)
