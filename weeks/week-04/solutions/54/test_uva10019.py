import subprocess

test_input = "100 25\n46 147\n999 1\n123 456\n1000000000000 999999999999"

result = subprocess.run(['python', 'uva10019.py'], 
                       input=test_input, 
                       capture_output=True, 
                       text=True)

print("Output:")
print(result.stdout)
