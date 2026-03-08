from collections import Counter, defaultdict


def parse_input(lines: list[str]) -> list[tuple[str, str]]:
	if not lines:
		return []

	m = int(lines[0])
	events: list[tuple[str, str]] = []
	for row in lines[1 : 1 + m]:
		user, action = row.split()
		events.append((user, action))
	return events


def summarize(events: list[tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str, int]]:
	user_count = defaultdict(int)
	action_count = Counter()

	for user, action in events:
		user_count[user] += 1
		action_count[action] += 1

	user_summary = sorted(user_count.items(), key=lambda x: (-x[1], x[0]))

	if not action_count:
		return user_summary, ("None", 0)

	top_action = min(action_count.items(), key=lambda x: (-x[1], x[0]))
	return user_summary, top_action


def format_output(user_summary: list[tuple[str, int]], top_action: tuple[str, int]) -> str:
    lines = [f"{user} {count}" for user, count in user_summary]
    lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    return "\n".join(lines)


def main() -> None:
	first = input().strip()
	if first == "":
		print("top_action: None 0")
		return

	m = int(first)
	lines = [first]
	for _ in range(m):
		lines.append(input().strip())

	events = parse_input(lines)
	user_summary, top_action = summarize(events)
	print(format_output(user_summary, top_action))


if __name__ == "__main__":
    main()
