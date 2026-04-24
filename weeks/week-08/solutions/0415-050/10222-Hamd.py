import sys

def solve(text):
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    result = ""
    
    for char in text.lower():
        idx = keyboard.find(char)
        if idx >= 2:
            result += keyboard[idx - 2]
        else:
            result += char
            
    return result

if __name__ == '__main__':
    for line in sys.stdin:
        print(solve(line.rstrip('\n')))