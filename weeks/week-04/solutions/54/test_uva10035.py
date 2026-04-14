import subprocess

test_input = "12 8\n123 456\n0 0"

result = subprocess.run(['python', 'uva10035.py'], 
                       input=test_input, 
                       capture_output=True, 
                       text=True)

print("Output:")
print(result.stdout)
