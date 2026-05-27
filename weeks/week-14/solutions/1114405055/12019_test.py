import subprocess

input_data = """8
1 6
2 28
4 5
5 26
8 1
11 1
12 25
12 31"""

expected_output = """Thursday
Monday
Tuesday
Thursday
Monday
Tuesday
Sunday
Saturday"""

def run_test():
    result = subprocess.run(['python3', '12019_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 12019 ===")
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
