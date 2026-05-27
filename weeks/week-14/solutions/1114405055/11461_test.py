import subprocess

input_data = """1 4
1 10
1 100000
0 0"""

expected_output = """2
3
316"""

def run_test():
    result = subprocess.run(['python3', '11461_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11461 ===")
    print("Output:")
    print(result.stdout.strip())
    print("Expected:")
    print(expected_output.strip())
    if result.stdout.strip() == expected_output.strip():
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == '__main__':
    run_test()
