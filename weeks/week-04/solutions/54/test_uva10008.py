import subprocess

test_input = "3\nthis is a test\nabc\nXYZ"

result = subprocess.run(['python', 'uva10008.py'], 
                       input=test_input, 
                       capture_output=True, 
                       text=True)

print("Output:")
print(result.stdout)
