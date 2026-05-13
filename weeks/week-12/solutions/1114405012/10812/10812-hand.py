import  sys

def main() -> None:
    line = sys.stdin.readline().strip()
    if not line:
        return

    count = int(line)
    output = []

    for _ in range(count):
        total, diff = map(int, sys.stdin.readline().split())
    
        if diff > total or (total + diff) % 2 == 1:
            output.append("impossible")
            continue
        big = (total + diff) // 2
        small = (total - diff) // 2
        output.append(f"{big} {small}")
    sys.stdout.write("\n".join(output))