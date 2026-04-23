# 01.py
# Variables and Assignment

def demonstrate_assignment():
    a = 10
    b = 20
    a, b = b, a  # Swap
    return a, b

if __name__ == "__main__":
    x, y = demonstrate_assignment()
    print(f"a: {x}, b: {y}")
