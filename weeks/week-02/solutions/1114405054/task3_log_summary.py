from collections import Counter
def summarize_logs(logs):
    if not logs: return [], None, 0
    uc = Counter(u for u, a in logs)
    ac = Counter(a for u, a in logs)
    return sorted(uc.items(), key=lambda x: (-x[1], x[0])), ac.most_common(1)[0][0], ac.most_common(1)[0][1]
