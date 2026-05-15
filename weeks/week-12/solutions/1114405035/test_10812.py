import subprocess

def run_test(input_str):
    process = subprocess.Popen(['python', '10812_manual.py'], 
                             stdin=subprocess.PIPE, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             text=True)
    stdout, stderr = process.communicate(input=input_str)
    return stdout

test_cases = """2
40 20
20 40
"""

expected_output = """30 10
impossible
"""

if __name__ == "__main__":
    print("Running tests for 10812_manual.py...")
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
