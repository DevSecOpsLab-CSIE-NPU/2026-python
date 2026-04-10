from collections import namedtuple
from pathlib import Path

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


def load_generals_easy(filename="generals.txt"):
    data = {}
    path = Path(__file__).resolve().parents[1] / filename

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()
            if not text or text == "EOF":
                if text == "EOF":
                    break
                continue

            faction, name, hp, atk, def_, spd, is_leader = text.split()
            data[name] = General(
                faction,
                name,
                int(hp),
                int(atk),
                int(def_),
                int(spd),
                is_leader == "True",
            )

    return data


def battle_order_easy(generals):
    return sorted(generals.values(), key=lambda g: g.spd, reverse=True)


if __name__ == "__main__":
    generals = load_generals_easy()
    print("Top 3 speed generals:")
    for g in battle_order_easy(generals)[:3]:
        print(f"- {g.name} ({g.spd})")
