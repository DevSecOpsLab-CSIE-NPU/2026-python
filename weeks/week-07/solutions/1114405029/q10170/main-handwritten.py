import sys

def solve():
    for line in sys.stdin:
        try:
            parts = line.split()
            if not parts:
                break
            
            s = int(parts[0])
            d = int(parts[1])
            
            current_people = s
            while d > 0:
                d -= current_people
                if d <= 0:
                    print(current_people)
                    break
                current_people += 1
                
        except EOFError:
            break

if __name__ == "__main__":
    solve()