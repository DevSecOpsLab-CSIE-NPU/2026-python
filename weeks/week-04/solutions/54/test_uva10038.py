import subprocess

test_input = "4 1 4 2 3\n5 1 4 2 -1 6\n3 2 1 3\n0"

result = subprocess.run(['python', 'uva10038.py'], 
                       input=test_input, 
                       capture_output=True, 
                       text=True)

print("Output:")
print(result.stdout)
