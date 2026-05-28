import subprocess

input_data = """10
100
500
0"""

expected_output = """67
13015
442011"""

def run_test():
    result = subprocess.run(['python3', '11417_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11417 ===")
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
