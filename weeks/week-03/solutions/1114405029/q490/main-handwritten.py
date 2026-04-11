import sys

def solve():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    
    if not lines:
        return

    max_length = 0
    for l in lines:
        if len(l) > max_length:
            max_length = len(l)
            
    for char_index in range(max_length):
        result_row = ""
        for line_index in range(len(lines) - 1, -1, -1):
            current_sentence = lines[line_index]
            if char_index < len(current_sentence):
                result_row += current_sentence[char_index]
            else:
                result_row += " "
        print(result_row)

if __name__ == "__main__":
    solve()