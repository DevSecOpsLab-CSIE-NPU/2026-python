from collections import Counter, defaultdict

def summarize_logs(lines):
    if not lines:
        return {"user_counts": [], "top_action": ("", 0)}

    user_counter = Counter()
    action_counter = Counter()

    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
        user, action = parts[0], parts[1]
        user_counter[user] += 1
        action_counter[action] += 1

    user_sorted = sorted(
        user_counter.items(), key=lambda x: (-x[1], x[0])
    )
    top_action = action_counter.most_common(1)[0]

    return {"user_counts": user_sorted, "top_action": top_action}

def format_output(result):
    lines_out = []
    for user, count in result["user_counts"]:
        lines_out.append(f"{user} {count}")
    lines_out.append(f"top_action: {result['top_action'][0]} {result['top_action'][1]}")
    return "\n".join(lines_out)

def main():
    import sys
    lines = sys.stdin.read().strip().split("\n")
    if not lines or not lines[0].isdigit():
        return
    m = int(lines[0])
    log_lines = lines[1:1 + m]
    result = summarize_logs(log_lines)
    sys.stdout.write(format_output(result) + "\n")

if __name__ == "__main__":
    main()
