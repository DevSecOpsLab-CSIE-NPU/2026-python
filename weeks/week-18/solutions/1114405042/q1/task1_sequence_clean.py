D = 4

def process_sequence(text):
    items = [int(x) for x in text.strip().split()]
    deduped = dedupe_preserve_order(items)
    filtered = [x for x in deduped if x % D == 0]
    result = sorted(filtered)
    return {"result": result}

def dedupe_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def format_output(result):
    return " ".join(str(x) for x in result["result"])

def main():
    import sys
    line = sys.stdin.readline()
    if not line.strip():
        return
    result = process_sequence(line)
    sys.stdout.write(format_output(result) + "\n")

if __name__ == "__main__":
    main()
