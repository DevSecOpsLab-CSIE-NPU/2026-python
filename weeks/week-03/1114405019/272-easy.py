import sys

def main():
    for line in sys.stdin:
        line = line.replace('"', '``', 1)
        while '``' in line and '"' in line:
            line = line.replace('"', "''", 1)
        print(line, end='')

if __name__ == "__main__":
    main()