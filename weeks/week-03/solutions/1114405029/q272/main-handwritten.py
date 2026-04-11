import sys

def solve():
    first = True
    data = sys.stdin.read()
    output = ""
    
    for char in data:
        if char == '"':
            if first:
                output += "``"
                first = False
            else:
                output += "''"
                first = True
        else:
            output += char
            
    print(output, end="")

if __name__ == "__main__":
    solve()