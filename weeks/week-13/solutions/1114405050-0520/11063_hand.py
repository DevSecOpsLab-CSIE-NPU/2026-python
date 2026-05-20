import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    tokens = iter(input_data)
    
    while True:
        try: n = int(next(tokens))
        except StopIteration: break
        
        total_pixels = n * n
        sum_y = 0.0
        for _ in range(total_pixels):
            r, g, b = int(next(tokens)), int(next(tokens)), int(next(tokens))
            x = 0.5149 * r + 0.3244 * g + 0.1607 * b
            y = 0.2654 * r + 0.6704 * g + 0.0642 * b
            z = 0.0248 * r + 0.1248 * g + 0.8504 * b
            sum_y += y
            print(f"{x:.4f} {y:.4f} {z:.4f}")
        print(f"The average of Y is {sum_y / total_pixels:.4f}")

if __name__ == '__main__':
    main()