import subprocess

input_data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5"""

expected_output = """Test #1: Symmetric.
Test #2: Non-symmetric."""

def run_test():
    with open('11349_test_input.py', 'w') as f:
        f.write(input_data)
        
    result = subprocess.run(['python3', '11349_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11349 ===")
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
