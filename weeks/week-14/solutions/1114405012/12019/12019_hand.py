import sys
from datetime import date

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    t = int(lines[0])
    answers = []

    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())
        answers.append(WEEKDAYS[date(2012, m, d).weekday()])

    sys.stdout.write("\n".join(answers))
if __name__ == "__main__":
    main()
