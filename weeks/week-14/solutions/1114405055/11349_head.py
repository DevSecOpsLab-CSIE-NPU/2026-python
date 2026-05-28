import sys

def process():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for c in range(1, t + 1):
        while idx < len(data) and data[idx] != '=':
            idx += 1
        idx += 1
        n = int(data[idx])
        idx += 1
        
        arr = []
        for _ in range(n * n):
            arr.append(int(data[idx]))
            idx += 1
            
        sym = True
        for x in arr:
            if x < 0:
                sym = False
                break
        if sym:
            for i in range(len(arr) // 2):
                if arr[i] != arr[len(arr) - 1 - i]:
                    sym = False
                    break
        if sym:
            print(f"Test #{c}: Symmetric.")
        else:
            print(f"Test #{c}: Non-symmetric.")

if __name__ == '__main__':
    process()
